# Paquete productos - Sistema de Gestión de Inventario
"""
Paquete que contiene los módulos para la gestión de inventario:

- validaciones.py: Funciones puras para validar entradas de usuario
- operaciones_diccionario.py: Operaciones CRUD usando diccionario en memoria
- operaciones_bd.py: Operaciones CRUD usando base de datos MySQL
- database.py: Gestión de conexiones a la base de datos

Para usar las funciones, importa directamente desde cada módulo:
    from productos.validaciones import validar_nombre
    from productos.operaciones_diccionario import intentar_agregar_producto
    from productos.operaciones_bd import agregar_producto_bd
"""
