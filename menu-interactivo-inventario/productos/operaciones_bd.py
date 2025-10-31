# Funciones para agregar, mostrar, actualizar y eliminar productos del inventario usando base de datos MySQL
from productos.validaciones import validar_nombre, validar_tipo, validar_precio, validar_stock
from productos.database import obtener_conexion_base_datos

def agregar_producto_bd(nombre, tipo, precio, stock, modo_prueba=False):
    """
    Agrega un producto usando UNIQUE constraint para evitar duplicados (thread-safe).
    
    Args:
        nombre (str): Nombre del producto
        tipo (str): Tipo del producto ('fruta' o 'verdura')
        precio (float): Precio del producto
        stock (int): Stock disponible
        modo_prueba (bool): Si True, usa la BD de pruebas
        
    Returns:
        bool: True si se agregó exitosamente, False en caso contrario
    """
    bd = obtener_conexion_base_datos(modo_prueba)
    if not bd:
        print("❌ Error: No se pudo conectar a la base de datos")
        return False
    
    try:
        # Insertar directamente - la BD maneja duplicados con UNIQUE constraint
        consulta_insertar = """
            INSERT INTO productos (nombre, tipo, precio, stock)
            VALUES (%s, %s, %s, %s)
        """
        
        exito = bd.ejecutar_consulta(
            consulta_insertar, 
            (nombre, tipo, precio, stock)
        )
        
        if exito:
            filas_afectadas = bd.cursor.rowcount
            if filas_afectadas > 0:
                print(f"✅ Producto '{nombre}' agregado exitosamente a la base de datos")
                return True
            else:
                print("⚠️ No se insertó ningún producto.")
                return False
        else:
            return False

    except Exception as e:
        # Manejar específicamente error de duplicado (MySQL)
        if "1062" in str(e) or "Duplicate entry" in str(e):
            print(f"❌ Error: El producto '{nombre}' ya existe en la base de datos")
        else:
            print(f"❌ Error inesperado al insertar producto: {e}")
        return False
    finally:
        bd.desconectar()  # Cierra su propia conexión


def mostrar_productos(modo_prueba=False):
    """
    Muestra todos los productos desde la base de datos MySQL
    
    Args:
        modo_prueba (bool): Si True, usa la BD de pruebas
    """
    bd = obtener_conexion_base_datos(modo_prueba)
    if not bd:
        print("❌ Error: No se pudo conectar a la base de datos")
        return
    
    try:
        consulta = """
            SELECT id, nombre, tipo, precio, stock, 
                   DATE_FORMAT(fecha_creacion, '%d/%m/%Y %H:%i') as fecha_creacion,
                   DATE_FORMAT(fecha_actualizacion, '%d/%m/%Y %H:%i') as fecha_actualizacion
            FROM productos 
            ORDER BY nombre
        """
        
        productos_bd = bd.ejecutar_consulta(consulta, obtener_resultados=True)
        
        if productos_bd:
            print("\n📋 Lista de productos en la base de datos:")
            print("-" * 80)
            for i, producto in enumerate(productos_bd, start=1):
                print(f"{i}. {producto['nombre']}")
                print(f"   • Tipo: {producto['tipo']}")
                print(f"   • Precio: ${producto['precio']}")
                print(f"   • Stock: {producto['stock']} unidades")
                print(f"   • Creado: {producto['fecha_creacion']}")
                print(f"   • Actualizado: {producto['fecha_actualizacion']}")
                print()
        else:
            print("📝 No hay productos en la base de datos")
            
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
    finally:
        bd.desconectar()


def actualizar_producto_bd(nombre, campo, nuevo_valor, modo_prueba=False):
    """
    Actualiza un producto en la base de datos MySQL
    
    Args:
        nombre (str): Nombre del producto a actualizar
        campo (str): Campo a actualizar ('precio' o 'stock')
        nuevo_valor (float|int): Nuevo valor para el campo
        modo_prueba (bool): Si True, usa la BD de pruebas
        
    Returns:
        bool: True si se actualizó exitosamente, False en caso contrario
    """
    bd = obtener_conexion_base_datos(modo_prueba)
    if not bd:
        print("❌ Error: No se pudo conectar a la base de datos")
        return False
    
    try:
        
        # Validar el campo a actualizar
        if campo not in ['precio', 'stock']:
            print(f"❌ Error: Campo '{campo}' no válido. Solo se puede actualizar 'precio' o 'stock'")
            return False
        
        # Actualizar el producto
        consulta_actualizar = f"UPDATE productos SET {campo} = %s WHERE nombre = %s"
        
        exito = bd.ejecutar_consulta(
            consulta_actualizar, 
            (nuevo_valor, nombre)
        )
        
        if not exito:
            print(f"❌ Error al intentar actualizar el producto '{nombre}'")
            return False
        #Verificar si se afectó alguna fila
        filas_afectadas = bd.cursor.rowcount
        if filas_afectadas > 0:
            print(f"✅ {campo.capitalize()} del producto '{nombre}' actualizado a {nuevo_valor}")
            return True
        else:
            print(f"❌ Error: El producto '{nombre}' no existe en la base de datos")
            return False
        
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False
    finally:
        bd.desconectar()


def eliminar_producto_bd(nombre, bd_conexion):
    """
    Elimina un producto usando una conexión existente
    
    Args:
        nombre (str): Nombre del producto a eliminar
        bd_conexion (DatabaseConnection): Conexión ya establecida
        
    Returns:
        bool: True si se eliminó exitosamente, False en caso contrario
    """
    try:
    
        # Intentar eliminar el producto directamente y usar rowcount para verificar
        consulta_eliminar = "DELETE FROM productos WHERE nombre = %s"
        exito = bd_conexion.ejecutar_consulta(consulta_eliminar, (nombre,))

        if exito:
            # Verificar cuántas filas fueron afectadas
            filas_afectadas = bd_conexion.cursor.rowcount
            
            if filas_afectadas > 0:
                print(f"✅ Producto '{nombre}' eliminado exitosamente")
                return True
            else:
                print(f"❌ Error: El producto '{nombre}' no existe")
                return False
        else:
            print("❌ Error: No se pudo ejecutar la eliminación")
            return False
            
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False
    # No cierra conexión - esa responsabilidad es del caller


def intentar_agregar_producto(modo_prueba=False):
    """
    Función interactiva para agregar un producto con validaciones usando BD
    
    Args:
        modo_prueba (bool): Si True, usa la BD de pruebas
        
    Returns:
        tuple: (resultado, nombre) donde resultado puede ser:
               'ok', 'cancelado', 'vacio', 'invalido', 'duplicado'
    """
    nombre_producto = input('Ingrese el nombre del producto que desea agregar (o "cancelar" para volver al menú): ')
    nombre = validar_nombre(nombre_producto)
    if nombre == "cancelado":
        print("Operación cancelada. Volviendo al menú principal.\n")
        return ('cancelado', None)
    if nombre == "vacio":
        print("No se ingresó ningún producto, por favor intente nuevamente.\n")
        return ('vacio', None)
    if nombre == "invalido":
        print("El producto debe contener solo letras y espacios, sin números ni caracteres especiales.\n")
        return ('invalido', None)
    
    tipo_producto = input('Ingrese el tipo de producto (fruta/verdura) (o "cancelar" para volver al menú): ')
    tipo = validar_tipo(tipo_producto)
    if tipo == 'cancelado':
        print("Operación cancelada. Volviendo al menú principal.\n")
        return ('cancelado', None)
    if tipo == 'invalido':
        print("El tipo de producto debe ser 'fruta' o 'verdura'.\n")
        return ('invalido', None)
    
    precio_producto = input('Ingrese el precio del producto (o "cancelar" para volver al menú): ')
    precio = validar_precio(precio_producto)
    if precio == 'cancelado':
        print("Operación cancelada. Volviendo al menú principal.\n")
        return ('cancelado', None)
    if precio == 'invalido':
        print("El precio debe ser un número positivo.\n")
        return ('invalido', None)
    
    stock_producto = input('Ingrese el stock del producto (o "cancelar" para volver al menú): ')
    stock = validar_stock(stock_producto)
    if stock == 'cancelado':
        print("Operación cancelada. Volviendo al menú principal.\n")
        return ('cancelado', None)
    if stock == 'invalido':
        print("El stock debe ser un número entero no negativo.\n")
        return ('invalido', None)
    
    # Intentar agregar a la base de datos
    exito = agregar_producto_bd(nombre, tipo, precio, stock, modo_prueba)
    if exito:
        return ('ok', nombre)
    else:
        # Si falló por producto duplicado, lo detectamos aquí
        return ('duplicado', nombre)


def intentar_actualizar_producto(modo_prueba=False):
    """
    Función interactiva para actualizar un producto usando BD
    
    Args:
        modo_prueba (bool): Si True, usa la BD de pruebas
        
    Returns:
        tuple: (resultado, nombre) donde resultado puede ser:
               'ok', 'cancelado', 'vacio', 'invalido', 'no_encontrado'
    """
    nombre_producto = input('Ingrese el nombre del producto que desea actualizar (o "cancelar" para volver al menú): ')
    nombre = validar_nombre(nombre_producto)
    if nombre == "cancelado":
        print("Operación cancelada. Volviendo al menú principal.\n")
        return ('cancelado', None)
    if nombre == "vacio":
        print("No se ingresó ningún producto, por favor intente nuevamente.\n")
        return ('vacio', None)

    print("¿Qué desea actualizar?")
    print("1. Precio")
    print("2. Stock")
    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            nuevo_precio = input("Ingrese el nuevo precio: ")
            precio = validar_precio(nuevo_precio)
            if precio == 'invalido':
                print("El precio debe ser un número positivo.\n")
                return ('invalido', None)
            
            exito = actualizar_producto_bd(nombre, 'precio', precio, modo_prueba)
            if exito:
                return ('ok', nombre)
            else:
                return ('no_encontrado', nombre)
        
        case "2":
            nuevo_stock = input("Ingrese el nuevo stock: ")
            stock = validar_stock(nuevo_stock)
            if stock == 'invalido':
                print("El stock debe ser un número entero no negativo.\n")
                return ('invalido', None)
            
            exito = actualizar_producto_bd(nombre, 'stock', stock, modo_prueba)
            if exito:
                return ('ok', nombre)
            else:
                return ('no_encontrado', nombre)
        
        case _:
            print("Opción inválida. No se realizó ninguna actualización.")
            return ('invalido', None)


def intentar_eliminar_producto(modo_prueba=False):
    """
    Función interactiva para eliminar un producto usando BD
    
    Args:
        modo_prueba (bool): Si True, usa la BD de pruebas
        
    Returns:
        tuple: (resultado, nombre) donde resultado puede ser:
               'ok', 'cancelado', 'vacio', 'no_encontrado'
    """
    # Una sola conexión para todo el flujo
    bd = obtener_conexion_base_datos(modo_prueba)
    if not bd:
        print("❌ Error: No se pudo conectar a la base de datos")
        return ('no_encontrado', None)
    
    try:
        # Verificar si hay productos
        consulta_contar = "SELECT COUNT(*) as total FROM productos"
        resultado = bd.ejecutar_consulta(consulta_contar, obtener_resultados=True)
        
        if not resultado or resultado[0]['total'] == 0:
            print("No hay productos en la base de datos.\n")
            return ('no_encontrado', None)
        
        # Input del usuario
        nombre_producto = input('Ingrese el nombre del producto que desea eliminar (o "cancelar" para volver al menú): ')
        nombre = validar_nombre(nombre_producto)
        
        if nombre == "cancelado":
            print("Operación cancelada. Volviendo al menú principal.\n")
            return ('cancelado', None)
        if nombre == "vacio":
            print("No se ingresó ningún producto, por favor intente nuevamente.\n")
            return ('vacio', None)

        # Confirmación
        confirmacion = input('¿Está seguro que desea eliminar el producto? (s/n): ').strip().lower()
        if confirmacion == 's':
            # Pasar la conexión existente (NO modo_prueba)
            exito = eliminar_producto_bd(nombre, bd)
            if exito:
                return ('ok', nombre)
            else:
                return ('no_encontrado', nombre)
        else:
            print("Operación cancelada.\n")
            return ('cancelado', None)
            
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return ('no_encontrado', None)
    finally:
        bd.desconectar()  # Una sola desconexión al final
