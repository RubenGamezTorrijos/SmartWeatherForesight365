# 🚀 **WeatherInsight: Predicción Inteligente de Climatología** 
Plataforma de Análisis y Monitorización de Datos Climatológicos para Predecir Condiciones Atmosféricas

¡Bienvenido al proyecto **WeatherInsight**! 🎯 Este proyecto de comoputación 1 implementa un sistema de predicción inteligente para conocer la clima en días posteriores según necesidades, con modelos de aprendizaje y entrenamiento en **Python** y usando herramientas cómo: **Pentaho**, **RapidMiner**, y **OpenRifine**.

![Status](https://img.shields.io/badge/Estado-Desarrollo-yellow?style=flat-square)
![GitHub license](https://img.shields.io/github/license/RubenGamezTorrijos/WeatherInsight?style=flat-square)
![GitHub version](https://img.shields.io/github/v/tag/RubenGamezTorrijos/WeatherInsight?label=versión&style=flat-square)
![GitHub repo size](https://img.shields.io/github/repo-size/RubenGamezTorrijos/WeatherInsight?style=flat-square)
![GitHub Repo stars](https://img.shields.io/github/stars/RubenGamezTorrijos/WeatherInsight?style=social)

![GitHub issues](https://img.shields.io/github/issues/RubenGamezTorrijos/WeatherInsight?style=flat-square)
![GitHub forks](https://img.shields.io/github/forks/RubenGamezTorrijos/WeatherInsight?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/RubenGamezTorrijos/WeatherInsight?style=flat-square)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/RubenGamezTorrijos/WeatherInsight/main.yml?style=flat-square)


> **Versión actual:** 1.0.0  
> **Plataforma:** Python v3.8.0^  
> **Compatibilidad:** Windows, macOS, Linux

---

## 📋 Indíce
- [Características](#-características)
- [Estructura](#-estructura)
- [Guía de uso](#-guía-de-uso)
- [Desarrollo](#-desarrollo)
- [Ejemplos de Consultas](#-ejemplos-de-consultas)
- [Contribuciones](#-contribuciones)
- [Próximas Mejoras](#-próximas-mejoras)
- [Créditos](#-créditos)
- [Licencia](#-licencia)

---

## 🌟 **Características**

✅ **Pentaho**: Encargado de obtener datos en CSV de URL y transformar datos.  
✅ **OpenRefine**: Procesar contenido de datos CSV obtenidos para una limpieza óptima.  
✅ **RapidMiner**: Proceso de mostrar gráficamente los datos de un modo más sencillo con módulos por bloques.
✅ **Diseño Modular**: Cada componente se desarrolla de forma independiente para facilitar la reutilización y mejora.  
✅ **Pruebas Unitarias**: Cada módulo incluye ejemplos de uso y pruebas básicas para garantizar su correcto funcionamiento.
✅ **Lenguaje: PYthon**: El lenguaje utilizado para el aprendiaje de librerías se defininarán a continuación...

---

## 📂 **Estructura**

```plaintext
weatherinsight/
├── datasets/                           # Almacenamiento datos históricos obtenidos de Meteostat en CSV
│   ├── Valencia_historial_weather.csv       
│   └── Madrid_historial_weather.csv         
├── models/                             # Modelos guardados de entrenamiento para luego su uso
│   ├── Valencia_weather_model.pkl      # generado automáticamente por ""rain_model.py""
│   └── Madrid_weather_model.pkl        
├── predictions/                        # Exportado datos predictivos en formato xls para mostrar
│   ├── Valencia_future_predictions.xls
│   ├── Madrid_future_predictions.xls
│   └── crawler.py 
├── venv/        
│   ├── Include 
│   ├── Lib
│   └── Scripts
│   └── pyvenv.cfg 
├── api_conexion.py
├── app.py                              # Función para ejecutar la aplicación de interfaz web gracias a la librería **Streamlit**
├── generate_dataset.py                 # Módulo para obtener datos de URL Meteostat para luego exportar en datasets
├── predict_weather.py                  # Módulo de predictivo para generar y exportar datos en excel XLS
├── train_model.py                      # Módulo de entramiento de datos obtenidos de historial CSV
├── requirements.txt                    # Dependencias del proyecto
├── dev-requirements.txt                # Dependencias para desarrollo
└── README.md                           # Este archivo
```
---

## 🚀 **Guía de Uso**
### 1. Instalación
🔹1. Clona este repositorio:
```
git clone https://github.com/tu-usuario/WeatherInsight.git
cd WeatherInsight
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

- ``--models``: Archivo donde se almacenará el índice invertido.

---

#### 🔍 Predictions
En este módulo se encargará de realizar la predicción basándose en los modelos generados en el directorio **models** por nombre de ciudad:
```
python predict_weather.py"
```
**Parámetros:**
- ``--predictions``: Guardado datos exportados en formato XLS para poder visualizarlos en local.

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

## 🗂️ Contribuciones
### 🤝 ¿Quieres colaborar? ¡Eres bienvenido! Sigue estos pasos:

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

- **Luca 🕷️** - Pendiente de asignar tareas
- **Sergio 📇** - Pendiente de asignar tareas
- **Rubén 🔍** - Organización y distribución tareas
Agradecemos también a la Universidad Europea por inspirar este proyecto académico. 🙌
