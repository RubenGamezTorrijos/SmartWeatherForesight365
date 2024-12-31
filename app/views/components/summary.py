import streamlit as st

def create_summary(prediction_data):
    st.markdown('<div id="resumen">', unsafe_allow_html=True)
    city_name = prediction_data['Ciudad'].iloc[0]
    st.markdown(f"""
    <h3>Resumen de predicción: 
        <span style="background-color: #FFA500; color: #000000; padding: 0.2em 0.5em; border-radius: 0.3em;">
            {city_name}
        </span>
    </h3>
    """, unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(
            "Temperatura Media",
            f"{prediction_data['Temperatura Media (°C)'].mean():.1f}°C",
            f"{prediction_data['Temperatura Media (°C)'].std():.1f}°C"
        )
    with col2:
        try:
            precip_sum = prediction_data['Precipitación (mm)'].replace('N/A', '0').astype(float).sum()
            precip_mean = prediction_data['Precipitación (mm)'].replace('N/A', '0').astype(float).mean()
            st.metric(
                "Precipitación Total",
                f"{precip_sum:.1f}mm",
                f"{precip_mean:.1f}mm/día"
            )
        except Exception as e:
            st.metric(
                "Precipitación Total",
                "N/A",
                "N/A"
            )
    with col3:
        st.metric(
            "Velocidad del Viento",
            f"{prediction_data['Velocidad del Viento (km/h)'].mean():.1f}km/h",
            f"{prediction_data['Velocidad del Viento (km/h)'].std():.1f}km/h"
        )
    with col4:
        st.metric(
            "Presión del Aire",
            f"{prediction_data['Presión Atmosférica (hPa)'].mean():.1f}hPa",
            f"{prediction_data['Presión Atmosférica (hPa)'].std():.1f}hPa"
        )
    st.markdown('</div>', unsafe_allow_html=True)

