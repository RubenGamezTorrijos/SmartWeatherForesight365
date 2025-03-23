# 🌤️ **Smart Weather Foresight 365: Previsión Climatológica Inteligente**

Plataforma de análisis y monitorización de datos climatológicos para predecir condiciones atmosféricas basado en datos históricos.

![SmartWeatherForesight365_Prevision_Valencia_10ENE2025_Captura_2_Resumen_Prediccion_4-Widget_2024-12-31-12_29_59](https://github.com/user-attachments/assets/c86fad05-dc0d-40cf-bc9b-9bdc72a120cc)

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


> [!NOTE]
> **Versión actual:** 1.0.8
> **Plataforma:** Python v3.8.0^  
> **Compatibilidad:** Windows, macOS, Linux
> **Navegadores:** Chrome, Brave, Firefox y Edge  


> [!WARNING]
> Actualmente este proyecto ha pasado a realizarse individualmente.

---

## 📋 Indíce
- [🌤️ **Smart Wather Foresight 365: Previsión Climatológica Inteligente**](#️-smart-wather-foresight-365-previsión-climatológica-inteligente)
  - [📋 **Indíce**](#-indíce)
  - [🌟 **Características**](#-características)
  - [🖼️**Capturas de pantalla**](#-capturas-de-pantalla)
  - [📂 **Arquitectura**](#-arquitectura)
  - [🚀 **Guía de uso**](#-guía-de-uso)
    - [🔍 **Instalación**](#-instalación)
    - [🕷️ **Flujo de trabajo de la Aplicación**](#️-flujo-de-trabajo-de-la-aplicación)
    - [🛠️ **Tecnologías utilizadas**](#️-tecnologías-utilizadas)
  - [🤝 **Contribuciones**](#-contribuciones)    
  - [🤖 **Próximas mejoras**](#-próximas-mejoras)
  - [✨ **Créditos**](#-créditos)
  - [📝 **Licencia**](#-licencia)

---

## 🌟 **Características**

- ✅ **API Meteostat**: Encargado de obtener datos históricos de clima de diversas ciudades.
- ✅ **Procesamiento de datos**: Limpieza y preparación de datos CSV obtenidos para un análisis óptimo.
- ✅ **Modelo de predicción**: Utilización de Random Forest para generar predicciones climáticas precisas.
- ✅ **Visualización de datos**: Proceso de mostrar gráficamente los datos de un modo más sencillo con Streamlit y Plotly.
- ✅ **Diseño modular**: Cada componente se desarrolla de forma independiente para facilitar la reutilización y mejora.
- ✅ **Exportación de resultados**: Capacidad de exportar predicciones en formato Excel para análisis externos.

---

## 🖼️ Capturas de pantalla

| Captura Formulario | Captura Resumen Predicción |
|---------------------------|--------------------|
|![SmartWeatherForesight365_Prevision_Valencia_10ENE2025_Captura_1_Formulario](https://github.com/user-attachments/assets/0fa2e604-a1fc-4449-931f-e91590cab4bf)|![SmartWeatherForesight365_Prevision_Valencia_10ENE2025_Captura_2_Resumen_Prediccion_4-Widget_2024-12-31-12_29_59](https://github.com/user-attachments/assets/c86fad05-dc0d-40cf-bc9b-9bdc72a120cc)|
| Captura Temperatura | Captura Precipitación |
|![SmartWeatherForesight365_Prevision_Valencia_10ENE2025_Captura_3_Temperatura_2024-12-31-12_29_59](https://github.com/user-attachments/assets/f9d27d40-6252-474b-b25e-eda810d7d6bd)|![SmartWeatherForesight365_Prevision_Valencia_10ENE2025_Captura_4_Precipitacion_2024-12-31-12_29_59](https://github.com/user-attachments/assets/b0e27cc9-cdaa-4cc3-99c8-1b17494a5c8c)|
| Captura Velocidad Viento | Captura Dirección Viento |
|![SmartWeatherForesight365_Prevision_Valencia_10ENE2025_Captura_5_Velocidad_del_Viento_2024-12-31-12_29_59](https://github.com/user-attachments/assets/940e614c-98ae-4d43-83c9-7685feed2312)|![SmartWeatherForesight365_Prevision_Valencia_10ENE2025_Captura_6_Direccion_del_Viento_2024-12-31-12_29_59](https://github.com/user-attachments/assets/ca641d63-4b68-4309-a8d3-b5d5ff758504)|
| Captura Presión Atmosférica | Captura Historial Clima |
|![SmartWeatherForesight365_Prevision_Valencia_10ENE2025_Captura_7_Presion_Atmosferica_2024-12-31-12_29_59](https://github.com/user-attachments/assets/8de040ae-e8a1-4fd7-8d5a-860fcbd13c8a)|![SmartWeatherForesight365_Prevision_Valencia_10ENE2025_Captura_8_Historial_Clima_2024-12-31-12_29_59](https://github.com/user-attachments/assets/8b499185-2c36-4baa-a549-0d9bcd1eb97c)|

| Captura página principal |
|--------------------------|
|![SmartWeatherForesight365_Prevision_Valencia_10ENE2025_Captura_General_Todo_2024-12-31-12_29_59](https://github.com/user-attachments/assets/9242752b-c1d0-4bcd-8b31-c757a73e790a)|
---

## 📂 **Arquitectura**

```plaintext
SmartWeatherForesight365/
├── .streamlit/                         # Directorio del framework Streamlit Web
│   └── config.toml                     # Configuración de Streamlit
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
stramlit run app.py
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
**¿Quieres colaborar? ¡Eres bienvenido! Sigue estos pasos:**

🔹1. Configura tu entorno
- Crea una cuenta en GitHub.
- Instala Git en tu computadora.
- Configura tu nombre de usuario y correo electrónico en Git:
```bash
git config --global user.name "TuNombre"
git config --global user.email "TuCorreo@example.com"
```
🔹2. Clona el repositorio en tu máquina local:
```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
```
🔹3. Crea un branch(rama) para tu funcionalidad:
```bash
git checkout -b mi-rama
```
🔹4. Haz un commit con tus cambios:
```bash
git commit -m "Añadir mi funcionalidad"
```
🔹5. Sube tus cambios:
```bash
git push origin mi-rama.
```
🔹6. Abre un pull request en este repositorio:

- Ve al repositorio en GitHub.
- Verás un mensaje en la parte superior que dice algo como:
- "Recently pushed branches:" seguido del nombre de tu rama.
- Haz clic en "Compare & pull request".
- Completa los detalles del PR (título, descripción, etc.).
- Haz clic en "Create pull request".

🔹7. Usar la URL para un atajo.
Si prefieres, puedes generar un enlace directo para abrir un PR. La estructura de la URL es:
```bash
https://github.com/usuario/repositorio/compare/main...nombre-de-la-rama
```
- Reemplaza usuario, repositorio, y nombre-de-la-rama con los valores correspondientes.

🔹8. Si trabajas en equipos grandes y usas herramientas como GitHub CLI, puedes usar este comando para crear un PR directamente desde la terminal:
```
gh pr create --base main --title "Título del PR" --body "Descripción del PR"

```

> [!WARNING]
> ⚠️ Esto requiere que tengas instalada y configurada la CLI de GitHub (gh).


---

## 🤖 Próximas mejoras
- Agregar una menú adicional para que el usuario pueda realizar ajustes.
- En los ajutes que el usuario pueda elegir la API que quiere usar y facilitar campos a rellena: URL y API KEY
- Elegir que tipo de datos desea entrenar: Temperatura, Humedad, Presión y Velocidad del viento.

---

## ✨ Créditos
Este proyecto no sería posible sin la dedicación de sus integrantes:

- **Rubén Gámez Torrijos 🔍** - Organización, distribución de tareas y desarrollo del proyecto.
Agradecemos también a la Universidad Europea por inspirar este proyecto académico. 🙌

## 📝 Licencia
Este proyecto está bajo la licencia Apache 2.0. Este software está desarrollado para modo pruebas para proyecto Universitario.
Siéntete libre de usarlo, mejorarlo y así poder ver los nuevos cambios que se van implementando.
