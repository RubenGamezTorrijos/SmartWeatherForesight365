import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import pickle

def load_data(csv_path):
    """
    Cargar los datos históricos desde un archivo CSV y procesarlos.
    """
    data = pd.read_csv(csv_path, index_col=0, parse_dates=True)
    data = data.fillna(data.mean())  # Manejar valores faltantes

    # Agregar características temporales
    data['day_of_year'] = data.index.dayofyear
    data['month'] = data.index.month
    data['week_of_year'] = data.index.isocalendar().week

    # Ajustar características y objetivos basados en las columnas disponibles
    features = ['tmin', 'tmax', 'prcp', 'wspd', 'pres', 'day_of_year', 'month', 'week_of_year']
    targets = ['tavg', 'wspd', 'pres']

    if not all([col in data.columns for col in features + targets]):
        raise ValueError(f"El CSV no tiene las columnas requeridas. Columnas encontradas: {list(data.columns)}")

    return data[features], data[targets]

def train_model(X, y, model_path, features_path):
    """
    Entrena un modelo para predecir múltiples variables climáticas y lo guarda en un archivo.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = MultiOutputRegressor(RandomForestRegressor(n_estimators=100, random_state=42))
    model.fit(X_train, y_train)

    # Evaluar el modelo
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred, multioutput='raw_values')
    rmse = mean_squared_error(y_test, y_pred, multioutput='raw_values', squared=False)
    print("MAE por variable:", mae)
    print("RMSE por variable:", rmse)

    # Guardar el modelo entrenado
    with open(model_path, 'wb') as file:
        pickle.dump(model, file)
        print(f"Modelo guardado en {model_path}")

    # Guardar el orden de las características
    with open(features_path, 'w') as file:
        file.write('\n'.join(X.columns))
        print(f"Orden de características guardado en {features_path}")

if __name__ == "__main__":
    city = input("Introduce el nombre de la ciudad (ejemplo: Valencia): ")
    csv_path = f"datasets/{city}_historical_weather.csv"
    model_path = f"models/{city}_weather_model.pkl"
    features_path = f"models/{city}_features.txt"

    os.makedirs("models", exist_ok=True)

    try:
        X, y = load_data(csv_path)
        train_model(X, y, model_path, features_path)
    except Exception as e:
        print(f"Error: {e}")
