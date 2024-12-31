import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
import numpy as np

def create_climate_chart():
    st.markdown("---")
    st.subheader("Clima")

    # Crear datos mensuales para el año actual y años anteriores
    current_year = datetime.now().year
    years = list(range(current_year - 5, current_year + 1))
    months = ['ENE', 'FEB', 'MAR', 'ABR', 'MAY', 'JUN', 'JUL', 'AGO', 'SEP', 'OCT', 'NOV', 'DIC']

    # Selector para el tipo de datos y año
    col1, col2 = st.columns(2)
    with col1:
        selected_metric = st.selectbox(
            'Seleccione el tipo de datos:',
            ['Temperatura', 'Precipitación Total', 'Velocidad Viento', 'Presión Aire', 'Duración Sol'],
            key='climate_metric'
        )
    with col2:
        selected_year = st.selectbox(
            'Seleccione el año:',
            years,
            key='climate_year'
        )

    # Generar datos simulados para cada año
    metric_options = {
        'Temperatura': {
            'data': {year: {
                'min': [round(x + np.random.uniform(-2, 2)) for x in [6, 7, 9, 10, 13, 15, 17, 17, 15, 13, 9, 7]],
                'max': [round(x + np.random.uniform(-2, 2)) for x in [12, 13, 15, 17, 20, 23, 25, 25, 22, 18, 14, 12]],
                'avg': [round(x + np.random.uniform(-1, 1), 1) for x in [9, 10, 12, 13.5, 16.5, 19, 21, 21, 18.5, 15.5, 11.5, 9.5]]
            } for year in years},
            'ylabel': 'Temperatura (°C)'
        },
        'Precipitación Total': {
            'data': {year: {'value': [round(x + np.random.uniform(-10, 10)) for x in [45, 35, 40, 50, 45, 30, 20, 25, 35, 50, 55, 50]]}
                     for year in years},
            'ylabel': 'Precipitación (mm)'
        },
        'Velocidad Viento': {
            'data': {year: {'value': [round(x + np.random.uniform(-2, 2)) for x in [15, 14, 16, 13, 12, 11, 10, 11, 12, 14, 15, 16]]}
                     for year in years},
            'ylabel': 'Velocidad (km/h)'
        },
        'Presión Aire': {
            'data': {year: {'value': [round(x + np.random.uniform(-2, 2)) for x in [1013, 1014, 1012, 1011, 1010, 1009, 1008, 1009, 1011, 1012, 1013, 1014]]}
                     for year in years},
            'ylabel': 'Presión (hPa)'
        },
        'Duración Sol': {
            'data': {year: {'value': [round(x + np.random.uniform(-1, 1)) for x in [4, 5, 6, 7, 8, 9, 10, 9, 8, 6, 5, 4]]}
                     for year in years},
            'ylabel': 'Horas de Sol'
        }
    }

    fig_climate = go.Figure()

    if selected_metric == 'Temperatura':
        # Añadir barras para temperaturas min y max
        fig_climate.add_trace(
            go.Bar(
                x=months,
                y=metric_options[selected_metric]['data'][selected_year]['min'],
                name='Temperatura Mínima',
                marker_color='rgb(55, 136, 216)'
            )
        )
        fig_climate.add_trace(
            go.Bar(
                x=months,
                y=metric_options[selected_metric]['data'][selected_year]['max'],
                name='Temperatura Máxima',
                marker_color='rgb(255, 132, 132)'
            )
        )
        # Añadir línea para temperatura media
        fig_climate.add_trace(
            go.Scatter(
                x=months,
                y=metric_options[selected_metric]['data'][selected_year]['avg'],
                name='Temperatura Media',
                line=dict(color='rgb(10, 150, 0)', width=2)
            )
        )
    else:
        fig_climate.add_trace(
            go.Bar(
                x=months,
                y=metric_options[selected_metric]['data'][selected_year]['value'],
                name=selected_metric,
                marker_color='rgb(55, 136, 216)'
            )
        )

    fig_climate.update_layout(
        title=f"{selected_metric} - {selected_year}",
        xaxis_title="Mes",
        yaxis_title=metric_options[selected_metric]['ylabel'],
        hovermode='x unified',
        showlegend=True,
        height=500
    )

    # Añadir grid
    fig_climate.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey')
    fig_climate.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey')

    st.plotly_chart(fig_climate, use_container_width=True)

