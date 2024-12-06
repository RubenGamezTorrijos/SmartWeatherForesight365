# app/generate_dataset.py
from app.predict_weather import predecir_clima   # Importación relativa dentro de 'app'
from app.train_model import entrenar_modelo      # Importación desde 'train_model.py' dentro de 'app'
from app.coordinates_util import obtener_coordenadas  # Importación desde 'coordinates_util.py' dentro de 'app'
from meteostat import Point, Daily
from datetime import datetime

# librerías importar
import pandas as pd
import requests
import os

def get_coordinates(city):
    """
    Obtiene las coordenadas (latitud y longitud) de una ciudad utilizando Nominatim (OpenStreetMap).
    """
    url = f"https://nominatim.openstreetmap.org/search"
    params = {"q": city, "format": "json", "limit": 1}
    headers = {"User-Agent": "WeatherSmartApp/1.0 (your_email@example.com)"}
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200 and len(response.json()) > 0:
        data = response.json()[0]
        return float(data["lat"]), float(data["lon"])
    else:
        print(f"Error al obtener coordenadas para la ciudad: {city}.")
        return None, None

def fetch_historical_weather(lat, lon, start_date, end_date):
    """
    Obtiene datos climáticos históricos desde Meteostat para un rango de fechas.
    """
    location = Point(lat, lon)  # Define la ubicación
    data = Daily(location, start_date, end_date).fetch()

    # Verificar que las columnas necesarias estén presentes
    required_columns = ['tavg', 'tmin', 'tmax', 'prcp', 'wspd', 'pres']
    for col in required_columns:
        if col not in data.columns:
            data[col] = 0  # Rellenar con un valor por defecto (puedes ajustar según corresponda)

    return data

def save_dataset(data, city):
    """
    Guarda los datos climáticos históricos en un archivo CSV.
    """
    os.makedirs("datasets", exist_ok=True)
    output_file = f"datasets/{city}_historical_weather.csv"
    data.to_csv(output_file)
    print(f"Datos históricos guardados en {output_file}")

if __name__ == "__main__":
    # Solicitar al usuario la ciudad y el rango de fechas
    city = input("Introduce el nombre de la ciudad: ")
    start_date = datetime.strptime(input("Introduce la fecha de inicio (YYYY-MM-DD): "), "%Y-%m-%d")
    end_date = datetime.strptime(input("Introduce la fecha de fin (YYYY-MM-DD): "), "%Y-%m-%d")

    # Obtener coordenadas de la ciudad
    lat, lon = get_coordinates(city)
    if lat is not None and lon is not None:
        print(f"Coordenadas de {city}: lat={lat}, lon={lon}")
        # Obtener datos históricos desde Meteostat
        data = fetch_historical_weather(lat, lon, start_date, end_date)
        print(data.head())  # Mostrar una vista previa de los datos
        # Guardar datos en un archivo CSV
        save_dataset(data, city)
    else:
        print("No se pudo obtener las coordenadas. Verifica el nombre de la ciudad.")
