# 🌤️ **Smart Wather Foresight 365: Previsión Climatológica Inteligente**

Plataforma de análisis y monitorización de datos climatológicos para predecir condiciones atmosféricas basado en datos históricos.

¡Bienvenido al proyecto **WeatherInsight**! 🎯 Este proyecto de computación 1 implementa un sistema de predicción inteligente para conocer la clima en días posteriores según necesidades, con modelos de aprendizaje y entrenamiento en **Python** y usando librerías.

![Status](https://img.shields.io/badge/Estado-Produccion-yellow?style=flat-square)
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
    - [1. Instalación](#1-instalación)
    - [2. Ejecución de los Módulos](#2-ejecución-de-los-módulos)
      - [🕷️ Obtener datos URL y guardarlos en CSV](#️-obtener-datos-url-y-guardarlos-en-csv)
      - [📇 Modelo entranmiento](#-modelo-entranmiento)
      - [🔍 Predictions](#-predictions)
      - [🛠️ Desarrollo](#️-desarrollo)
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
├── app.py                              # Ejecución principal de la aplicación de la aplicación Streamlit ``Streamlit run app.py``
├── config.py                           # Configuraciones globales de la aplicación
├── requirements.txt                    # Dependencias del proyecto
└── README.md                           # Este archivo se encuentra la guía preincipal LEEME
```
---

## 🚀 **Guía de Uso**
### 1. Instalación
🔹1. Clona este repositorio:
```
git clone https://github.com/RubenGamezTorrijos/SmartWeatherForesight365.git
cd SmartWeatherForesight365
```

🔹2. Instala las dependencias:
```
pip install -r requirements.txt
```

### 2. Ejecución de los Módulos
#### 🕷️ Obtener datos URL y guardarlos en CSV
Obtiene los datos relacionados de la URL y los guarda en datasets en formato CSV:
```
python generate_datasets.py
```
**Parámetros:**

- ``datasets``: Carpeta destino para los archivos CSV.

---

#### 📇 Modelo entranmiento
Aprende de los datos históricos obtenidos según los que le hayamos indicado en rango de fechas, mayor rango mayor entrenamiento:

```
python train_model.py
```
**Parámetros:**

- ``--models``: Directorio donde se procesará el modelo de entrenamiento.

---

#### 🔍 Predictions
En este módulo se encargará de realizar la predicción basándose en los modelos generados en el directorio **models** por nombre de ciudad:
```
python predict_weather.py"
```
**Parámetros:**
- ``--predictions``: Guardado datos exportados en formato XLSX para poder visualizarlos en local.

---

#### 🛠️ Desarrollo
**Scripts Útiles**
- Formatear Código:
```
bash dev-tools/format.sh
```
- Análisis Estático:
```
bash dev-tools/lint.sh
```
**Requisitos de Desarrollo**
Instala las dependencias adicionales para desarrollo:
```
pip install -r dev-requirements.txt
```

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
- Posibilidad de agregar gráficas según el tipo de análisis.

---

## ✨ Créditos
Este proyecto no sería posible sin la dedicación de sus integrantes:

- **Rubén Gámez Torrijos 🔍** - Organización, distribución de tareas y desarrollo del proyecto.
Agradecemos también a la Universidad Europea por inspirar este proyecto académico. 🙌
