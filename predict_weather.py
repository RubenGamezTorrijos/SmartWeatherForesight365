import pandas as pd
import pickle
from datetime import datetime, timedelta
import os


def load_model(model_path):
    """
    Carga el modelo entrenado desde un archivo .pkl.
    """
    with open(model_path, 'rb') as file:
        return pickle.load(file)


def load_feature_order(features_path):
    """
    Carga el orden de las características desde un archivo.
    """
    with open(features_path, 'r') as file:
        return file.read().splitlines()


def load_recent_data(csv_path):
    """
    Carga los datos históricos más recientes desde un archivo CSV.
    """
    data = pd.read_csv(csv_path, index_col=0, parse_dates=True)
    data = data.fillna(data.mean())  # Manejar valores faltantes

    # Agregar características temporales
    data['day_of_year'] = data.index.dayofyear
    data['month'] = data.index.month
    data['week_of_year'] = data.index.isocalendar().week

    return data.iloc[-1]  # Última fila como base


def predict_future(model, recent_data, days_to_predict, feature_order):
    """
    Genera predicciones automáticas para un horizonte temporal futuro.

    Args:
        model: Modelo entrenado.
        recent_data (pd.Series): Datos históricos más recientes.
        days_to_predict (int): Número de días en el futuro para predecir.
        feature_order (list): Orden de características esperado por el modelo.

    Returns:
        pd.DataFrame: Predicciones para los días futuros.
    """
    predictions = []
    current_data = recent_data.copy()
    current_date = datetime.now()

    days_to_predict = min(days_to_predict, 365)  # Limitar predicción a 1 año máximo

    for day in range(1, days_to_predict + 1):
        # Generar características futuras
        current_data['day_of_year'] = (current_date.timetuple().tm_yday % 365) + 1
        current_data['month'] = current_date.month
        current_data['week_of_year'] = current_date.isocalendar()[1]  # Corregido: extraer semana

        # Asegurar el orden de características
        features_df = pd.DataFrame([current_data[feature_order].values], columns=feature_order)

        # Realizar la predicción
        predicted_values = model.predict(features_df)[0]

        # Guardar las predicciones en la tabla de resultados
        predictions.append({
            'date': current_date.strftime("%Y-%m-%d"),
            'predicted_tavg': predicted_values[0],
            'predicted_tmin': predicted_values[0] - 2,  # Simulación
            'predicted_tmax': predicted_values[0] + 2,  # Simulación
            'predicted_wspd': predicted_values[1],
            'predicted_pres': predicted_values[2],
        })

        # Actualizar la fecha para la siguiente predicción
        current_date += timedelta(days=1)

    return pd.DataFrame(predictions)


if __name__ == "__main__":
    city = input("Introduce el nombre de la ciudad (ejemplo: Madrid): ")
    days_to_predict = int(input("Introduce el número de días futuros para predecir (máximo 365 días): "))
    csv_path = f"datasets/{city}_historical_weather.csv"
    model_path = f"models/{city}_weather_model.pkl"
    features_path = f"models/{city}_features.txt"

    os.makedirs('predictions', exist_ok=True)

    try:
        # Cargar el modelo y las características
        model = load_model(model_path)
        feature_order = load_feature_order(features_path)
        recent_data = load_recent_data(csv_path)

        # Generar predicciones
        predictions = predict_future(model, recent_data, days_to_predict, feature_order)

        # Mostrar y guardar predicciones
        print("Predicciones futuras:")
        print(predictions)

        output_file = f"predictions/{city}_future_predictions.csv"
        predictions.to_csv(output_file, index=False)
        print(f"Predicciones guardadas en {output_file}")
    except Exception as e:
        print(f"Error: {e}")
