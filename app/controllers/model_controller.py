from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import os
import logging
import pandas as pd

class ModelController:
    def __init__(self):
        self.models = {
            'temp': RandomForestRegressor(n_estimators=100, random_state=42),
            'temp_min': RandomForestRegressor(n_estimators=100, random_state=42),
            'temp_max': RandomForestRegressor(n_estimators=100, random_state=42),
            'precipitacion': RandomForestRegressor(n_estimators=100, random_state=42),
            'nieve': RandomForestRegressor(n_estimators=100, random_state=42),
            'direccion_viento': RandomForestRegressor(n_estimators=100, random_state=42),
            'velocidad_viento': RandomForestRegressor(n_estimators=100, random_state=42),
            'punto_rocio': RandomForestRegressor(n_estimators=100, random_state=42),
            'presion': RandomForestRegressor(n_estimators=100, random_state=42)
        }
        self.scalers = {param: StandardScaler() for param in self.models.keys()}

    def train_model(self, data: pd.DataFrame, city: str):
        """
        Entrena los modelos de predicción y los guarda.
        """
        try:
            features = [
                'temp', 'temp_min', 'temp_max', 'precipitacion', 'nieve',
                'direccion_viento', 'velocidad_viento', 'punto_rocio', 'presion'
            ]
            
            os.makedirs("ml", exist_ok=True)
            
            for target in features:
                # Preparar features (usar todos los parámetros excepto el objetivo)
                X = data[[col for col in features if col != target]]
                y = data[target].shift(-1)  # Predecir el valor del día siguiente

                # Eliminar la última fila
                X = X[:-1]
                y = y[:-1]

                # Escalar features
                X_scaled = self.scalers[target].fit_transform(X)

                # Split y entrenamiento
                X_train, X_test, y_train, y_test = train_test_split(
                    X_scaled, y, test_size=0.2, random_state=42
                )

                # Entrenar modelo
                self.models[target].fit(X_train, y_train)

                # Guardar modelo y scaler
                model_path = f"ml/{city}_{target}_Model.pkl"
                scaler_path = f"ml/{city}_{target}_Scaler.pkl"
                
                joblib.dump(self.models[target], model_path)
                joblib.dump(self.scalers[target], scaler_path)
                
                logging.info(f"Modelo y scaler guardados para {city} - {target}")

            logging.info(f"Todos los modelos entrenados y guardados para {city}")

        except Exception as e:
            logging.error(f"Error al entrenar los modelos: {str(e)}")
            raise

    def load_models(self, city: str):
        """
        Carga los modelos de predicción guardados.
        """
        try:
            features = [
                'temp', 'temp_min', 'temp_max', 'precipitacion', 'nieve',
                'direccion_viento', 'velocidad_viento', 'punto_rocio', 'presion'
            ]
            
            for target in features:
                model_path = f"ml/{city}_{target}_Model.pkl"
                scaler_path = f"ml/{city}_{target}_Scaler.pkl"

                if not os.path.exists(model_path) or not os.path.exists(scaler_path):
                    raise FileNotFoundError(f"No se encontró el modelo o el scaler para {city} - {target}")

                self.models[target] = joblib.load(model_path)
                self.scalers[target] = joblib.load(scaler_path)
                logging.info(f"Modelo y scaler cargados para {city} - {target}")

            logging.info(f"Todos los modelos cargados para {city}")

        except Exception as e:
            logging.error(f"Error al cargar los modelos: {str(e)}")
            raise

