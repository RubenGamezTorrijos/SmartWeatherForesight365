import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def create_wind_rose(prediction_data):
    st.markdown('<div id="direccion-viento">', unsafe_allow_html=True)

    # --------- Limpieza y normalización de datos ---------

    # Dirección del viento → numérica segura
    wind_dir = pd.to_numeric(
        prediction_data['Dirección del Viento (°)']
        .astype(str)
        .str.replace("°", "")
        .str.replace(",", "."),
        errors='coerce'
    )

    # Velocidad del viento → numérica segura
    wind_speed = pd.to_numeric(
        prediction_data['Velocidad del Viento (km/h)']
        .astype(str)
        .str.replace("km/h", "")
        .str.replace(",", "."),
        errors='coerce'
    )

    # Crear DataFrame limpio
    clean_df = pd.DataFrame({
        "dir": wind_dir,
        "speed": wind_speed
    }).dropna()

    if clean_df.empty:
        st.warning("No hay datos válidos de viento para generar la rosa.")
        st.markdown('</div>', unsafe_allow_html=True)
        return

    # --------- Crear categorías de viento ---------

    directions_labels = [
        'N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 
        'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW'
    ]

    bins = np.linspace(0, 360, len(directions_labels) + 1)

    # Crear bins de forma segura
    dir_bins = pd.cut(
        clean_df['dir'],
        bins=bins,
        labels=directions_labels,
        include_lowest=True
    )

    # --------- Calcular estadísticas ---------

    wind_stats = pd.DataFrame({
        'direction': dir_bins,
        'speed': clean_df['speed']
    }).groupby('direction', observed=True).agg(
        frequency=('speed', 'count'),
        speed=('speed', 'mean')
    ).reset_index()

    total = len(clean_df)
    wind_stats['frequency'] = (wind_stats['frequency'] / total) * 100

    # Rellenar direcciones vacías con 0
    wind_stats = wind_stats.set_index('direction').reindex(directions_labels).fillna(0).reset_index()

    # Cerrar el polígono
    directions = list(wind_stats['direction']) + [wind_stats['direction'].iloc[0]]
    frequencies = list(wind_stats['frequency']) + [wind_stats['frequency'].iloc[0]]

    # --------- Crear gráfica ---------

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=frequencies,
        theta=directions,
        fill='toself',
        fillcolor='rgba(55, 136, 216, 0.5)',
        line=dict(color='rgb(0, 70, 255)', width=2),
        name='Dirección del Viento'
    ))

    fig.update_layout(
        title="Dirección del Viento",
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max(frequencies) * 1.2 if max(frequencies) > 0 else 1],
                ticksuffix='%',
                showline=False,
                gridcolor='lightgrey',
            ),
            angularaxis=dict(
                direction="clockwise",
                period=16,
                gridcolor='lightgrey',
            ),
            bgcolor='rgba(0,0,0,0)'
        ),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)'
    )

    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

