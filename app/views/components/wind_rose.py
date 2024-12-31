import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def create_wind_rose(prediction_data):
    st.markdown('<div id="direccion-viento">', unsafe_allow_html=True)
    
    # Convertir direcciones a categorías de viento
    directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 
                  'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    bins = np.linspace(0, 360, len(directions) + 1)
    
    # Crear bins para las direcciones
    dir_bins = pd.cut(prediction_data['Dirección del Viento (°)'], 
                     bins=bins, 
                     labels=directions, 
                     include_lowest=True)
    
    # Calcular la frecuencia y velocidad media para cada dirección
    wind_stats = pd.DataFrame({
        'direction': dir_bins,
        'speed': prediction_data['Velocidad del Viento (km/h)']
    }).groupby('direction').agg({
        'speed': ['count', 'mean']
    }).reset_index()
    
    wind_stats.columns = ['direction', 'frequency', 'speed']
    wind_stats['frequency'] = wind_stats['frequency'] / len(prediction_data) * 100
    
    # Añadir el primer punto al final para cerrar el polígono
    directions = list(wind_stats['direction']) + [wind_stats['direction'].iloc[0]]
    frequencies = list(wind_stats['frequency']) + [wind_stats['frequency'].iloc[0]]
    
    fig = go.Figure()
    
    # Añadir el área rellena
    fig.add_trace(go.Scatterpolar(
        r=frequencies,
        theta=directions,
        fill='toself',
        fillcolor='rgba(55, 136, 216, 0.5)',
        line=dict(color='rgb(0, 70, 255)', width=2),
        name='Dirección del Viento'
    ))
    
    # Configurar el layout
    fig.update_layout(
        title="Dirección del Viento",
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max(frequencies) * 1.2],
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
    
    st.plotly_chart(fig)
    st.markdown('</div>', unsafe_allow_html=True)

