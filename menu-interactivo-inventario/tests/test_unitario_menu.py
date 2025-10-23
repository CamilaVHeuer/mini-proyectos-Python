import unittest
from unittest.mock import patch
import sys
import os

# Agregar el directorio padre al path para importar el módulo
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import menu_inventario

class TestMenuFrutas(unittest.TestCase):
    
    def setUp(self):
        """Configuración que se ejecuta antes de cada test"""
        # Limpiar el diccionario de productos antes de cada test
        menu_inventario.productos = {}
    
    def tearDown(self):
        """Limpieza que se ejecuta después de cada test"""
        # Limpiar el diccionario de productos después de cada test
        menu_inventario.productos = {}

    # Tests para validar_nombre
    def test_validar_nombre_texto_valido(self):
        """Test para validar nombre con texto válido"""
        resultado = menu_inventario.validar_nombre("Manzana")
        self.assertEqual(resultado, "manzana")
    
    def test_validar_nombre_texto_con_acentos(self):
        """Test para validar nombre con acentos"""
        resultado = menu_inventario.validar_nombre("Limón")
        self.assertEqual(resultado, "limón")
    
    def test_validar_nombre_texto_con_espacios(self):
        """Test para validar nombre con espacios"""
        resultado = menu_inventario.validar_nombre("Fruta del Dragón")
        self.assertEqual(resultado, "fruta del dragón")
    
    def test_validar_nombre_texto_mixto(self):
        """Test para validar nombre con mayúsculas y minúsculas"""
        resultado = menu_inventario.validar_nombre("PeRa")
        self.assertEqual(resultado, "pera")
    
    def test_validar_nombre_vacio(self):
        """Test para validar nombre vacío"""
        resultado = menu_inventario.validar_nombre("")
        self.assertEqual(resultado, "vacio")
    
    def test_validar_nombre_solo_espacios(self):
        """Test para validar nombre con solo espacios"""
        resultado = menu_inventario.validar_nombre("   ")
        self.assertEqual(resultado, "vacio")
    
    def test_validar_nombre_cancelar(self):
        """Test para validar entrada de cancelación"""
        resultado = menu_inventario.validar_nombre("cancelar")
        self.assertEqual(resultado, "cancelado")
    
    def test_validar_nombre_cancelar_mayusculas(self):
        """Test para validar entrada de cancelación en mayúsculas"""
        resultado = menu_inventario.validar_nombre("CANCELAR")
        self.assertEqual(resultado, "cancelado")
    
    def test_validar_nombre_numeros(self):
        """Test para validar nombre con números (debe ser inválido)"""
        resultado = menu_inventario.validar_nombre("123")
        self.assertEqual(resultado, "invalido")
    
    def test_validar_nombre_caracteres_especiales(self):
        """Test para validar nombre con caracteres especiales (debe ser inválido)"""
        resultado = menu_inventario.validar_nombre("Manzana!")
        self.assertEqual(resultado, "invalido")

    # Tests para validar_tipo
    def test_validar_tipo_fruta_minuscula(self):
        """Test para validar tipo 'fruta' en minúsculas"""
        resultado = menu_inventario.validar_tipo("fruta")
        self.assertEqual(resultado, "fruta")
    
    def test_validar_tipo_fruta_mayuscula(self):
        """Test para validar tipo 'FRUTA' en mayúsculas"""
        resultado = menu_inventario.validar_tipo("FRUTA")
        self.assertEqual(resultado, "fruta")
    
    def test_validar_tipo_verdura_minuscula(self):
        """Test para validar tipo 'verdura' en minúsculas"""
        resultado = menu_inventario.validar_tipo("verdura")
        self.assertEqual(resultado, "verdura")
    
    def test_validar_tipo_verdura_mayuscula(self):
        """Test para validar tipo 'VERDURA' en mayúsculas"""
        resultado = menu_inventario.validar_tipo("VERDURA")
        self.assertEqual(resultado, "verdura")
    
    def test_validar_tipo_cancelar(self):
        """Test para validar cancelación en tipo"""
        resultado = menu_inventario.validar_tipo("cancelar")
        self.assertEqual(resultado, "cancelado")
    
    def test_validar_tipo_invalido(self):
        """Test para validar tipo inválido"""
        resultado = menu_inventario.validar_tipo("cereal")
        self.assertEqual(resultado, "invalido")
    
    def test_validar_tipo_vacio(self):
        """Test para validar tipo vacío"""
        resultado = menu_inventario.validar_tipo("")
        self.assertEqual(resultado, "invalido")

    # Tests para validar_precio
    def test_validar_precio_valido_entero(self):
        """Test para validar precio válido entero"""
        resultado = menu_inventario.validar_precio("100")
        self.assertEqual(resultado, 100.0)
    
    def test_validar_precio_valido_decimal(self):
        """Test para validar precio válido decimal"""
        resultado = menu_inventario.validar_precio("99.50")
        self.assertEqual(resultado, 99.5)
    
    def test_validar_precio_cancelar(self):
        """Test para validar cancelación en precio"""
        resultado = menu_inventario.validar_precio("cancelar")
        self.assertEqual(resultado, "cancelado")
    
    def test_validar_precio_negativo(self):
        """Test para validar precio negativo (inválido)"""
        resultado = menu_inventario.validar_precio("-10")
        self.assertEqual(resultado, "invalido")
    
    def test_validar_precio_cero(self):
        """Test para validar precio cero (inválido)"""
        resultado = menu_inventario.validar_precio("0")
        self.assertEqual(resultado, "invalido")
    
    def test_validar_precio_texto(self):
        """Test para validar precio con texto (inválido)"""
        resultado = menu_inventario.validar_precio("abc")
        self.assertEqual(resultado, "invalido")
    
    def test_validar_precio_vacio(self):
        """Test para validar precio vacío"""
        resultado = menu_inventario.validar_precio("")
        self.assertEqual(resultado, "invalido")

    # Tests para validar_stock
    def test_validar_stock_valido_positivo(self):
        """Test para validar stock válido positivo"""
        resultado = menu_inventario.validar_stock("50")
        self.assertEqual(resultado, 50)
    
    def test_validar_stock_cero(self):
        """Test para validar stock cero (válido)"""
        resultado = menu_inventario.validar_stock("0")
        self.assertEqual(resultado, 0)
    
    def test_validar_stock_cancelar(self):
        """Test para validar cancelación en stock"""
        resultado = menu_inventario.validar_stock("cancelar")
        self.assertEqual(resultado, "cancelado")
    
    def test_validar_stock_negativo(self):
        """Test para validar stock negativo (inválido)"""
        resultado = menu_inventario.validar_stock("-5")
        self.assertEqual(resultado, "invalido")
    
    def test_validar_stock_decimal(self):
        """Test para validar stock decimal (inválido)"""
        resultado = menu_inventario.validar_stock("10.5")
        self.assertEqual(resultado, "invalido")
    
    def test_validar_stock_texto(self):
        """Test para validar stock con texto (inválido)"""
        resultado = menu_inventario.validar_stock("abc")
        self.assertEqual(resultado, "invalido")
    
    def test_validar_stock_vacio(self):
        """Test para validar stock vacío"""
        resultado = menu_inventario.validar_stock("")
        self.assertEqual(resultado, "invalido")

    # Tests para intentar_agregar_producto
    @patch('builtins.input', side_effect=['manzana', 'fruta', '100.5', '50'])
    def test_intentar_agregar_producto_exitoso(self, mock_input):
        """Test para agregar un producto nuevo exitosamente"""
        estado, producto = menu_inventario.intentar_agregar_producto()
        self.assertEqual(estado, 'ok')
        self.assertEqual(producto, 'manzana')
        self.assertIn('manzana', menu_inventario.productos)
        self.assertEqual(menu_inventario.productos['manzana']['tipo'], 'fruta')
        self.assertEqual(menu_inventario.productos['manzana']['precio'], 100.5)
        self.assertEqual(menu_inventario.productos['manzana']['stock'], 50)
    
    @patch('builtins.input', side_effect=['tomate', 'verdura', '25', '100'])
    def test_intentar_agregar_producto_verdura(self, mock_input):
        """Test para agregar una verdura exitosamente"""
        estado, producto = menu_inventario.intentar_agregar_producto()
        self.assertEqual(estado, 'ok')
        self.assertEqual(producto, 'tomate')
        self.assertIn('tomate', menu_inventario.productos)
        self.assertEqual(menu_inventario.productos['tomate']['tipo'], 'verdura')
    
    @patch('builtins.input', side_effect=['manzana', 'fruta', '100', '50'])
    def test_intentar_agregar_producto_duplicado(self, mock_input):
        """Test para agregar un producto que ya existe"""
        menu_inventario.productos = {'manzana': {'tipo': 'fruta', 'precio': 80.0, 'stock': 30}}
        estado, producto = menu_inventario.intentar_agregar_producto()
        self.assertEqual(estado, 'duplicado')
        self.assertEqual(producto, 'manzana')
        # Verificar que no se sobrescribió el producto original
        self.assertEqual(menu_inventario.productos['manzana']['precio'], 80.0)
    
    @patch('builtins.input', return_value='cancelar')
    def test_intentar_agregar_producto_cancelar_nombre(self, mock_input):
        """Test para cancelar al ingresar el nombre del producto"""
        estado, producto = menu_inventario.intentar_agregar_producto()
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(producto)
        self.assertEqual(len(menu_inventario.productos), 0)
    
    @patch('builtins.input', return_value='')
    def test_intentar_agregar_producto_nombre_vacio(self, mock_input):
        """Test para entrada vacía al agregar producto"""
        estado, producto = menu_inventario.intentar_agregar_producto()
        self.assertEqual(estado, 'vacio')
        self.assertIsNone(producto)
        self.assertEqual(len(menu_inventario.productos), 0)
    
    @patch('builtins.input', side_effect=['pera', 'cancelar'])
    def test_intentar_agregar_producto_cancelar_tipo(self, mock_input):
        """Test para cancelar al ingresar el tipo del producto"""
        estado, producto = menu_inventario.intentar_agregar_producto()
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(producto)
        self.assertEqual(len(menu_inventario.productos), 0)
    
    @patch('builtins.input', side_effect=['pera', 'cereal'])
    def test_intentar_agregar_producto_tipo_invalido(self, mock_input):
        """Test para tipo de producto inválido"""
        estado, producto = menu_inventario.intentar_agregar_producto()
        self.assertEqual(estado, 'invalido')
        self.assertIsNone(producto)
        self.assertEqual(len(menu_inventario.productos), 0)
    
    @patch('builtins.input', side_effect=['pera', 'fruta', 'cancelar'])
    def test_intentar_agregar_producto_cancelar_precio(self, mock_input):
        """Test para cancelar al ingresar el precio del producto"""
        estado, producto = menu_inventario.intentar_agregar_producto()
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(producto)
        self.assertEqual(len(menu_inventario.productos), 0)
    
    @patch('builtins.input', side_effect=['pera', 'fruta', '-10'])
    def test_intentar_agregar_producto_precio_invalido(self, mock_input):
        """Test para precio inválido"""
        estado, producto = menu_inventario.intentar_agregar_producto()
        self.assertEqual(estado, 'invalido')
        self.assertIsNone(producto)
        self.assertEqual(len(menu_inventario.productos), 0)
    
    @patch('builtins.input', side_effect=['pera', 'fruta', '50', 'cancelar'])
    def test_intentar_agregar_producto_cancelar_stock(self, mock_input):
        """Test para cancelar al ingresar el stock del producto"""
        estado, producto = menu_inventario.intentar_agregar_producto()
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(producto)
        self.assertEqual(len(menu_inventario.productos), 0)
    
    @patch('builtins.input', side_effect=['pera', 'fruta', '50', '-5'])
    def test_intentar_agregar_producto_stock_invalido(self, mock_input):
        """Test para stock inválido"""
        estado, producto = menu_inventario.intentar_agregar_producto()
        self.assertEqual(estado, 'invalido')
        self.assertIsNone(producto)
        self.assertEqual(len(menu_inventario.productos), 0)

    @patch('builtins.print')
    def test_mostrar_productos_con_elementos(self, mock_print):
        """Test para mostrar productos cuando hay elementos en el diccionario"""
        menu_inventario.productos = {
            'manzana': {'tipo': 'fruta', 'precio': 100.0, 'stock': 50},
            'tomate': {'tipo': 'verdura', 'precio': 25.0, 'stock': 100}
        }
        menu_inventario.mostrar_productos()
        
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
    def test_mostrar_productos_diccionario_vacio(self, mock_print):
        """Test para mostrar productos cuando el diccionario está vacío"""
        menu_inventario.mostrar_productos()
        
        # Verificar que se llamó a print
        self.assertTrue(mock_print.called)
        
        # Verificar que se imprimió el mensaje de diccionario vacío
        calls = [str(call) for call in mock_print.call_args_list]
        mensaje_impreso = ''.join(calls)
        self.assertIn('No hay productos', mensaje_impreso)

    # Tests para intentar_actualizar_producto
    @patch('builtins.input', side_effect=['manzana', '1', '150'])
    def test_intentar_actualizar_producto_precio_exitoso(self, mock_input):
        """Test para actualizar precio de producto exitosamente"""
        menu_inventario.productos = {'manzana': {'tipo': 'fruta', 'precio': 100.0, 'stock': 50}}
        estado, producto = menu_inventario.intentar_actualizar_producto()
        self.assertEqual(estado, 'ok')
        self.assertEqual(producto, 'manzana')
        self.assertEqual(menu_inventario.productos['manzana']['precio'], 150.0)
        self.assertEqual(menu_inventario.productos['manzana']['stock'], 50)  # Stock sin cambios
    
    @patch('builtins.input', side_effect=['tomate', '2', '75'])
    def test_intentar_actualizar_producto_stock_exitoso(self, mock_input):
        """Test para actualizar stock de producto exitosamente"""
        menu_inventario.productos = {'tomate': {'tipo': 'verdura', 'precio': 25.0, 'stock': 100}}
        estado, producto = menu_inventario.intentar_actualizar_producto()
        self.assertEqual(estado, 'ok')
        self.assertEqual(producto, 'tomate')
        self.assertEqual(menu_inventario.productos['tomate']['stock'], 75)
        self.assertEqual(menu_inventario.productos['tomate']['precio'], 25.0)  # Precio sin cambios
    
    @patch('builtins.input', return_value='cancelar')
    def test_intentar_actualizar_producto_cancelar_nombre(self, mock_input):
        """Test para cancelar al ingresar nombre del producto a actualizar"""
        menu_inventario.productos = {'manzana': {'tipo': 'fruta', 'precio': 100.0, 'stock': 50}}
        estado, producto = menu_inventario.intentar_actualizar_producto()
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(producto)
        # Verificar que el producto no se modificó
        self.assertEqual(menu_inventario.productos['manzana']['precio'], 100.0)
    
    @patch('builtins.input', return_value='')
    def test_intentar_actualizar_producto_nombre_vacio(self, mock_input):
        """Test para entrada vacía al actualizar producto"""
        menu_inventario.productos = {'manzana': {'tipo': 'fruta', 'precio': 100.0, 'stock': 50}}
        estado, producto = menu_inventario.intentar_actualizar_producto()
        self.assertEqual(estado, 'vacio')
        self.assertIsNone(producto)
    
    @patch('builtins.input', return_value='banana')
    def test_intentar_actualizar_producto_no_encontrado(self, mock_input):
        """Test para actualizar producto que no existe"""
        menu_inventario.productos = {'manzana': {'tipo': 'fruta', 'precio': 100.0, 'stock': 50}}
        estado, producto = menu_inventario.intentar_actualizar_producto()
        self.assertEqual(estado, 'no_encontrado')
        self.assertIsNone(producto)
    
    @patch('builtins.input', side_effect=['manzana', '1', '-50'])
    def test_intentar_actualizar_producto_precio_invalido(self, mock_input):
        """Test para actualizar con precio inválido"""
        menu_inventario.productos = {'manzana': {'tipo': 'fruta', 'precio': 100.0, 'stock': 50}}
        estado, producto = menu_inventario.intentar_actualizar_producto()
        self.assertEqual(estado, 'invalido')
        self.assertIsNone(producto)
        # Verificar que no se modificó el precio original
        self.assertEqual(menu_inventario.productos['manzana']['precio'], 100.0)
    
    @patch('builtins.input', side_effect=['manzana', '2', '-10'])
    def test_intentar_actualizar_producto_stock_invalido(self, mock_input):
        """Test para actualizar con stock inválido"""
        menu_inventario.productos = {'manzana': {'tipo': 'fruta', 'precio': 100.0, 'stock': 50}}
        estado, producto = menu_inventario.intentar_actualizar_producto()
        self.assertEqual(estado, 'invalido')
        self.assertIsNone(producto)
        # Verificar que no se modificó el stock original
        self.assertEqual(menu_inventario.productos['manzana']['stock'], 50)
    
    @patch('builtins.input', side_effect=['manzana', '3'])
    def test_intentar_actualizar_producto_opcion_invalida(self, mock_input):
        """Test para opción de actualización inválida"""
        menu_inventario.productos = {'manzana': {'tipo': 'fruta', 'precio': 100.0, 'stock': 50}}
        estado, producto = menu_inventario.intentar_actualizar_producto()
        self.assertEqual(estado, 'invalido')
        self.assertIsNone(producto)

    # Tests para intentar_eliminar_producto
    @patch('builtins.input', side_effect=['manzana', 's'])
    def test_intentar_eliminar_producto_exitoso(self, mock_input):
        """Test para eliminar un producto exitosamente"""
        menu_inventario.productos = {
            'manzana': {'tipo': 'fruta', 'precio': 100.0, 'stock': 50},
            'tomate': {'tipo': 'verdura', 'precio': 25.0, 'stock': 100}
        }
        estado, producto = menu_inventario.intentar_eliminar_producto()
        self.assertEqual(estado, 'ok')
        self.assertEqual(producto, 'manzana')
        self.assertNotIn('manzana', menu_inventario.productos)
        self.assertIn('tomate', menu_inventario.productos)
    
    @patch('builtins.input', side_effect=['manzana', 'n'])
    def test_intentar_eliminar_producto_cancelar_confirmacion(self, mock_input):
        """Test para cancelar la confirmación de eliminación"""
        menu_inventario.productos = {'manzana': {'tipo': 'fruta', 'precio': 100.0, 'stock': 50}}
        estado, producto = menu_inventario.intentar_eliminar_producto()
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(producto)
        self.assertIn('manzana', menu_inventario.productos)
    
    @patch('builtins.input', return_value='cancelar')
    def test_intentar_eliminar_producto_cancelar_nombre(self, mock_input):
        """Test para cancelar al ingresar nombre del producto a eliminar"""
        menu_inventario.productos = {'manzana': {'tipo': 'fruta', 'precio': 100.0, 'stock': 50}}
        estado, producto = menu_inventario.intentar_eliminar_producto()
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(producto)
        self.assertIn('manzana', menu_inventario.productos)
    
    @patch('builtins.input', return_value='')
    def test_intentar_eliminar_producto_nombre_vacio(self, mock_input):
        """Test para entrada vacía al eliminar producto"""
        menu_inventario.productos = {'manzana': {'tipo': 'fruta', 'precio': 100.0, 'stock': 50}}
        estado, producto = menu_inventario.intentar_eliminar_producto()
        self.assertEqual(estado, 'vacio')
        self.assertIsNone(producto)
        self.assertIn('manzana', menu_inventario.productos)
    
    @patch('builtins.input', return_value='banana')
    def test_intentar_eliminar_producto_no_encontrado(self, mock_input):
        """Test para eliminar producto que no existe"""
        menu_inventario.productos = {'manzana': {'tipo': 'fruta', 'precio': 100.0, 'stock': 50}}
        estado, producto = menu_inventario.intentar_eliminar_producto()
        self.assertEqual(estado, 'no_encontrado')
        self.assertIsNone(producto)
        self.assertIn('manzana', menu_inventario.productos)
    
    def test_intentar_eliminar_producto_diccionario_vacio(self):
        """Test para eliminar producto cuando el diccionario está vacío"""
        estado, producto = menu_inventario.intentar_eliminar_producto()
        self.assertEqual(estado, 'no_encontrado')
        self.assertIsNone(producto)

if __name__ == '__main__':
    unittest.main() 