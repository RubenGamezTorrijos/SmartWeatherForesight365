# 🌤️ **Smart Wather Foresight 365: Previsión Climatológica Inteligente**

Plataforma de análisis y monitorización de datos climatológicos para predecir condiciones atmosféricas basado en datos históricos.

¡Bienvenido al proyecto **SmartWeatherForesight365**! 🎯 Este proyecto de Computación 1 implementa un sistema de predicción inteligente para predecir el clima en fechas posteriores hasta un máximo de 30 días, obteniendo datos históricos de **meteostat.net** conectado mediante API y con modelos de aprendizaje y entrenamiento en **Python** usando librerías.

![Status](https://img.shields.io/badge/Estado-Produccion-green?style=flat-square)
![GitHub license](https://img.shields.io/github/license/RubenGamezTorrijos/SmartWeatherForesight365?style=flat-square)
![GitHub version](https://img.shields.io/github/v/tag/RubenGamezTorrijos/SmartWeatherForesight365?label=versión&style=flat-square)
![GitHub repo size](https://img.shields.io/github/repo-size/RubenGamezTorrijos/SmartWeatherForesight365?style=flat-square)
![GitHub Repo stars](https://img.shields.io/github/stars/RubenGamezTorrijos/SmartWeatherForesight365?style=social)

![GitHub issues](https://img.shields.io/github/issues/RubenGamezTorrijos/SmartWeatherForesight365?style=flat-square)
![GitHub forks](https://img.shields.io/github/forks/RubenGamezTorrijos/SmartWeatherForesight365?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/RubenGamezTorrijos/SmartWeatherForesight365?style=flat-square)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/RubenGamezTorrijos/SmartWeatherForesight365/main.yml?style=flat-square)


> **Versión actual:** 1.0.7  
> **Plataforma:** Python v3.8.0^  
> **Compatibilidad:** Windows, macOS, Linux

---

## 📋 Indíce
- [🌤️ **Smart Wather Foresight 365: Previsión Climatológica Inteligente**](#️-smart-wather-foresight-365-previsión-climatológica-inteligente)
  - [📋 Indíce](#-indíce)
  - [🌟 **Características**](#-características)
  - [📂 **Estructura**](#-estructura)
  - [🚀 **Guía de Uso**](#-guía-de-uso)
    - [🔍 Instalación](#-instalación)
    - [🕷️ Flujo de trabajo de la Aplicación](#️-flujo-de-trabajo-de-la-aplicación)
      - [🛠️ Tecnologías utilizadas](#️-tecnologías-utilizadas)
  - [🤝 Contribuciones](#-contribuciones)
    - [¿Quieres colaborar? ¡Eres bienvenido! Sigue estos pasos:](#quieres-colaborar-eres-bienvenido-sigue-estos-pasos)
  - [🤖 Próximas Mejoras](#-próximas-mejoras)
  - [✨ Créditos](#-créditos)

---

## 🌟 **Características**

- ✅ **API Meteostat**: Encargado de obtener datos históricos de clima de diversas ciudades.
- ✅ **Procesamiento de datos**: Limpieza y preparación de datos CSV obtenidos para un análisis óptimo.
- ✅ **Modelo de predicción**: Utilización de Random Forest para generar predicciones climáticas precisas.
- ✅ **Visualización de datos**: Proceso de mostrar gráficamente los datos de un modo más sencillo con Streamlit y Plotly.
- ✅ **Diseño modular**: Cada componente se desarrolla de forma independiente para facilitar la reutilización y mejora.
- ✅ **Exportación de resultados**: Capacidad de exportar predicciones en formato Excel para análisis externos.

---

## 📂 **Estructura**

```plaintext
SmartWeatherForesight365/
├── datasets/                           # Almacenamiento datos históricos obtenidos de Meteostat en CSV
│   └── [Ciudad]_Historial_Weather.csv       
├── ml/                                 # Modelos guardados de entrenamiento para su uso posterior
│   ├── [Ciudad]_[Parametro]_Model.pkl
│   └── [Ciudad]_[Parametro]_Scaler.pkl
├── predictions/                        # Exportado datos predictivos en formato Excel
│   └── [Ciudad]_Future_Predictions.xlsx
├── app/
│   ├── controllers/
│   │   ├── api_controller.py           # Controlador para la conexión con la API de Meteostat
│   │   ├── data_controller.py          # Controlador para el procesamiento de datos
│   │   └── model_controller.py         # Controlador para la gestión de modelos de predicción
│   ├── models/
│   │   ├── dataset_model.py
│   │   ├── prediction_model.py         # Modelo para generar predicciones
│   │   └── training_model.py           # Modelo para entrenar con datos históricos
│   └── views/
│       ├── components/                 # Componentes de la interfaz de usuario
│       │   ├── __init__.py             # Integración de los componentes
│       │   ├── climate_chart.py        # Componente: Gráfica Clima histórico (temperatura, presión, etc...) historial años anteriores
│       │   ├── precipitation_chart.py  # Componente: Gráfica previsión de precipitación
│       │   ├── pressure_chart.py       # Componente: Gráfica previsión de presión atmosférica
│       │   ├── summary.py              # Componente: Gráfica previsión resumen en cuatro columnas: Temperatura, Presión, Humedad y Precipitación
│       │   ├── temperature_chart.py    # Componente: Gráfica previsión de temperatura (Máxima, Baja y Media)
│       │   ├── wind_chart.py           # Componente: Gráfica previsión de velocidad del viento
│       │   └── wind_rose.py            # Componente: Gráfica previsión dirección del viento
│       ├── utils/
│       │   └── data_processing.py      # Utilidades para el procesamiento de datos
│       └── home.py                     # Vista principal de la aplicación
├── app.py                              # Ejecución principal de la aplicación de la aplicación Streamlit
├── config.py                           # Configuraciones globales de la aplicación
├── requirements.txt                    # Dependencias del proyecto
└── README.md                           # Este archivo se encuentra la guía preincipal LEEME
```
---

## 🚀 **Guía de Uso**
### 🔍 Instalación
🔹1. Clona este repositorio:
```
git clone https://github.com/RubenGamezTorrijos/SmartWeatherForesight365.git
cd SmartWeatherForesight365
```

🔹2. Instala las dependencias:
```
pip install -r requirements.txt
```

🔹3. Ejecutar aplicación desde la ruta del paquete:

`C:/ruta/SmartWeatherSingith/>`
```
Stramlit run app.py
```

---

### 🕷️ Flujo de trabajo de la Aplicación

1. El usuario inicia la aplicación ejecutando `streamlit run app.py`.
2. La aplicación carga la interfaz de usuario principal.
3. El usuario selecciona una ciudad y un rango de fechas para la predicción.
4. La aplicación obtiene datos históricos de la API de Meteostat si no están disponibles localmente.
5. Los datos se procesan y limpian.
6. Se entrenan modelos de predicción si no existen para la ciudad seleccionada.
7. Se generan predicciones para el rango de fechas especificado.
8. Los resultados se visualizan en varios gráficos y resúmenes.
9. El usuario puede descargar las predicciones en formato Excel (*.xlsx).

---

#### 🛠️ Tecnologías utilizadas

- Python 3.8+
- Numpy para cálculos numéricos y manejo de matrices.
- Scikit-learn para algoritmos de machine learning.
- Flask para crear aplicaciones web y APIs.
- Joblib para guardar y cargar modelos de machine learning.
- Requests para realizar solicitudes HTTP.
- BeautifulSoup para scraping de datos web.
- Kaggle para acceder a datasets y competiciones.
- Streamlit para crear interfaces interactivas.
- Matplotlib para visualización de datos estáticos.
- Pandas para manipulación y análisis de datos.
- Plotly para visualizaciones interactivas.
- Openpyxl para leer y escribir archivos Excel.
- Python-dateutil para manejo avanzado de fechas y horas.

---

## 🤝 Contribuciones
### ¿Quieres colaborar? ¡Eres bienvenido! Sigue estos pasos:

🔹1. Haz un fork de este repositorio.
🔹2. Crea un branch para tu funcionalidad:
```
git checkout -b mi-funcionalidad
```
🔹3. Haz un commit con tus cambios:
```
git commit -m "Añadir mi funcionalidad"
```
🔹4. Sube tus cambios:
```
git push origin mi-funcionalidad.
```
🔹5. Abre un pull request en este repositorio.

---

## 🤖 Próximas Mejoras
- Agregar una menú adicional para que el usuario pueda realizar ajustes.
- En los ajutes que el usuario pueda elegir la API que quiere usar y facilitar campos a rellena: URL y API KEY
- Elegir que tipo de datos desea entrenar: Temperatura, Humedad, Presión y Velocidad del viento.

---

## ✨ Créditos
Este proyecto no sería posible sin la dedicación de sus integrantes:

- **Rubén Gámez Torrijos 🔍** - Organización, distribución de tareas y desarrollo del proyecto.
Agradecemos también a la Universidad Europea por inspirar este proyecto académico. 🙌