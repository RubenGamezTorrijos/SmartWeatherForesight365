import streamlit as st
import plotly.graph_objects as go

def create_wind_chart(prediction_data):
    st.markdown('<div id="viento">', unsafe_allow_html=True)
    fig_wind = go.Figure()
    fig_wind.add_trace(
        go.Scatter(
            x=prediction_data['Fecha'],
            y=prediction_data['Velocidad del Viento (km/h)'],
            name="Velocidad del Viento",
            line=dict(color='rgb(70, 140, 255)', width=2)
        )
    )
    fig_wind.update_layout(
        title="Velocidad del Viento",
        xaxis_title="Fecha",
        yaxis_title="Velocidad (km/h)",
        hovermode='x unified'
    )
    st.plotly_chart(fig_wind)
    st.markdown('</div>', unsafe_allow_html=True)

