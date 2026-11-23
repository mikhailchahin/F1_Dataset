
# Importamos Matplotlib para crear gráficos
import matplotlib.pyplot as plt

# Importamos logging para registrar las operaciones
import logging

# Importamos Path para trabajar con las carpetas
from pathlib import Path


# Función para generar los gráficos
def generar_graficos(df):
    """Genera y guarda un gráfico de barras y un histograma."""

    # Comprobamos que el dataset esté cargado
    if df is None:
        print("Primero debe cargar el dataset.")

        # Registramos el error
        logging.error(
            "Intento de generar gráficos sin cargar el dataset."
        )
        return

    try:
        # Comprobamos que existan las columnas necesarias
        if "Rainfall" not in df.columns:
            raise KeyError("No existe la columna Rainfall.")

        if "AirTemp" not in df.columns:
            raise KeyError("No existe la columna AirTemp.")

        # Indicamos la ubicación de la carpeta de gráficos
        carpeta_graficos = (
            Path(__file__).resolve().parent / "graficos"
        )

        # Creamos la carpeta si todavía no existe
        carpeta_graficos.mkdir(parents=True, exist_ok=True)

        # Contamos las mediciones con y sin lluvia
        conteo_lluvia = df["Rainfall"].value_counts().reindex(
            [False, True], fill_value=0
        )

        # Creamos una figura para el gráfico de barras
        plt.figure(figsize=(8, 5))

        # Creamos el gráfico de barras
        plt.bar(
            ["Sin lluvia", "Con lluvia"],
            conteo_lluvia.values
        )

        # Agregamos el título y los nombres de los ejes
        plt.title("Mediciones con y sin lluvia")
        plt.xlabel("Condición climática")
        plt.ylabel("Cantidad de mediciones")

        # Ajustamos los espacios del gráfico
        plt.tight_layout()

        # Indicamos la ruta donde guardaremos el gráfico de barras
        ruta_barras = carpeta_graficos / "barras_lluvia.png"

        # Guardamos el gráfico como imagen PNG
        plt.savefig(ruta_barras)

        # Registramos que el gráfico de barras fue generado
        logging.info(
            "Gráfico guardado: graficos/barras_lluvia.png"
        )

        # Cerramos la figura
        plt.close()

        # Creamos una figura para el histograma
        plt.figure(figsize=(8, 5))

        # Creamos el histograma de temperaturas
        plt.hist(df["AirTemp"], bins=10)

        # Agregamos el título y los nombres de los ejes
        plt.title("Distribución de la temperatura del aire")
        plt.xlabel("Temperatura del aire")
        plt.ylabel("Frecuencia")

        # Ajustamos los espacios del gráfico
        plt.tight_layout()

        # Indicamos la ruta donde guardaremos el histograma
        ruta_histograma = (
            carpeta_graficos / "histograma_temperatura.png"
        )

        # Guardamos el histograma como imagen PNG
        plt.savefig(ruta_histograma)

        # Registramos que el histograma fue generado
        logging.info(
            "Gráfico guardado: graficos/histograma_temperatura.png"
        )

        # Cerramos la figura
        plt.close()

        # Informamos que los gráficos fueron generados
        print("\nGráficos generados correctamente.")

    except (KeyError, OSError, ValueError) as error:

        # Cerramos cualquier figura que haya quedado abierta
        plt.close("all")

        # Informamos que ocurrió un problema
        print(f"\nError al generar los gráficos: {error}")

        # Registramos el error en el archivo de logs
        logging.exception("Error durante la generación de gráficos.")
