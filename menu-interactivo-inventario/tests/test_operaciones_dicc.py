"""
Unit tests para las operaciones de diccionario en memoria.

Este módulo prueba las funciones CRUD que utilizan almacenamiento en memoria:
- Funciones interactivas (con input): intentar_agregar_producto, intentar_actualizar_producto, intentar_eliminar_producto
- Función de visualización: mostrar_productos

Cobertura de testing:
✅ Tests unitarios con mock para funciones interactivas (usando @patch)
✅ Tests de casos edge (diccionario vacío, productos inexistentes, valores inválidos)
✅ Tests de validación de entrada (nombres vacíos, precios/stocks negativos, tipos inválidos)

Tecnologías probadas:
- Almacenamiento en memoria: Diccionario Python puro
- Gestión de estado: setUp/tearDown para aislamiento de tests
- UI Testing: Mock de input() para funciones interactivas
- Validación: Integración con módulo validaciones.py

Características del almacenamiento:
- Independiente de configuraciones externas (.env, base de datos)
- Estado volátil (se pierde al cerrar la aplicación)
- Acceso instantáneo sin latencia de red
- Ideal para desarrollo y testing rápido

Para ejecutar:
    python tests/test_operaciones_dicc.py                    # Con unittest (built-in)
    python -m unittest tests.test_operaciones_dicc -v       # Con unittest desde módulo
"""

import unittest
from unittest.mock import patch
import sys
import os

# Agregar el directorio padre al path para importar el módulo
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from productos.operaciones_diccionario import (
    intentar_agregar_producto, 
    mostrar_productos, 
    intentar_actualizar_producto, 
    intentar_eliminar_producto,
    productos
)

class TestOperacionesDiccionario(unittest.TestCase):
    """Tests para operaciones de diccionario en memoria"""
    
    def setUp(self):
        """Configuración que se ejecuta antes de cada test"""
        # Limpiar el diccionario de productos antes de cada test
        productos.clear()
    
    def tearDown(self):
        """Limpieza que se ejecuta después de cada test"""
        # Limpiar el diccionario de productos después de cada test
        productos.clear()

    # Tests para intentar_agregar_producto
    @patch('builtins.input', side_effect=['manzana', 'fruta', '100.5', '50'])
    def test_01_intentar_agregar_producto_exitoso(self, mock_input):
        """Test para agregar un producto nuevo exitosamente"""
        estado, producto = intentar_agregar_producto()
        self.assertEqual(estado, 'ok')
        self.assertEqual(producto, 'manzana')
        self.assertIn('manzana', productos)
        self.assertEqual(productos['manzana']['tipo'], 'fruta')
        self.assertEqual(productos['manzana']['precio'], 100.5)
        self.assertEqual(productos['manzana']['stock'], 50)
    
    @patch('builtins.input', side_effect=['tomate', 'verdura', '25', '100'])
    def test_02_intentar_agregar_producto_verdura(self, mock_input):
        """Test para agregar una verdura exitosamente"""
        estado, producto = intentar_agregar_producto()
        self.assertEqual(estado, 'ok')
        self.assertEqual(producto, 'tomate')
        self.assertIn('tomate', productos)
        self.assertEqual(productos['tomate']['tipo'], 'verdura')
    
    @patch('builtins.input', side_effect=['manzana', 'fruta', '100', '50'])
    def test_03_intentar_agregar_producto_duplicado(self, mock_input):
        """Test para agregar un producto que ya existe"""
        productos['manzana'] = {'tipo': 'fruta', 'precio': 80.0, 'stock': 30}
        estado, producto = intentar_agregar_producto()
        self.assertEqual(estado, 'duplicado')
        self.assertEqual(producto, 'manzana')
        # Verificar que no se sobrescribió el producto original
        self.assertEqual(productos['manzana']['precio'], 80.0)
    
    @patch('builtins.input', return_value='cancelar')
    def test_04_intentar_agregar_producto_cancelar_nombre(self, mock_input):
        """Test para cancelar al ingresar el nombre del producto"""
        estado, producto = intentar_agregar_producto()
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(producto)
        self.assertEqual(len(productos), 0)
    
    @patch('builtins.input', side_effect=['', 'cancelar'])
    def test_05_intentar_agregar_producto_nombre_vacio(self, mock_input):
        """Test para entrada vacía al agregar producto"""
        estado, producto = intentar_agregar_producto()
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(producto)
        self.assertEqual(len(productos), 0)
    
    @patch('builtins.input', side_effect=['pera', 'cancelar'])
    def test_06_intentar_agregar_producto_cancelar_tipo(self, mock_input):
        """Test para cancelar al ingresar el tipo del producto"""
        estado, producto = intentar_agregar_producto()
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(producto)
        self.assertEqual(len(productos), 0)
    
    @patch('builtins.input', side_effect=['pera', 'cereal', 'cancelar'])
    def test_07_intentar_agregar_producto_tipo_invalido(self, mock_input):
        """Test para tipo de producto inválido"""
        estado, producto = intentar_agregar_producto()
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(producto)
        self.assertEqual(len(productos), 0)
    
    @patch('builtins.input', side_effect=['pera', 'fruta', 'cancelar'])
    def test_08_intentar_agregar_producto_cancelar_precio(self, mock_input):
        """Test para cancelar al ingresar el precio del producto"""
        estado, producto = intentar_agregar_producto()
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(producto)
        self.assertEqual(len(productos), 0)
    
    @patch('builtins.input', side_effect=['pera', 'fruta', '-10', 'cancelar'])
    def test_09_intentar_agregar_producto_precio_invalido(self, mock_input):
        """Test para precio inválido"""
        estado, producto = intentar_agregar_producto()
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(producto)
        self.assertEqual(len(productos), 0)
    
    @patch('builtins.input', side_effect=['pera', 'fruta', '50', '-5', 'cancelar'])
    def test_11_intentar_agregar_producto_stock_invalido(self, mock_input):
        """Test para stock inválido"""
        estado, producto = intentar_agregar_producto()
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(producto)
        self.assertEqual(len(productos), 0)

    @patch('builtins.print')
    def test_12_mostrar_productos_con_elementos(self, mock_print):
        """Test para mostrar productos cuando hay elementos en el diccionario"""
        productos['manzana'] = {'tipo': 'fruta', 'precio': 100.0, 'stock': 50}
        productos['tomate'] = {'tipo': 'verdura', 'precio': 25.0, 'stock': 100}
        mostrar_productos()
        
        # Verificar que se llamó a print
        self.assertTrue(mock_print.called)
        
        # Verificar que se imprimieron los productos
        calls = [str(call) for call in mock_print.call_args_list]
        productos_impresos = ''.join(calls)
        self.assertIn('manzana', productos_impresos)
        self.assertIn('tomate', productos_impresos)
        self.assertIn('fruta', productos_impresos)
        self.assertIn('verdura', productos_impresos)
    
    @patch('builtins.print')
    def test_13_mostrar_productos_diccionario_vacio(self, mock_print):
        """Test para mostrar productos cuando el diccionario está vacío"""
        mostrar_productos()
        
        # Verificar que se llamó a print
        self.assertTrue(mock_print.called)
        
        # Verificar que se imprimió el mensaje de diccionario vacío
        calls = [str(call) for call in mock_print.call_args_list]
        mensaje_impreso = ''.join(calls)
        self.assertIn('No hay productos', mensaje_impreso)

    # Tests para intentar_actualizar_producto
    @patch('builtins.input', side_effect=['manzana', '1', '150'])
    def test_14_intentar_actualizar_producto_precio_exitoso(self, mock_input):
        """Test para actualizar precio de producto exitosamente"""
        productos['manzana'] = {'tipo': 'fruta', 'precio': 100.0, 'stock': 50}
        estado, producto = intentar_actualizar_producto()
        self.assertEqual(estado, 'ok')
        self.assertEqual(producto, 'manzana')
        self.assertEqual(productos['manzana']['precio'], 150.0)
        self.assertEqual(productos['manzana']['stock'], 50)  # Stock sin cambios
    
    @patch('builtins.input', side_effect=['tomate', '2', '75'])
    def test_15_intentar_actualizar_producto_stock_exitoso(self, mock_input):
        """Test para actualizar stock de producto exitosamente"""
        productos['tomate'] = {'tipo': 'verdura', 'precio': 25.0, 'stock': 100}
        estado, producto = intentar_actualizar_producto()
        self.assertEqual(estado, 'ok')
        self.assertEqual(producto, 'tomate')
        self.assertEqual(productos['tomate']['stock'], 75)
        self.assertEqual(productos['tomate']['precio'], 25.0)  # Precio sin cambios
    
    @patch('builtins.input', return_value='cancelar')
    def test_16_intentar_actualizar_producto_cancelar_nombre(self, mock_input):
        """Test para cancelar al ingresar nombre del producto a actualizar"""
        productos['manzana'] = {'tipo': 'fruta', 'precio': 100.0, 'stock': 50}
        estado, producto = intentar_actualizar_producto()
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(producto)
        # Verificar que el producto no se modificó
        self.assertEqual(productos['manzana']['precio'], 100.0)
    
    @patch('builtins.input', side_effect=['', 'cancelar'])
    def test_17_intentar_actualizar_producto_nombre_vacio(self, mock_input):
        """Test para entrada vacía al actualizar producto"""
        productos['manzana'] = {'tipo': 'fruta', 'precio': 100.0, 'stock': 50}
        estado, producto = intentar_actualizar_producto()
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(producto)
    
    @patch('builtins.input', return_value='banana')
    def test_18_intentar_actualizar_producto_no_encontrado(self, mock_input):
        """Test para actualizar producto que no existe"""
        productos['manzana'] = {'tipo': 'fruta', 'precio': 100.0, 'stock': 50}
        estado, producto = intentar_actualizar_producto()
        self.assertEqual(estado, 'no_encontrado')
        self.assertIsNone(producto)
    
    @patch('builtins.input', side_effect=['manzana', '1', '-50', '150'])
    def test_19_intentar_actualizar_producto_precio_invalido(self, mock_input):
        """Test para actualizar con precio inválido y luego valor válido"""
        productos['manzana'] = {'tipo': 'fruta', 'precio': 100.0, 'stock': 50}
        estado, producto = intentar_actualizar_producto()
        self.assertEqual(estado, 'ok')
        self.assertIsNotNone(producto)
        self.assertEqual(productos['manzana']['precio'], 150.0)

    @patch('builtins.input', side_effect=['manzana', '2', '-10', '60'])
    def test_20_intentar_actualizar_producto_stock_invalido(self, mock_input):
        """Test para actualizar con stock inválido y luego valor válido"""
        productos['manzana'] = {'tipo': 'fruta', 'precio': 100.0, 'stock': 50}
        estado, producto = intentar_actualizar_producto()
        self.assertEqual(estado, 'ok')
        self.assertIsNotNone(producto)
        self.assertEqual(productos['manzana']['stock'], 60)

    @patch('builtins.input', side_effect=['manzana', '3', '0', '1', '200'])
    def test_21_intentar_actualizar_producto_opcion_invalida(self, mock_input):
        """Test para opción de actualización inválida y luego válida"""
        productos['manzana'] = {'tipo': 'fruta', 'precio': 100.0, 'stock': 50}
        estado, producto = intentar_actualizar_producto()
        self.assertEqual(estado, 'ok')
        self.assertEqual(producto, 'manzana')
        self.assertEqual(productos['manzana']['precio'], 200.0)
        self.assertEqual(productos['manzana']['stock'], 50)  # Stock sin cambios

    # Tests para intentar_eliminar_producto
    @patch('builtins.input', side_effect=['manzana', 's'])
    def test_22_intentar_eliminar_producto_exitoso(self, mock_input):
        """Test para eliminar un producto exitosamente"""
        productos['manzana'] = {'tipo': 'fruta', 'precio': 100.0, 'stock': 50}
        productos['tomate'] = {'tipo': 'verdura', 'precio': 25.0, 'stock': 100}
        estado, producto = intentar_eliminar_producto()
        self.assertEqual(estado, 'ok')
        self.assertEqual(producto, 'manzana')
        self.assertNotIn('manzana', productos)
        self.assertIn('tomate', productos)
    
    @patch('builtins.input', side_effect=['manzana', 'n'])
    def test_23_intentar_eliminar_producto_cancelar_confirmacion(self, mock_input):
        """Test para cancelar la confirmación de eliminación"""
        productos['manzana'] = {'tipo': 'fruta', 'precio': 100.0, 'stock': 50}
        estado, producto = intentar_eliminar_producto()
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(producto)
        self.assertIn('manzana', productos)
    
    @patch('builtins.input', return_value='cancelar')
    def test_24_intentar_eliminar_producto_cancelar_nombre(self, mock_input):
        """Test para cancelar al ingresar nombre del producto a eliminar"""
        productos['manzana'] = {'tipo': 'fruta', 'precio': 100.0, 'stock': 50}
        estado, producto = intentar_eliminar_producto()
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(producto)
        self.assertIn('manzana', productos)
    
    @patch('builtins.input', side_effect=['', 'cancelar'])
    def test_25_intentar_eliminar_producto_nombre_vacio(self, mock_input):
        """Test para entrada vacía al eliminar producto"""
        productos['manzana'] = {'tipo': 'fruta', 'precio': 100.0, 'stock': 50}
        estado, producto = intentar_eliminar_producto()
        self.assertEqual(estado, 'vacio')
        self.assertIsNone(producto)
        self.assertIn('manzana', productos)
    
    @patch('builtins.input', return_value='banana')
    def test_26_intentar_eliminar_producto_no_encontrado(self, mock_input):
        """Test para eliminar producto que no existe"""
        productos['manzana'] = {'tipo': 'fruta', 'precio': 100.0, 'stock': 50}
        estado, producto = intentar_eliminar_producto()
        self.assertEqual(estado, 'no_encontrado')
        self.assertIsNone(producto)
        self.assertIn('manzana', productos)
    
    def test_27_intentar_eliminar_producto_diccionario_vacio(self):
        """Test para eliminar producto cuando el diccionario está vacío"""
        estado, producto = intentar_eliminar_producto()
        self.assertEqual(estado, 'no_encontrado')
        self.assertIsNone(producto)

if __name__ == '__main__':
    unittest.main()