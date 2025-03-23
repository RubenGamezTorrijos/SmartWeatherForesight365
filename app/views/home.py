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
    # Configuración inicial de la página
    st.set_page_config(
        page_title="Smart Weather Foresight 365",
        page_icon="🌤️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.title("Smart Weather Foresight 365 🌤️") 
    st.markdown('<div id="resumen">', unsafe_allow_html=True)
    city_name = prediction_data['Ciudad'].iloc[0]
    st.markdown(f"""
    <h3>Resumen de predicción: 
        <span style="background-color: #FFA500; color: #000000; padding: 0.2em 0.5em; border-radius: 0.3em;">
            {city_name}
        </span>
    </h3>
    """, unsafe_allow_html=True)
    st.subheader("Predicción meteorológica basada en entrenamiento de datos históricos")

    if 'show_results' not in st.session_state:
        st.session_state.show_results = False

    # Mover el formulario al sidebar
    with st.sidebar:
        st.title("Menú")
        
        # Formulario
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
        
        # Botón para obtener predicción
        submit_button = st.button("Obtener predicción")
        
        # Botones adicionales
        download_button = st.button("Generar Excel")
        new_search_button = st.button("Nueva búsqueda")

    # Lógica del botón "Obtener predicción"
    if submit_button:
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

    # Mostrar resultados si están disponibles
    if st.session_state.show_results:
        prediction_data = st.session_state.prediction_data
        city = st.session_state.city

        # Crear pestañas para organizar el contenido
        tab_sumary, tab_temperature, tab_precipitation, tab_wind_speed, tab_wind_direction, tab_atmospheric_pressure, tab_climate_history = st.tabs(
            ["Resumen", "Temperatura", "Precipitación", "Velocidad del Viento", "Dirección del Viento", "Presión Atmosférica", "Historial"]
        )

        with tab_sumary:
            create_summary(prediction_data)

        with tab_temperature:
            create_temperature_chart(prediction_data)

        with tab_precipitation:
            create_precipitation_chart(prediction_data)

        with tab_wind_speed:
            create_wind_chart(prediction_data)

        with tab_wind_direction:
            create_wind_rose(prediction_data)

        with tab_atmospheric_pressure:
            create_pressure_chart(prediction_data)

        with tab_climate_history:
            create_climate_chart()

        # Botón para descargar predicciones (movido al sidebar)
        if download_button:
            excel_file = process_prediction_data(prediction_data, city)
            if excel_file:
                st.sidebar.download_button(
                    label="Descargar predicción en Excel",
                    data=excel_file,
                    file_name=f"{city}_prediccion.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            else:
                st.sidebar.warning("No se pudo generar el archivo Excel.")

        # Botón para nueva búsqueda (movido al sidebar)
        if new_search_button:
            st.session_state.prediction_data = None
            st.session_state.show_results = False
            st.session_state.city = None
            st.rerun()