import streamlit as st
from app.views import create_home_page
from app.controllers.api_controller import WeatherAPIController
from app.controllers.data_controller import DataController
from app.controllers.model_controller import ModelController
from app.models.prediction_model import PredictionModel

def main():
    # Inicializar controllers
    api_controller = WeatherAPIController()
    data_controller = DataController()
    model_controller = ModelController()
    
    # Inicializar PredictionModel con model_controller
    prediction_model = PredictionModel(model_controller)
    
    # Crear y mostrar la página de inicio (Home)
    create_home_page(api_controller, data_controller, model_controller, prediction_model)

if __name__ == "__main__":
    main()

