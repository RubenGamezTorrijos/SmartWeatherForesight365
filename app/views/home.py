import streamlit as st
from datetime import datetime, timedelta
import logging
from .components import (
    create_summary,
    create_temperature_chart,
    create_precipitation_chart,
    create_wind_chart,
    create_wind_rose,
    create_pressure_chart,
    create_climate_chart
)
from .utils.data_processing import process_prediction_data

def create_home_page(api_controller, data_controller, model_controller, prediction_model):
    st.set_page_config(page_title="Smart Foresight 365", page_icon="🌤️", layout="wide", initial_sidebar_state="expanded")
    
    st.title("Smart Foresight 365 🌤️")
    st.subheader("Predicción meteorológica basada en entrenamiento de datos históricos")

    if 'show_results' not in st.session_state:
        st.session_state.show_results = False

    if not st.session_state.show_results:
        city = st.text_input("Introduce nombre de una ciudad de España:")

        col1, col2 = st.columns(2)
        with col1:
            start_date = st.date_input(
                "Fecha de inicio:",
                min_value=datetime.now().date(),
                value=datetime.now().date()
            )
        with col2:
            end_date = st.date_input(
                "Fecha de fin:",
                min_value=start_date,
                value=start_date + timedelta(days=7),
                max_value=start_date + timedelta(days=30)
            )

        if st.button("Obtener predicción"):
            if city and start_date and end_date:
                try:
                    with st.spinner("Por favor, espere. Obteniendo datos históricos..."):
                        historical_data = api_controller.get_historical_data(
                            city, start_date - timedelta(days=1825), start_date
                        )
                    st.success(f"¡COMPLETADO! Datos históricos obtenidos para {city}")

                    with st.spinner("Limpiando y procesando datos, cargando..."):
                        cleaned_data = data_controller.load_and_clean_data(city)
                    st.success(f"¡COMPLETADO! Datos limpiados y procesados para {city}")

                    with st.spinner("Por favor, espere. Entrenando modelo..."):
                        model_controller.train_model(cleaned_data, city)
                    st.success(f"¡COMPLETADO! Modelo entrenado para {city}")

                    with st.spinner("Por favor, espere. Generando predicción..."):
                        prediction_data = prediction_model.generate_prediction(
                            city, start_date, end_date
                        )
                    st.success("¡Predicción generada correctamente!")

                    st.session_state.prediction_data = prediction_data
                    st.session_state.city = city
                    st.session_state.show_results = True
                    st.rerun()

                except Exception as e:
                    st.error(f"Error al generar la predicción: {str(e)}")
                    logging.exception("Error detallado:")
            else:
                st.warning("Por favor, complete todos los campos requeridos.")

    else:
        
        prediction_data = st.session_state.prediction_data
        city = st.session_state.city

        create_summary(prediction_data)
        create_temperature_chart(prediction_data)
        create_precipitation_chart(prediction_data)
        create_wind_chart(prediction_data)
        create_wind_rose(prediction_data)
        create_pressure_chart(prediction_data)
        create_climate_chart()

        # Botón para descargar predicciones
        col1, col2 = st.columns([4, 1])
        with col1:
            process_prediction_data(prediction_data, city)
        with col2:
            if st.button("Nueva búsqueda"):
                st.session_state.prediction_data = None
                st.session_state.show_results = False
                st.session_state.city = None
                st.rerun()

