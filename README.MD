# Analizador de Datos - Fórmula 1

## 1. Descripción del proyecto

Este proyecto consiste en desarrollar un analizador de datos utilizando Python. El programa trabaja con información meteorológica relacionada con la Fórmula 1 durante las temporadas 2018 a 2023.

El usuario puede cargar un archivo CSV, explorar sus datos, calcular estadísticas, filtrar registros y generar gráficos desde un menú interactivo por consola.

## 2. Tecnologías utilizadas

- Python 3.12
- Pandas 3.1.1
- Matplotlib 3.11.2
- JSON
- Logging
- Git y GitHub
- Visual Studio Code

## 3. Dataset

**Archivo:** `f1_weather_2018_2023.csv`

El dataset contiene 18.214 registros y 10 columnas.

Entre las variables disponibles se encuentran:

- Time: tiempo de la medición.
- AirTemp: temperatura del aire.
- Humidity: humedad.
- Pressure: presión atmosférica.
- Rainfall: indicador de lluvia.
- TrackTemp: temperatura de pista.
- WindDirection: dirección del viento.
- WindSpeed: velocidad del viento.
- Round Number: número de carrera.
- Year: año.

**Fuente del dataset:** Kaggle (datos meteorológicos de Fórmula 1, temporadas 2018-2023).

## 4. Instalación y ejecución

Primero, crear un entorno virtual:

```powershell
py -m venv .venv
```

Activar el entorno virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```powershell
python -m pip install -r requirements.txt
```

Ejecutar el programa:

```powershell
python main.py
```

## 5. Funcionalidades

El programa cuenta con seis opciones:

1. Cargar dataset: lee el archivo CSV y muestra sus dimensiones.
2. Ver información general: muestra las primeras filas, columnas, tipos de datos y valores vacíos.
3. Estadísticas: calcula cantidad, promedio, mínimo, máximo y mediana de una columna numérica.
4. Filtrar datos: permite buscar registros según una categoría o valor.
5. Generar gráficos: crea un gráfico de barras y un histograma.
6. Salir: guarda los resultados en un archivo JSON y finaliza el programa.

## 6. Gráficos generados

Los gráficos se guardan como imágenes PNG dentro de la carpeta `graficos/`.

### Gráfico de barras

![Mediciones con y sin lluvia](graficos/barras_lluvia.png)

### Histograma

![Distribución de la temperatura del aire](graficos/histograma_temperatura.png)


Los gráficos se guardan como imágenes PNG dentro de la carpeta `graficos/`.

### Gráfico de barras

`graficos/barras_lluvia.png`

### Histograma

`graficos/histograma_temperatura.png`

## 7. Archivos de resultados

- `resumen.json`: almacena las dimensiones del dataset, las columnas, estadísticas y gráficos generados.
- `analisis.log`: registra las operaciones realizadas y los errores del programa.

## 8. Conclusiones del análisis

1. El dataset contiene 18.214 mediciones meteorológicas correspondientes al período 2018-2023.
2. La temperatura promedio del aire fue de 23,62 °C, con un mínimo de 8,9 °C y un máximo de 37,2 °C.
3. Se identificaron 1.346 mediciones con lluvia, equivalentes aproximadamente al 7,39 % de los registros.

## 9. Estructura del proyecto

```text
F1_Dataset/
├── .gitignore
├── main.py
├── analisis.py
├── graficos.py
├── data/
│   └── f1_weather_2018_2023.csv
├── graficos/
│   ├── barras_lluvia.png
│   └── histograma_temperatura.png
├── resumen.json
├── analisis.log
├── requirements.txt
└── README.md
```

## 10. Autor

Proyecto individual desarrollado para la materia Programación 1, correspondiente a la carrera Ciencia de Datos.

Mikhail Acevedo.
