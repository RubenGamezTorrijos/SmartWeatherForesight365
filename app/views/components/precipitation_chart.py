import streamlit as st
import plotly.graph_objects as go

def create_precipitation_chart(prediction_data):
    st.markdown('<div id="precipitacion">', unsafe_allow_html=True)
    fig_prcp = go.Figure()
    fig_prcp.add_trace(
        go.Bar(
            x=prediction_data['Fecha'],
            y=prediction_data['Precipitación (mm)'],
            name="Precipitación",
            marker_color='blue'
        )
    )
    fig_prcp.update_layout(
        title="Precipitación",
        xaxis_title="Fecha",
        yaxis_title="Precipitación (mm)",
        hovermode='x unified'
    )
    st.plotly_chart(fig_prcp)
    st.markdown('</div>', unsafe_allow_html=True)

