import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DataController:
    def __init__(self):
        self.data_dir = "datasets"

    def load_and_clean_data(self, city: str) -> pd.DataFrame:
        """
        Carga y limpia los datos históricos del clima para una ciudad específica.
        """
        try:
            file_path = os.path.join(self.data_dir, f"{city}_Historial_Weather.csv")
            if not os.path.exists(file_path):
                logging.error(f"Archivo no encontrado: {file_path}")
                raise FileNotFoundError(f"No se encontraron datos históricos para {city}")

            logging.info(f"Intentando cargar datos desde: {file_path}")
            data = pd.read_csv(file_path)
            
            # Convertir fecha a datetime
            data['date'] = pd.to_datetime(data['date'])

            # Mapeo exacto de columnas como vienen de la API
            column_mapping = {
                'tavg': 'temp',
                'tmin': 'temp_min',
                'tmax': 'temp_max',
                'prcp': 'precipitacion',
                'snow': 'nieve',
                'wdir': 'direccion_viento',
                'wspd': 'velocidad_viento',
                'wpgt': 'punto_rocio',
                'pres': 'presion'
            }

            # Verificar qué columnas están presentes en los datos
            present_columns = []
            for api_col, new_col in column_mapping.items():
                if api_col in data.columns:
                    data = data.rename(columns={api_col: new_col})
                    present_columns.append(new_col)
                else:
                    logging.warning(f"Columna {api_col} no encontrada en los datos")
                    data[new_col] = pd.NA

            logging.info(f"Columnas presentes después del mapeo: {present_columns}")

            # Asegurar que todas las columnas necesarias existen
            required_columns = [
                'temp', 'temp_min', 'temp_max', 'precipitacion',
                'nieve', 'direccion_viento', 'velocidad_viento',
                'punto_rocio', 'presion'
            ]

            # Rellenar valores faltantes
            for col in required_columns:
                if col in ['nieve', 'direccion_viento']:
                    data[col] = data[col].fillna(0)
                else:
                    data[col] = data[col].fillna(data[col].mean() if not pd.isna(data[col]).all() else 0)

            # Eliminar duplicados y ordenar por fecha
            data = data.drop_duplicates().sort_values('date')

            logging.info(f"Datos procesados para {city}. Shape: {data.shape}")
            logging.info(f"Columnas finales: {data.columns.tolist()}")
            
            return data

        except Exception as e:
            logging.error(f"Error al cargar y limpiar datos: {str(e)}")
            raise
