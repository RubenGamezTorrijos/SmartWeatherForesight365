import requests
import logging
import pandas as pd
from datetime import datetime, timedelta
import os

# Configuración del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WeatherAPIController:
    def __init__(self):
        self.API_KEY = "fe5d411a2cmsh1b597687f803a91p115ad4jsnf2229f917062"
        self.BASE_URL = "https://meteostat.p.rapidapi.com"
        self.HEADERS = {
            "X-RapidAPI-Key": self.API_KEY,
            "X-RapidAPI-Host": "meteostat.p.rapidapi.com"
        }
        
    def get_request(self, endpoint, params=None, headers=None):
        """
        Realiza una solicitud GET a la API de Meteostat.
        """
        url = f"{self.BASE_URL}{endpoint}"
        headers = headers or self.HEADERS
        try:
            logging.info(f"Realizando solicitud GET a {url} con parámetros: {params}")
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            logging.info("Respuesta recibida correctamente.")
            return data
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"Error HTTP al conectar con la API: {http_err}")
        except requests.exceptions.RequestException as req_err:
            logging.error(f"Error de conexión con la API: {req_err}")
        except ValueError as val_err:
            logging.error(f"Error al decodificar la respuesta JSON: {val_err}")
        return None

    def get_coordinates(self, city: str) -> tuple:
        """
        Obtiene las coordenadas de una ciudad usando OpenStreetMap.
        """
        url = "https://nominatim.openstreetmap.org/search"
        params = {"q": f"{city}, España", "format": "json", "limit": 1}
        headers = {"User-Agent": "WeatherInsight/1.0 (soporte@ejemplo.com)"}
        
        try:
            logging.info(f"Buscando coordenadas para la ciudad: {city}")
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            data = response.json()
            
            if data:
                lat, lon = float(data[0]["lat"]), float(data[0]["lon"])
                logging.info(f"Coordenadas para {city}: (Lat: {lat}, Lon: {lon})")
                return lat, lon
            else:
                logging.warning(f"No se encontraron resultados para la ciudad: {city}")
                
        except requests.exceptions.RequestException as e:
            logging.error(f"Error al obtener coordenadas para la ciudad {city}: {e}")
        except (KeyError, ValueError) as e:
            logging.error(f"Error al procesar la respuesta de coordenadas: {e}")
            
        return None, None

    def get_historical_data(self, city: str, start_date: datetime, end_date: datetime) -> pd.DataFrame:
        """
        Obtiene datos históricos del clima para una ciudad específica y los guarda en un CSV.
        """
        try:
            # Obtener coordenadas de la ciudad
            lat, lon = self.get_coordinates(city)
            if not lat or not lon:
                raise ValueError(f"No se pudieron obtener coordenadas para: {city}")

            # Formatear fechas
            start_str = start_date.strftime("%Y-%m-%d")
            end_str = end_date.strftime("%Y-%m-%d")

            # Obtener datos meteorológicos
            endpoint = "/point/daily"
            params = {
                "lat": lat,
                "lon": lon,
                "start": start_str,
                "end": end_str
            }

            logging.info(f"Solicitando datos meteorológicos para {city}")
            response_data = self.get_request(endpoint, params=params)

            if response_data and "data" in response_data:
                # Convertir a DataFrame
                df = pd.DataFrame(response_data["data"])
                
                # Añadir columna de ciudad y fecha
                df['city'] = city
                df['date'] = pd.to_datetime(df['date'])
                
                # Guardar datos en CSV
                csv_path = f"datasets/{city}_Historial_Weather.csv"
                logging.info(f"Intentando guardar datos en: {csv_path}")
                df.to_csv(csv_path, index=False)
                if os.path.exists(csv_path):
                    logging.info(f"Archivo CSV creado exitosamente: {csv_path}")
                else:
                    logging.error(f"No se pudo crear el archivo CSV: {csv_path}")
                logging.info(f"Datos guardados en {csv_path}")
                
                return df
            else:
                raise ValueError("No se obtuvieron datos de la API")

        except Exception as e:
            logging.error(f"Error al obtener datos históricos: {str(e)}")
            raise

    def get_weather_data(self, lat: float, lon: float, start_date: str, end_date: str) -> dict:
        """
        Obtiene datos meteorológicos específicos para unas coordenadas.
        """
        endpoint = "/point/daily"
        params = {
            "lat": lat,
            "lon": lon,
            "start": start_date,
            "end": end_date
        }
        
        try:
            logging.info(f"Solicitando datos meteorológicos para Lat: {lat}, Lon: {lon}")
            data = self.get_request(endpoint, params=params)
            
            if data and "data" in data:
                logging.info("Datos meteorológicos recibidos correctamente.")
                return data["data"]
            else:
                logging.warning("No se encontraron datos meteorológicos para las fechas especificadas.")
                
        except Exception as e:
            logging.error(f"Error al obtener datos meteorológicos: {e}")
            
        return None
