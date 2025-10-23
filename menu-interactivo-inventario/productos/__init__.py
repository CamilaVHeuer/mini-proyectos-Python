# Paquete productos - Sistema de Gestión de Inventario
"""
Paquete que contiene los módulos para la gestión de inventario:

- validaciones.py: Funciones puras para validar entradas de usuario
- operaciones.py: Operaciones CRUD para el manejo del inventario
"""

# Importaciones opcionales para facilitar el acceso directo
from .validaciones import validar_nombre, validar_tipo, validar_precio, validar_stock
from .operaciones import (
    intentar_agregar_producto,
    mostrar_productos,
    intentar_actualizar_producto,
    intentar_eliminar_producto,
    productos
)

__all__ = [
    # Funciones de validación
    'validar_nombre',
    'validar_tipo', 
    'validar_precio',
    'validar_stock',
    # Operaciones CRUD
    'intentar_agregar_producto',
    'mostrar_productos',
    'intentar_actualizar_producto',
    'intentar_eliminar_producto',
    # Diccionario de productos
    'productos'
]
