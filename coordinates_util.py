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
    headers = {"User-Agent": "WeatherSmartApp/1.0 (your_email@example.com)"}
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200 and len(response.json()) > 0:
        data = response.json()[0]
        return float(data["lat"]), float(data["lon"])
    else:
        print(f"Error al obtener coordenadas para la ciudad: {city}.")
        return None, None

def get_station_by_coordinates(lat, lon):
    """
    Busca la estación meteorológica más cercana utilizando coordenadas geográficas.

    Args:
        lat (float): Latitud de la ciudad.
        lon (float): Longitud de la ciudad.

    Returns:
        str: ID de la estación meteorológica más cercana o None si no se encuentra.
    """
    endpoint = "/stations/nearby"
    params = {"lat": lat, "lon": lon, "limit": 1}
    url = f"https://meteostat.p.rapidapi.com{endpoint}"
    headers = {
        "X-RapidAPI-Key": "fe5d411a2cmsh1b597687f803a91p115ad4jsnf2229f917062",
        "X-RapidAPI-Host": "meteostat.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if "data" in data and len(data["data"]) > 0:
            station = data["data"][0]
            print(f"Estación seleccionada: {station['name']} ({station['id']}), País: {station['country']}")
            return station["id"]
        else:
            print(f"No se encontró una estación cercana a las coordenadas: lat={lat}, lon={lon}.")
            return None
    else:
        print(f"Error al conectar con la API de Meteostat: {response.status_code}")
        return None
