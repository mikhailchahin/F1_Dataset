
# Importamos Pandas para trabajar con los datos
import pandas as pd

# Importamos logging para registrar las operaciones
import logging

# Importamos json para guardar resultados en formato JSON
import json

# Importamos Path para construir rutas de archivos
from pathlib import Path


# Función para cargar el dataset
def cargar_dataset():
    """Carga el archivo CSV y muestra sus dimensiones."""

    # Indicamos la ubicación del archivo CSV
    ruta_archivo = (
        Path(__file__).resolve().parent
        / "data"
        / "f1_weather_2018_2023.csv"
    )

    try:
        # Leemos el archivo CSV utilizando Pandas
        df = pd.read_csv(ruta_archivo)

        # Registramos la carga correcta del dataset
        logging.info(
            "Dataset cargado: %s (%s filas)",
            ruta_archivo.name,
            df.shape[0]
        )

        # Mostramos un mensaje de confirmación
        print("\nDataset cargado correctamente.")

        # Mostramos la cantidad de filas
        print(f"Cantidad de filas: {df.shape[0]}")

        # Mostramos la cantidad de columnas
        print(f"Cantidad de columnas: {df.shape[1]}")

        # Devolvemos el DataFrame para utilizarlo en otras funciones
        return df

    except FileNotFoundError:
        # Informamos si no encontramos el archivo
        print("\nError: no se encontró el archivo CSV.")

        # Registramos el error
        logging.error("Archivo CSV no encontrado: %s", ruta_archivo)

        # Devolvemos None porque no se pudo cargar el dataset
        return None

    except (pd.errors.ParserError, UnicodeDecodeError):
        # Informamos si existe un problema con el formato del CSV
        print("\nError: el archivo CSV tiene un formato inválido.")

        # Registramos el error
        logging.exception("Error al leer el formato del CSV: %s", ruta_archivo)

        return None


# Función para mostrar información general del dataset
def mostrar_informacion(df):
    """Muestra las primeras filas y la estructura del dataset."""

    # Comprobamos que el dataset esté cargado
    if df is None:
        print("Primero debe cargar el dataset.")
        logging.error("Intento de consultar información sin cargar el dataset.")
        return

    # Mostramos las primeras cinco filas
    print("\n===== PRIMERAS CINCO FILAS =====")
    print(df.head())

    # Mostramos los nombres de las columnas
    print("\n===== NOMBRES DE LAS COLUMNAS =====")
    print(df.columns)

    # Mostramos los tipos de datos de cada columna
    print("\n===== TIPOS DE DATOS =====")
    print(df.dtypes)

    # Contamos los valores vacíos de cada columna
    print("\n===== VALORES VACÍOS =====")
    print(df.isnull().sum())

    # Registramos la consulta de información general
    logging.info("Información general del dataset consultada.")


# Función para calcular estadísticas de una columna
def calcular_estadisticas(df):
    """Calcula estadísticas básicas de una columna numérica."""

    # Comprobamos que el dataset esté cargado
    if df is None:
        print("Primero debe cargar el dataset.")
        logging.error("Intento de calcular estadísticas sin cargar el dataset.")
        return

    # Obtenemos las columnas que contienen números
    columnas_numericas = df.select_dtypes(include="number").columns

    # Mostramos las columnas disponibles
    print("\n===== COLUMNAS NUMÉRICAS =====")
    for columna in columnas_numericas:
        print(columna)

    # Solicitamos al usuario que elija una columna
    nombre_columna = input("\nIngrese el nombre de la columna: ")

    # Comprobamos que la columna exista
    if nombre_columna not in df.columns:
        print("Error: la columna no existe.")
        logging.error("Columna inexistente para estadísticas: %s", nombre_columna)
        return

    # Comprobamos que la columna sea numérica
    if not pd.api.types.is_numeric_dtype(df[nombre_columna]):
        print("Error: debe seleccionar una columna numérica.")
        logging.error("Columna no numérica seleccionada: %s", nombre_columna)
        return

    # Guardamos la columna seleccionada
    datos = df[nombre_columna]

    # Mostramos las estadísticas calculadas
    print("\n===== ESTADÍSTICAS =====")
    print(f"Cantidad: {datos.count()}")
    print(f"Promedio: {datos.mean():.2f}")
    print(f"Mínimo: {datos.min()}")
    print(f"Máximo: {datos.max()}")
    print(f"Mediana: {datos.median()}")

    # Registramos el cálculo de estadísticas
    logging.info("Estadísticas calculadas para la columna: %s", nombre_columna)


# Función para filtrar los datos por una categoría
def filtrar_datos(df):
    """Filtra los registros según una columna y un valor elegido."""

    # Comprobamos que el dataset esté cargado
    if df is None:
        print("Primero debe cargar el dataset.")
        logging.error("Intento de filtrar datos sin cargar el dataset.")
        return

    # Identificamos las columnas categóricas y booleanas
    columnas_categoricas = [
        columna for columna in df.columns
        if (
            not pd.api.types.is_numeric_dtype(df[columna])
            or pd.api.types.is_bool_dtype(df[columna])
        )
    ]

    # Mostramos las columnas disponibles
    print("\n===== COLUMNAS CATEGÓRICAS =====")
    for columna in columnas_categoricas:
        print(columna)

    # Solicitamos al usuario que elija una columna
    nombre_columna = input("\nIngrese el nombre de la columna: ")

    # Comprobamos que la columna exista entre las disponibles
    if nombre_columna not in columnas_categoricas:
        print("Error: debe seleccionar una columna categórica.")
        logging.error("Columna categórica inexistente o inválida: %s", nombre_columna)
        return

    # Solicitamos el valor que queremos buscar
    valor = input("Ingrese el valor que desea buscar: ")

    # Convertimos el valor si la columna contiene booleanos
    if pd.api.types.is_bool_dtype(df[nombre_columna]):

        # Convertimos el texto ingresado a True o False
        if valor.strip().lower() == "true":
            valor = True

        elif valor.strip().lower() == "false":
            valor = False

        else:
            print("Error: ingrese True o False.")
            logging.error("Valor booleano inválido: %s", valor)
            return

    # Filtramos las filas que coinciden con el valor elegido
    resultados = df[df[nombre_columna] == valor]

    # Mostramos la cantidad de coincidencias
    print(f"\nCantidad de registros encontrados: {len(resultados)}")

    # Mostramos las primeras diez filas encontradas
    print("\n===== RESULTADOS DEL FILTRO =====")
    print(resultados.head(10))

    # Registramos el filtro aplicado y la cantidad de resultados
    logging.info(
        "Filtro aplicado: %s = %s (%s resultados)",
        nombre_columna,
        valor,
        len(resultados)
    )


# Función para guardar los resultados en un archivo JSON
def guardar_resumen(df):
    """Guarda un resumen del dataset y sus estadísticas en JSON."""

    # Comprobamos que el dataset esté cargado
    if df is None:
        print("Primero debe cargar el dataset.")
        logging.error("Intento de guardar resumen sin cargar el dataset.")
        return

    # Creamos un diccionario para guardar las estadísticas
    estadisticas = {}

    # Obtenemos las columnas numéricas
    columnas_numericas = df.select_dtypes(include="number").columns

    # Calculamos las estadísticas de cada columna numérica
    for columna in columnas_numericas:

        # Seleccionamos los datos de la columna
        datos = df[columna]

        # Guardamos las estadísticas en un diccionario
        estadisticas[columna] = {
            "cantidad": int(datos.count()),
            "promedio": float(datos.mean()),
            "minimo": float(datos.min()),
            "maximo": float(datos.max()),
            "mediana": float(datos.median())
        }

    # Obtenemos la carpeta principal del proyecto
    carpeta_proyecto = Path(__file__).resolve().parent

    # Buscamos los gráficos PNG que fueron generados
    carpeta_graficos = carpeta_proyecto / "graficos"

    # Guardamos los nombres de los gráficos en una lista
    graficos_generados = [
        f"graficos/{archivo.name}"
        for archivo in carpeta_graficos.glob("*.png")
    ]

    # Creamos el diccionario principal del resumen
    resumen = {
        "dataset": "f1_weather_2018_2023.csv",
        "filas": int(df.shape[0]),
        "columnas": df.columns.tolist(),
        "estadisticas": estadisticas,
        "graficos_generados": graficos_generados
    }

    # Indicamos la ubicación del archivo JSON
    ruta_resumen = carpeta_proyecto / "resumen.json"

    # Guardamos el diccionario en formato JSON
    with open(ruta_resumen, "w", encoding="utf-8") as archivo:
        json.dump(resumen, archivo, indent=4, ensure_ascii=False)

    # Informamos que el resumen fue guardado
    print("\nResumen guardado correctamente en resumen.json.")

    # Registramos el guardado del resumen
    logging.info("Resumen guardado correctamente: %s", ruta_resumen.name)
