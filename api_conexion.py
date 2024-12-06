import requests

# Clave API sitio web "https://rapidapi.com" para Meteostat (Sólo uso para la UEM)
API_KEY = "fe5d411a2cmsh1b597687f803a91p115ad4jsnf2229f917062"

BASE_URL = "https://meteostat.p.rapidapi.com"

HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "meteostat.p.rapidapi.com"
}

def get_request(endpoint, params=None):
    """
    Realiza una solicitud GET a la API de Meteostat.
    """
    url = f"{BASE_URL}{endpoint}"
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API de Meteostat: {e}")
        return None

def get_coordinates(city):
    """
    Obtiene las coordenadas (latitud y longitud) de una ciudad utilizando Nominatim (OpenStreetMap).

    Args:
        city (str): Nombre de la ciudad.

    Returns:
        tuple: (lat, lon) como flotantes, o (None, None) si falla.
    """
    url = f"https://nominatim.openstreetmap.org/search"
    params = {"q": city, "format": "json", "limit": 1}
    headers = {"User-Agent": "WeatherSmartApp/1.0 (tu-correoelctronico@ejemplo.com)"}
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200 and len(response.json()) > 0:
        data = response.json()[0]
        return float(data["lat"]), float(data["lon"])
    else:
        print(f"Error al obtener coordenadas para la ciudad: {city}.")
        return None, None
