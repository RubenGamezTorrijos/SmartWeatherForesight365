import pickle
import pandas as pd
import streamlit as st
from datetime import datetime

# Cargar el modelo entrenado
with open("best_model.pkl", "rb") as file:
    model = pickle.load(file)

# Título y descripción de la aplicación
st.title("Predicción Climática Interactiva")
st.write("En esta aplicación puedes obtener la predicción de la temperatura, humedad y viento actuales de cualquier ciudad futura basado en datos históricos.")

# Formulario de entrada para la ciudad
city = st.text_input("Introduce la ciudad para la predicción del clima:")

# Si se ha introducido una ciudad, obtener y mostrar los datos
if city:
    # Obtenemos los datos de la API para la ciudad introducida
    dataset_path = f"datasets/{city}_weather.csv"
    
    try:
        df = pd.read_csv(dataset_path)
        st.subheader("Datos Históricos")
        st.write(df.head())  # Mostrar los primeros datos históricos

        # Gráfico de datos históricos
        st.subheader("Gráfico de Temperatura Histórica")
        st.line_chart(df[['datetime', 'temperature']].set_index('datetime'))

        # Selección de fecha futura
        future_date = st.date_input("Selecciona la fecha futura para la predicción:", min_value=datetime.today(), max_value=datetime.today() + timedelta(days=365))
        future_datetime = datetime.combine(future_date, datetime.min.time())
        future_timestamp = future_datetime.timestamp()

        # Entradas del usuario para predicción
        humidity_input = st.number_input("Humedad actual (%):", min_value=0, max_value=100, value=50)
        wind_speed_input = st.number_input("Velocidad del viento actual (m/s):", value=3.0)

        # Botón para hacer la predicción
        if st.button("Ver predicción"):
            # Crear un DataFrame con la entrada del usuario
            input_df = pd.DataFrame([[humidity_input, wind_speed_input]], columns=['humidity', 'wind_speed'])

            # Realizar la predicción
            prediction = model.predict(input_df)

            # Mostrar los resultados
            st.write(f"**Predicción para la próxima fecha: {future_date}**")
            st.write(f"**Temperatura:** {prediction[0]:.2f}°C")
            st.write(f"**Humedad:** {humidity_input}%")
            st.write(f"**Viento:** {wind_speed_input} m/s")

    except FileNotFoundError:
        st.error(f"No se encontraron datos históricos para la ciudad: {city}. Por favor, genera el dataset primero.")

# Botón para limpiar los datos y permitir ingresar una nueva ciudad
if st.button("Nueva búsqueda"):
    city = ""
    st.session_state()  # Reinicia la aplicación