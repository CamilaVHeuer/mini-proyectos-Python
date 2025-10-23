#Implementación de un menú para gestionar un inventario de productos.
#Se podrá agregar, mostrar, actualizar y eliminar productos de un inventario (que será un diccionario).
#El programa presentará un menú que le permitirá al usuario elegir qué acción desea realizar.
#El programa se ejecutará hasta que el usuario decida salir.

from productos.operaciones import intentar_agregar_producto, mostrar_productos, intentar_actualizar_producto, intentar_eliminar_producto

def mostrar_menu():
    while True:
        print("\n--- Menú ---")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")
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
