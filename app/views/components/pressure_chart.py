import streamlit as st
import plotly.graph_objects as go

def create_pressure_chart(prediction_data):
    st.markdown('<div id="presion">', unsafe_allow_html=True)
    fig_pres = go.Figure()
    fig_pres.add_trace(
        go.Scatter(
            x=prediction_data['Fecha'],
            y=prediction_data['Presión Atmosférica (hPa)'],
            name="Presión Atmosférica",
            line=dict(color="green", width=2)
        )
    )
    fig_pres.update_layout(
        title="Presión Atmosférica",
        xaxis_title="Fecha",
        yaxis_title="Presión (hPa)",
        hovermode='x unified'
    )
    st.plotly_chart(fig_pres)
    st.markdown('</div>', unsafe_allow_html=True)

