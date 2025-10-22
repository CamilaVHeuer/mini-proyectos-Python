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

# --- Funciones auxiliares ---
def validar_entrada(texto: str, permitir_cancelar=True):
    """
    Valida la entrada del usuario.
    - Elimina espacios iniciales/finales y capitaliza la palabra.
    - Retorna:
        'cancelado' si el usuario ingresa cancelar/volver/salir.
        'vacio' si la entrada está vacía.
        'invalido' si contiene caracteres no permitidos.
        texto limpio si es válido.
    """
    texto = texto.strip().title()
    #valido si el usuario quiere cancelar
    if permitir_cancelar and texto.lower() in ['cancelar', 'volver', 'salir']:
        return "cancelado"
    #valido si la entrada está vacía
    if texto == "":
        return "vacio"
    #valido si la entrada contiene caracteres no permitidos
    if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", texto):
        return "invalido"
    #si todo está bien, retorno el texto limpio
    return texto

def intentar_agregar_fruta():
    entrada = input('Ingrese la fruta que desea agregar (o "cancelar" para volver al menú): ').strip().title()
    resultado = validar_entrada(entrada)
    if resultado == "cancelado":
        print("Operación cancelada. Volviendo al menú principal.\n")
        return ('cancelado', None)  #volver al menú principal
    if resultado == "vacio":
        print("No se ingresó ninguna fruta, por favor intente nuevamente.\n")
        return ('vacio', None)  # Salgo de la función sin agregar nada
    if resultado == "invalido":
        print("La fruta debe contener solo letras y espacios, sin números ni caracteres especiales.\n")
        return ('invalido', None)  # Salgo de la función sin agregar nada
    if resultado in frutas:
        print("La fruta ya está en la lista.\n")
        return ('duplicado', resultado)  # Salgo de la función sin agregar nada
    # Si la entrada es válida, la agrego a la lista
    frutas.append(resultado)
    print(f"Fruta {resultado} agregada con éxito.\n")
    return ('ok', resultado)  # Indico que se agregó la fruta con éxito


def mostrar_frutas():
    if frutas: # Verifico si la lista no está vacía
        print("Lista de frutas:")
        for i, fruta in enumerate(frutas, start=1):
            print(f"{i}. {fruta}")
        print()  # Línea en blanco al final de la lista
    else:
        print("No hay frutas en la lista.\n")

def intentar_eliminar_fruta():
    if not frutas:
        print("No hay frutas en la lista.\n")
        return 'no_encontrado' #volver al menú principal para evitar loop infinito
    if frutas:
        entrada = input('Ingrese la fruta que desea eliminar (o "cancelar" para volver al menú): ').strip().title()
        resultado = validar_entrada(entrada)
        if resultado == "cancelado":
            print("Operación cancelada. Volviendo al menú principal.\n")
            return ('cancelado', None)  #volver al menú principal
        if resultado == "vacio":
            print("No se ingresó ninguna fruta, por favor intente nuevamente.\n")
            return ('vacio', None)  # Salgo de la función sin eliminar nada
        if resultado not in frutas:
            print("La fruta no se encuentra en la lista.\n")
            return ('no_encontrado', None)  # Salgo de la función sin eliminar nada

        confirmacion = input('Está seguro que desea eliminar la fruta? (s/n): ').strip().lower()
        if confirmacion == 's':
            frutas.remove(resultado)
            print(f"Fruta {resultado} eliminada con éxito.\n")
            return ('ok', resultado)  # Indico que se eliminó la fruta con éxito
        else:
            print("Operación cancelada.\n")
            return ('cancelado', None)  # Operación cancelada, volver al menú principal

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

        match opcion:
            case "1":
                while True:
                    estado, _ = intentar_agregar_fruta()
                    if estado in ["ok", "cancelado"]:
                        break
                
            case "2":
                mostrar_frutas()
            case "3":
                while True:
                    estado, _ = intentar_eliminar_fruta()
                    if estado in ["ok", "cancelado", "no_encontrado"]:
                        break
            case "4":
                print("Saliendo del programa...\n")
                break
        """if opcion == "1":
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
            print("Opción no válida. Por favor, seleccione una opción del menú.\n")""" 

