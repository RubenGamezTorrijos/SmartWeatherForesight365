import streamlit as st
import plotly.graph_objects as go

def create_temperature_chart(prediction_data):
    st.markdown('<div id="temperatura">', unsafe_allow_html=True)
    fig_temp = go.Figure()
    
    fig_temp.add_trace(
        go.Scatter(
            x=prediction_data['Fecha'],
            y=prediction_data['Temperatura Máxima (°C)'],
            name="Temperatura Máxima",
            line=dict(color="red", width=2)
        )
    )
    
    fig_temp.add_trace(
        go.Scatter(
            x=prediction_data['Fecha'],
            y=prediction_data['Temperatura Mínima (°C)'],
            name="Temperatura Mínima",
            line=dict(color="blue", width=2)
        )
    )
    
    fig_temp.add_trace(
        go.Scatter(
            x=prediction_data['Fecha'],
            y=prediction_data['Temperatura Media (°C)'],
            name="Temperatura Media",
            line=dict(color="black", width=2)
        )
    )
    
    fig_temp.add_trace(
        go.Scatter(
            x=prediction_data['Fecha'],
            y=prediction_data['Punto de Rocío (°C)'],
            name="Punto de Rocío",
            line=dict(color="purple", width=2)
        )
    )
    
    fig_temp.update_layout(
        title="Temperatura",
        xaxis_title="Fecha",
        yaxis_title="Temperatura (°C)",
        hovermode='x unified'
    )
    st.plotly_chart(fig_temp)
    st.markdown('</div>', unsafe_allow_html=True)

