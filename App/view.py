import pandas as pd
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
# df = pd.DataFrame([1, 2, 3], columns={'fdfd'})
# print(df.to_markdown(index=False, tablefmt='grid'))


def printMenu():
    """
    Function to print the Menu Options
    """
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- ")


catalog = controller.newCatalog()


"""
Menu principal
"""

while True:

    printMenu()

    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:

        print("Cargando información de los archivos ....")
        controller.loadData(catalog)
        print(catalog)

    elif int(inputs[0]) == 2:
        pass

    else:
        print("Salinedo de la Aplicación")
        sys.exit(0)
