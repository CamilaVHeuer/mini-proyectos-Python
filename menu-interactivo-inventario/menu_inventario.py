#Implementación de un menú para gestionar un inventario de productos.
#Permite alternar entre almacenamiento en diccionario (memoria) o base de datos MySQL
#usando la variable de entorno INVENTARIO_MODO.
#El programa presentará un menú que le permitirá al usuario elegir qué acción desea realizar.

import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Determinar modo de almacenamiento desde variable de entorno
MODO_ALMACENAMIENTO = os.getenv('INVENTARIO_MODO', 'diccionario').lower()

# Imports dinámicos según el modo configurado
if MODO_ALMACENAMIENTO == 'bd':
    from productos.operaciones_bd import (
        intentar_agregar_producto,
        mostrar_productos,
        intentar_actualizar_producto,
        intentar_eliminar_producto
    )
    MODO_TEXTO = "Base de datos MySQL"
else:
    from productos.operaciones_diccionario import (
        intentar_agregar_producto, 
        mostrar_productos, 
        intentar_actualizar_producto, 
        intentar_eliminar_producto
    )
    MODO_TEXTO = "Diccionario (en memoria)"

def mostrar_menu():
    """Menú principal - modo determinado por variable de entorno"""
    while True:
        print(f"\n--- Menú - Modo: {MODO_TEXTO} ---")
        print("1. ➕ Agregar producto")
        print("2. 📋 Mostrar productos")
        print("3. ✏️ Actualizar producto")
        print("4. 🗑️ Eliminar producto")
        print("5. 🚪 Salir")
        print("---------------")

        opcion = input("Seleccione una opción del 1 al 5: ")
        #validar la opción ingresada
        if not opcion.isdigit() or not 1 <= int(opcion) <= 5:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 5.\n")
            continue  # Volver al inicio del bucle si la opción es inválida

        match opcion:
            case "1":
                while True:
                    estado, _ = intentar_agregar_producto()
                    if estado in ["ok", "cancelado"]:
                        break
                
            case "2":
                mostrar_productos()
                
            case "3":
                while True:
                    estado, _ = intentar_actualizar_producto()
                    if estado in ["ok", "cancelado", "no_encontrado"]:
                        break
                        
            case "4":
                while True:
                    estado, _ = intentar_eliminar_producto()
                    if estado in ["ok", "cancelado", "no_encontrado"]:
                        break
                        
            case "5":
                print("Saliendo del programa...\n")
                break

def main():
    """Función principal del programa"""
    mostrar_menu()

if __name__ == "__main__":
    main()
