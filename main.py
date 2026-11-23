
# Importamos logging para registrar las operaciones del programa
import logging

# Importamos Path para indicar la ubicación del archivo de registro
from pathlib import Path


# Configuramos el archivo donde se guardarán los registros
logging.basicConfig(
    filename=Path(__file__).resolve().parent / "analisis.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


# Importamos las funciones para trabajar con el dataset
from analisis import (
    cargar_dataset,
    mostrar_informacion,
    calcular_estadisticas,
    filtrar_datos,
    guardar_resumen
)

# Importamos la función para generar gráficos
from graficos import generar_graficos


# Función que muestra el menú principal del programa
def mostrar_menu():
    """Muestra las seis opciones disponibles del programa."""

    # Mostramos el título del menú
    print("\n===== ANALIZADOR DE DATOS - FORMULA 1 =====")

    # Mostramos las opciones disponibles
    print("1. Cargar dataset")
    print("2. Ver información general")
    print("3. Estadísticas de una columna")
    print("4. Filtrar datos")
    print("5. Generar gráficos")
    print("6. Salir")


# Función principal del programa
def main():
    """Controla el menú y ejecuta las opciones seleccionadas."""

    # Inicializamos el dataset como vacío
    df = None

    # Creamos un bucle para mantener el menú funcionando
    while True:

        # Mostramos las opciones del menú
        mostrar_menu()

        # Solicitamos al usuario que ingrese una opción
        opcion = input("Ingrese una opción: ")

        # Evaluamos la opción seleccionada
        if opcion == "1":

            # Cargamos el dataset y guardamos los datos en df
            df = cargar_dataset()

        elif opcion == "2":

            # Mostramos la información general del dataset
            mostrar_informacion(df)

        elif opcion == "3":

            # Calculamos las estadísticas de una columna
            calcular_estadisticas(df)

        elif opcion == "4":

            # Filtramos los datos según la categoría seleccionada
            filtrar_datos(df)

        elif opcion == "5":

            # Generamos los gráficos utilizando el dataset cargado
            generar_graficos(df)

        elif opcion == "6":

            # Guardamos los resultados en el archivo JSON
            guardar_resumen(df)

            # Registramos que el usuario decidió salir
            logging.info("Programa finalizado por el usuario.")

            # Mostramos el mensaje de salida
            print("Saliendo del programa...")

            # Terminamos el bucle del menú
            break

        else:

            # Informamos si el usuario ingresó una opción inválida
            print("Opción inválida. Intente nuevamente.")

            # Registramos la opción incorrecta en el archivo de logs
            logging.error("Opción de menú inválida: %s", opcion)


# Ejecutamos el programa principal
if __name__ == "__main__":
    main()
