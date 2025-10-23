import unittest
from unittest.mock import patch, call
import sys
import os

# Agregar el directorio padre al path para importar menu_inventario
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Patch para evitar que se ejecute el menú automáticamente al importar
with patch('builtins.input') as mock_input:
    mock_input.return_value = '5'  # Simular salir del menú
    import menu_inventario

# Importar el diccionario productos desde el módulo correcto
from productos.operaciones import productos

class TestIntegracionMenuInventario(unittest.TestCase):

    def setUp(self):
        """Configurar el estado inicial antes de cada test"""
        # Limpiar el diccionario de productos antes de cada test
        productos.clear()
    
    def tearDown(self):
        """Limpiar después de cada test"""
        # Limpiar el diccionario de productos después de cada test
        productos.clear()

    @patch('builtins.input', side_effect=[
        '1',           # Agregar producto
        'manzana',     # Nombre del producto
        'fruta',       # Tipo del producto
        '100.50',      # Precio
        '50',          # Stock
        '1',           # Agregar otro producto
        'tomate',      # Nombre del producto
        'verdura',     # Tipo del producto
        '25',          # Precio
        '100',         # Stock
        '2',           # Mostrar productos
        '5'            # Salir
    ])
    @patch('builtins.print')
    def test_flujo_agregar_y_mostrar_productos(self, mock_print, mock_input):
        """Test de integración: agregar productos y mostrarlos"""
        menu_inventario.mostrar_menu()
        
        # Verificar que se agregaron los productos
        self.assertEqual(len(productos), 2)
        self.assertIn('manzana', productos)
        self.assertIn('tomate', productos)
        
        # Verificar los datos de los productos
        self.assertEqual(productos['manzana']['tipo'], 'fruta')
        self.assertEqual(productos['manzana']['precio'], 100.5)
        self.assertEqual(productos['manzana']['stock'], 50)
        
        self.assertEqual(productos['tomate']['tipo'], 'verdura')
        self.assertEqual(productos['tomate']['precio'], 25.0)
        self.assertEqual(productos['tomate']['stock'], 100)
        
        # Verificar algunas llamadas clave de print
        expected_messages = [
            "✅ Producto 'manzana' agregado con éxito.",
            "✅ Producto 'tomate' agregado con éxito.",
            "Lista de productos:"
        ]
        
        calls_str = ''.join([str(call) for call in mock_print.call_args_list])
        for message in expected_messages:
            self.assertIn(message, calls_str)

    @patch('builtins.input', side_effect=[
        '1',           # Agregar producto
        'piña',        # Nombre del producto
        'fruta',       # Tipo
        '80',          # Precio
        '25',          # Stock
        '1',           # Intentar agregar duplicado
        'piña',        # Mismo nombre
        '1',           # Agregar otro producto válido
        'lechuga',     # Nombre diferente
        'verdura',     # Tipo
        '15',          # Precio
        '75',          # Stock
        '4',           # Eliminar producto
        'piña',        # Producto a eliminar
        's',           # Confirmar eliminación
        '2',           # Mostrar productos
        '5'            # Salir
    ])
    @patch('builtins.print')
    def test_flujo_completo_con_duplicados_y_eliminacion(self, mock_print, mock_input):
        """Test de integración: flujo completo con duplicados y eliminación"""
        menu_inventario.mostrar_menu()
        
        # Verificar estado final: solo debe quedar lechuga
        self.assertEqual(len(productos), 1)
        self.assertIn('lechuga', productos)
        self.assertNotIn('piña', productos)
        
        # Verificar mensajes clave
        calls_str = ''.join([str(call) for call in mock_print.call_args_list])
        expected_messages = [
            "✅ Producto 'piña' agregado con éxito.",
            "El producto ya está en la lista.",
            "✅ Producto 'lechuga' agregado con éxito.",
            "Producto piña eliminado con éxito."
        ]
        
        for message in expected_messages:
            self.assertIn(message, calls_str)

    @patch('builtins.input', side_effect=[
        '1',           # Agregar producto
        'cancelar',    # Cancelar operación
        '1',           # Intentar agregar de nuevo
        'uva',         # Nombre válido
        'fruta',       # Tipo
        '120',         # Precio
        '30',          # Stock
        '4',           # Eliminar producto
        'cancelar',    # Cancelar eliminación
        '2',           # Mostrar productos
        '5'            # Salir
    ])
    @patch('builtins.print')
    def test_flujo_con_cancelaciones(self, mock_print, mock_input):
        """Test de integración: flujo con cancelaciones"""
        menu_inventario.mostrar_menu()
        
        # Verificar que solo se agregó uva (cancelar no agregó nada)
        self.assertEqual(len(productos), 1)
        self.assertIn('uva', productos)
        
        # Verificar mensajes de cancelación
        calls_str = ''.join([str(call) for call in mock_print.call_args_list])
        expected_messages = [
            "Operación cancelada. Volviendo al menú principal.",
            "✅ Producto 'uva' agregado con éxito.",
            "Lista de productos:"
        ]
        
        for message in expected_messages:
            self.assertIn(message, calls_str)

    @patch('builtins.input', side_effect=[
        '1',           # Agregar producto
        '',            # Entrada vacía para nombre (función retorna 'vacio', bucle reintenta)
        'naranja',     # Nombre válido
        'fruta',       # Tipo válido  
        '90',          # Precio válido
        '40',          # Stock válido (función retorna 'ok', sale del bucle)
        '1',           # Agregar otro producto
        'apio123',     # Nombre con números (función retorna 'invalido', bucle reintenta)
        'apio',        # Nombre válido
        'cereal',      # Tipo inválido (función retorna 'invalido', bucle reintenta)
        'apio',        # Nombre válido (otra vez)
        'verdura',     # Tipo válido
        '-10',         # Precio inválido (función retorna 'invalido', bucle reintenta)
        'apio',        # Nombre válido (otra vez)
        'verdura',     # Tipo válido (otra vez)
        '20',          # Precio válido
        '10.5',        # Stock inválido (función retorna 'invalido', bucle reintenta)
        'apio',        # Nombre válido (otra vez)
        'verdura',     # Tipo válido (otra vez)
        '20',          # Precio válido (otra vez)
        '60',          # Stock válido (función retorna 'ok', sale del bucle)
        '2',           # Mostrar productos
        '5'            # Salir
    ])
    @patch('builtins.print')
    def test_flujo_con_entradas_invalidas(self, mock_print, mock_input):
        """Test de integración: flujo con entradas inválidas"""
        menu_inventario.mostrar_menu()
        
        # Verificar que solo se agregaron los productos válidos
        self.assertEqual(len(productos), 2)
        self.assertIn('naranja', productos)
        self.assertIn('apio', productos)
        
        # Verificar mensajes de validación
        calls_str = ''.join([str(call) for call in mock_print.call_args_list])
        expected_messages = [
            "No se ingresó ningún producto, por favor intente nuevamente.",
            "✅ Producto 'naranja' agregado con éxito.",
            "El producto debe contener solo letras y espacios, sin números ni caracteres especiales.",
            "El tipo de producto debe ser 'fruta' o 'verdura'.",
            "El precio debe ser un número positivo.",
            "El stock debe ser un número entero no negativo.",
            "✅ Producto 'apio' agregado con éxito."
        ]
        
        for message in expected_messages:
            self.assertIn(message, calls_str)

    @patch('builtins.input', side_effect=[
        '3',           # Actualizar producto
        'manzana',     # Producto a actualizar
        '1',           # Actualizar precio
        '150',         # Nuevo precio
        '3',           # Actualizar producto
        'manzana',     # Producto a actualizar
        '2',           # Actualizar stock
        '75',          # Nuevo stock
        '2',           # Mostrar productos
        '5'            # Salir
    ])
    @patch('builtins.print')
    def test_flujo_actualizacion_productos(self, mock_print, mock_input):
        """Test de integración: actualización de productos"""
        # Precargar un producto
        productos['manzana'] = {'tipo': 'fruta', 'precio': 100.0, 'stock': 50}
        
        menu_inventario.mostrar_menu()
        
        # Verificar que se actualizaron los valores
        self.assertEqual(productos['manzana']['precio'], 150.0)
        self.assertEqual(productos['manzana']['stock'], 75)
        
        # Verificar mensajes de actualización
        calls_str = ''.join([str(call) for call in mock_print.call_args_list])
        expected_messages = [
            "✅ Precio del producto 'manzana' actualizado a 150.0.",
            "✅ Stock del producto 'manzana' actualizado a 75."
        ]
        
        for message in expected_messages:
            self.assertIn(message, calls_str)

    @patch('builtins.input', side_effect=[
        '4',           # Eliminar producto (diccionario vacío)
        '1',           # Agregar producto
        'durazno',     # Nombre del producto
        'fruta',       # Tipo
        '70',          # Precio
        '35',          # Stock
        '4',           # Eliminar producto
        'pera',        # Producto que no existe
        '4',           # Eliminar producto
        '',            # Entrada vacía
        'durazno',     # Producto existente (continúa en el mismo bucle)
        'n',           # No confirmar eliminación
        '5'            # Salir
    ])
    @patch('builtins.print')
    def test_flujo_eliminacion_casos_edge(self, mock_print, mock_input):
        """Test de integración: casos edge en eliminación"""
        menu_inventario.mostrar_menu()
        
        # Verificar que el producto sigue ahí (no se eliminó)
        self.assertEqual(len(productos), 1)
        self.assertIn('durazno', productos)
        
        # Verificar mensajes de error y cancelación
        calls_str = ''.join([str(call) for call in mock_print.call_args_list])
        expected_messages = [
            "No hay productos en la lista.",
            "✅ Producto 'durazno' agregado con éxito.",
            "El producto no se encuentra en la lista.",
            "No se ingresó ningún producto, por favor intente nuevamente.",
            "Operación cancelada."
        ]
        
        for message in expected_messages:
            self.assertIn(message, calls_str)

    @patch('builtins.input', side_effect=[
        '6',           # Opción inválida
        'abc',         # Opción no numérica
        '0',           # Opción fuera de rango
        '1',           # Opción válida
        'frutilla',    # Nombre del producto
        'fruta',       # Tipo
        '45',          # Precio
        '80',          # Stock
        '5'            # Salir
    ])
    @patch('builtins.print')
    def test_flujo_opciones_menu_invalidas(self, mock_print, mock_input):
        """Test de integración: manejo de opciones inválidas del menú"""
        menu_inventario.mostrar_menu()
        
        # Verificar que se agregó el producto después de las opciones inválidas
        self.assertEqual(len(productos), 1)
        self.assertIn('frutilla', productos)
        
        # Verificar mensajes de error para opciones inválidas
        calls_str = ''.join([str(call) for call in mock_print.call_args_list])
        expected_messages = [
            "Opción inválida. Por favor, ingrese un número entre 1 y 5.",
            "✅ Producto 'frutilla' agregado con éxito."
        ]
        
        for message in expected_messages:
            self.assertIn(message, calls_str)

if __name__ == '__main__':
    unittest.main()
