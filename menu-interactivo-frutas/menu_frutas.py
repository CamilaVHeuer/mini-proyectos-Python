#Implementación de un menú para gestionar
#una lista de frutas con funciones.
#se podrá agregar, mostrar y eliminar frutas de la lista.
#El programa presentará un menú que le permitirá al usuario elegir qué acción desea realizar.

#En primer lugar, definimos una lista vacía llamada frutas que almacenará los nombres de
# las frutas. Luego, crearemos tres funciones: una para agregar frutas, otra para consultar
# la lista de frutas, y una más para borrar una fruta específica. Finalmente,implementaremos una función para mostrar el menú y permitir que se seleccione una
# opción.

import re

frutas = []  # Lista para almacenar las frutas

def intentar_agregar_fruta():
    fruta = input('Ingrese la fruta que desea agregar (o "cancelar" para volver al menú): ').strip().title()
    #validar que no se ingrese una cadena vacía
    if fruta == "":
        print("No se ingresó ninguna fruta, por favor intente nuevamente.\n")
        return False #salgo de la función sin agregar nada
    #validar si el usuario quiere cancelar
    if fruta.lower() in ['cancelar', 'volver', 'salir']:
        print("Operación cancelada. Volviendo al menú principal.\n")
        return True #volver al menú principal
    #validar que solo contenga letras (incluye acentos y ñ) y espacios
    if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", fruta):
        print("La fruta debe contener solo letras y espacios, sin números ni caracteres especiales.\n")
        return False #salgo de la función sin agregar nada
    #validar que no se ingrese una fruta que ya esté en la lista
    if fruta in frutas:
        print("La fruta ya está en la lista.\n")
        return False #salgo de la función sin agregar nada
    frutas.append(fruta)
    print(f"Fruta {fruta} agregada con éxito.\n")
    return True #indico que se agregó la fruta con éxito

def mostrar_frutas():
    if frutas: # Verifico si la lista no está vacía
        print("Lista de frutas:")
        for i, fruta in enumerate(frutas, start=1):
            print(f"{i}. {fruta}")
        print()  # Línea en blanco al final de la lista
    else:
        print("No hay frutas en la lista.\n")

def intentar_eliminar_fruta():
    if frutas:
        fruta_a_eliminar = input('Ingrese la fruta que desea eliminar (o "cancelar" para volver al menú): ').strip().title()
        #validar que no se ingrese una cadena vacía
        if fruta_a_eliminar == "":
            print("No se ingresó ninguna fruta, por favor intente nuevamente.\n")
            return False #salgo de la función sin eliminar nada
        #validar si el usuario quiere cancelar
        if fruta_a_eliminar.lower() in ['cancelar', 'volver', 'salir']:
            print("Operación cancelada. Volviendo al menú principal.\n")
            return True #volver al menú principal
        if fruta_a_eliminar in frutas:
            confirmacion = input('Está seguro que desea eliminar la fruta? (s/n): ').strip().lower()
            if confirmacion == 's':
                frutas.remove(fruta_a_eliminar)
                print(f"Fruta {fruta_a_eliminar} eliminada con éxito.\n")
                return True #indico que se eliminó la fruta con éxito
            else:
                print("Operación cancelada.\n")
                return True #operación cancelada, volver al menú principal
        else:
            print("La fruta que desea eliminar no está en la lista.\n")
            return False #salgo de la función sin eliminar nada
    else:
        print("No hay frutas en la lista.\n")
        return True #volver al menú principal, si no escribo este return, me queda en un loop infinito porque en el menú principal sigue intentando eliminar fruta

def mostrar_menu():
    while True:
        print("\n--- Menú ---")
        print("1. Agregar fruta")
        print("2. Mostrar frutas")
        print("3. Eliminar fruta")
        print("4. Salir")
        print("---------------")

        opcion = input("Seleccione una opción del 1 al 4: ")
        #validar la opción ingresada
        if not opcion.isdigit() or not 1 <= int(opcion) <= 4:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 4.\n")
            continue  # Volver al inicio del bucle si la opción es inválida

        if opcion == "1":
            fruta_agregada = False
            while not fruta_agregada:
                fruta_agregada = intentar_agregar_fruta()
        elif opcion == "2":
            mostrar_frutas()
        elif opcion == "3":
            fruta_eliminada = False
            while not fruta_eliminada:
                # intentar_eliminar_fruta retorna True si se eliminó o se canceló (para volver al menú)
                fruta_eliminada = intentar_eliminar_fruta()
        elif opcion == "4":
            print("Saliendo del programa...\n")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.\n")

