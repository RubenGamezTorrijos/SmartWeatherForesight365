import streamlit as st
import pandas as pd

def create_summary(prediction_data):
    st.markdown('<div id="resumen">', unsafe_allow_html=True)
    st.markdown("""
    <h3>Resumen de predicción</h3>
    """, unsafe_allow_html=True)

    # --- Conversión segura a numérico ---
    temp_col = pd.to_numeric(
        prediction_data['Temperatura Media (°C)'].astype(str)
        .str.replace("°C", "")
        .str.replace(",", "."),
        errors='coerce'
    )

    wind_col = pd.to_numeric(
        prediction_data['Velocidad del Viento (km/h)'].astype(str)
        .str.replace("km/h", "")
        .str.replace(",", "."),
        errors='coerce'
    )

    pressure_col = pd.to_numeric(
        prediction_data['Presión Atmosférica (hPa)'].astype(str)
        .str.replace("hPa", "")
        .str.replace(",", "."),
        errors='coerce'
    )

    rain_col = pd.to_numeric(
        prediction_data['Precipitación (mm)'].astype(str)
        .replace("N/A", "0")
        .str.replace("mm", "")
        .str.replace(",", "."),
        errors='coerce'
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Temperatura Media",
            f"{temp_col.mean():.1f}°C" if temp_col.notna().any() else "N/A",
            f"{temp_col.std():.1f}°C" if temp_col.notna().any() else "N/A"
        )

    with col2:
        try:
            st.metric(
                "Precipitación Total",
                f"{rain_col.sum():.1f}mm" if rain_col.notna().any() else "N/A",
                f"{rain_col.mean():.1f}mm/día" if rain_col.notna().any() else "N/A"
            )
        except:
            st.metric("Precipitación Total", "N/A", "N/A")

    with col3:
        st.metric(
            "Velocidad del Viento",
            f"{wind_col.mean():.1f}km/h" if wind_col.notna().any() else "N/A",
            f"{wind_col.std():.1f}km/h" if wind_col.notna().any() else "N/A"
        )

    with col4:
        st.metric(
            "Presión del Aire",
            f"{pressure_col.mean():.1f}hPa" if pressure_col.notna().any() else "N/A",
            f"{pressure_col.std():.1f}hPa" if pressure_col.notna().any() else "N/A"
        )

    st.markdown('</div>', unsafe_allow_html=True)

