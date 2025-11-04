"""
Unit tests para las operaciones de base de datos.

Este módulo prueba las funciones CRUD individuales:
- Funciones core (sin input): agregar_producto_bd, actualizar_producto_bd, eliminar_producto_bd
- Funciones interactivas (con input): intentar_agregar_producto, intentar_actualizar_producto, intentar_eliminar_producto

Cobertura de testing:
✅ Tests unitarios para funciones core (sin mock)
✅ Tests con mock para funciones interactivas (usando @patch)
✅ Tests de casos edge (BD vacía, productos inexistentes, valores inválidos)

Tecnologías probadas:
- Thread-safety: INSERT directo + manejo de constraint UNIQUE
- Optimización: UPDATE/DELETE directo + rowcount verification
- UI Testing: Mock de input() para funciones interactivas

Para ejecutar:
    python tests/test_operaciones_bd.py                    # Con unittest (built-in)
    python -m pytest tests/test_operaciones_bd.py -v      # Con pytest (si está instalado)
    python -m unittest tests.test_operaciones_bd -v       # Con unittest desde módulo
"""

import unittest
from unittest.mock import patch
import sys
import os
from io import StringIO
from contextlib import redirect_stdout

# Agregar el directorio padre al path para poder importar los módulos
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from productos.operaciones_bd import (
    agregar_producto_bd, 
    mostrar_productos, 
    actualizar_producto_bd, 
    eliminar_producto_bd,
    intentar_agregar_producto,
    intentar_actualizar_producto,
    intentar_eliminar_producto
)
from productos.database import obtener_conexion_base_datos

class TestOperacionesBD(unittest.TestCase):
    """Tests para operaciones de base de datos optimizadas"""
    
    def setUp(self):
        """Configuración antes de cada test - limpia la BD de pruebas y crea conexión"""
        self.bd_conexion = obtener_conexion_base_datos(modo_prueba=True)
        assert self.bd_conexion is not None, "No se pudo conectar a la BD de pruebas"
        self.bd_conexion.limpiar_todos_los_datos()
    
    def tearDown(self):
        """Cerrar la conexión después de cada test"""
        if self.bd_conexion:
            self.bd_conexion.desconectar()

    def test_01_agregar_producto_exitoso(self):
        """Test: Agregar un producto nuevo debe ser exitoso"""
        resultado = agregar_producto_bd("Manzana", "fruta", 1.50, 100, self.bd_conexion)
        self.assertTrue(resultado, "Agregar producto nuevo debe ser exitoso")
    
    def test_02_agregar_producto_duplicado(self):
        """Test: Agregar producto duplicado debe fallar (thread-safe)"""
        resultado1 = agregar_producto_bd("Banana", "fruta", 0.80, 50, self.bd_conexion)
        self.assertTrue(resultado1, "Primer producto debe agregarse exitosamente")
        with redirect_stdout(StringIO()):
            resultado2 = agregar_producto_bd("Banana", "fruta", 1.00, 75, self.bd_conexion)
        self.assertFalse(resultado2, "Agregar producto duplicado debe fallar")
    
    def test_03_agregar_multiples_productos(self):
        """Test: Agregar múltiples productos diferentes"""
        productos = [
            ("Tomate", "verdura", 2.00, 30),
            ("Lechuga", "verdura", 1.20, 25),
            ("Pera", "fruta", 1.80, 40)
        ]
        for nombre, tipo, precio, stock in productos:
            with self.subTest(producto=nombre):
                resultado = agregar_producto_bd(nombre, tipo, precio, stock, self.bd_conexion)
                self.assertTrue(resultado, f"Agregar {nombre} debe ser exitoso")
    
    def test_04_actualizar_producto_precio(self):
        """Test: Actualizar precio de producto existente"""
        agregar_producto_bd("Naranja", "fruta", 1.00, 50, self.bd_conexion)
        resultado = actualizar_producto_bd("Naranja", "precio", 1.25, self.bd_conexion)
        self.assertTrue(resultado, "Actualizar precio debe ser exitoso")
    
    def test_05_actualizar_producto_stock(self):
        """Test: Actualizar stock de producto existente"""
        agregar_producto_bd("Limón", "fruta", 0.50, 20, self.bd_conexion)
        resultado = actualizar_producto_bd("Limón", "stock", 35, self.bd_conexion)
        self.assertTrue(resultado, "Actualizar stock debe ser exitoso")
    
    def test_06_actualizar_producto_inexistente(self):
        """Test: Actualizar producto que no existe debe fallar"""
        with redirect_stdout(StringIO()):
            resultado = actualizar_producto_bd("Producto Fantasma", "precio", 5.0, self.bd_conexion)
        self.assertFalse(resultado, "Actualizar producto inexistente debe fallar")
    
    def test_07_actualizar_campo_invalido(self):
        """Test: Actualizar con campo inválido debe fallar"""
        agregar_producto_bd("Apio", "verdura", 1.50, 15, self.bd_conexion)
        with redirect_stdout(StringIO()):
            resultado = actualizar_producto_bd("Apio", "campo_invalido", "valor", self.bd_conexion)
        self.assertFalse(resultado, "Actualizar con campo inválido debe fallar")
    
    def test_08_eliminar_producto_existente(self):
        """Test: Eliminar producto existente debe ser exitoso"""
        agregar_producto_bd("Zanahoria", "verdura", 0.80, 60, self.bd_conexion)
        resultado = eliminar_producto_bd("Zanahoria", self.bd_conexion)
        self.assertTrue(resultado, "Eliminar producto existente debe ser exitoso")
    
    def test_09_eliminar_producto_inexistente(self):
        """Test: Eliminar producto que no existe debe fallar"""
        with redirect_stdout(StringIO()):
            resultado = eliminar_producto_bd("Producto Inexistente", self.bd_conexion)
        self.assertFalse(resultado, "Eliminar producto inexistente debe fallar")
    
    def test_10_mostrar_productos_bd_vacia(self):
        """Test: Mostrar productos en BD vacía no debe fallar"""
        try:
            with redirect_stdout(StringIO()) as output:
                mostrar_productos(self.bd_conexion)
            output_text = output.getvalue()
            self.assertIn("No hay productos", output_text)
        except Exception as e:
            self.fail(f"mostrar_productos no debe fallar con BD vacía: {e}")
    
    def test_11_mostrar_productos_con_datos(self):
        """Test: Mostrar productos con datos en la BD"""
        productos = [
            ("Manzana Verde", "fruta", 1.75, 80),
            ("Espinaca", "verdura", 2.50, 15)
        ]
        for nombre, tipo, precio, stock in productos:
            agregar_producto_bd(nombre, tipo, precio, stock, self.bd_conexion)
        try:
            with redirect_stdout(StringIO()) as output:
                mostrar_productos(self.bd_conexion)
            output_text = output.getvalue()
            self.assertIn("Manzana Verde", output_text)
            self.assertIn("Espinaca", output_text)
        except Exception as e:
            self.fail(f"mostrar_productos no debe fallar con datos: {e}")
    
    @patch('builtins.input', side_effect=['manzana', 'fruta', '1.50', '100'])
    def test_12_intentar_agregar_producto_exitoso(self, mock_input):
        """Test: Agregar producto interactivo exitoso con mock"""
        estado, producto = intentar_agregar_producto(self.bd_conexion)
        self.assertEqual(estado, 'ok')
        self.assertEqual(producto, 'manzana')
    
    @patch('builtins.input', return_value='cancelar')
    def test_13_intentar_agregar_producto_cancelar(self, mock_input):
        """Test: Cancelar al agregar producto interactivo"""
        estado, producto = intentar_agregar_producto(self.bd_conexion)
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(producto)
    
    @patch('builtins.input', return_value='')
    def test_14_intentar_agregar_producto_vacio(self, mock_input):
        """Test: Entrada vacía al agregar producto interactivo"""
        estado, producto = intentar_agregar_producto(self.bd_conexion)
        self.assertEqual(estado, 'vacio')
        self.assertIsNone(producto)
    
    @patch('builtins.input', side_effect=['manzana', 'fruta', '1.50', '100'])
    def test_15_intentar_agregar_producto_duplicado(self, mock_input):
        """Test: Agregar producto duplicado interactivo"""
        agregar_producto_bd("manzana", "fruta", 1.00, 50, self.bd_conexion)
        with redirect_stdout(StringIO()):
            estado, producto = intentar_agregar_producto(self.bd_conexion)
        self.assertEqual(estado, 'duplicado')
        self.assertEqual(producto, 'manzana')
    
    @patch('builtins.input', side_effect=['tomate', '1', '2.50'])
    def test_16_intentar_actualizar_producto_precio_exitoso(self, mock_input):
        """Test: Actualizar precio interactivo exitoso"""
        agregar_producto_bd("tomate", "verdura", 2.00, 30, self.bd_conexion)
        estado, producto = intentar_actualizar_producto(self.bd_conexion)
        self.assertEqual(estado, 'ok')
        self.assertEqual(producto, 'tomate')
    
    @patch('builtins.input', side_effect=['lechuga', '2', '45'])
    def test_17_intentar_actualizar_producto_stock_exitoso(self, mock_input):
        """Test: Actualizar stock interactivo exitoso"""
        agregar_producto_bd("lechuga", "verdura", 1.20, 25, self.bd_conexion)
        estado, producto = intentar_actualizar_producto(self.bd_conexion)
        self.assertEqual(estado, 'ok')
        self.assertEqual(producto, 'lechuga')
    
    @patch('builtins.input', return_value='cancelar')
    def test_18_intentar_actualizar_producto_cancelar_nombre(self, mock_input):
        """Test: Cancelar al ingresar nombre para actualizar"""
        estado, producto = intentar_actualizar_producto(self.bd_conexion)
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(producto)
    
    @patch('builtins.input', return_value='')
    def test_19_intentar_actualizar_producto_nombre_vacio(self, mock_input):
        """Test: Entrada vacía al actualizar producto"""
        estado, producto = intentar_actualizar_producto(self.bd_conexion)
        self.assertEqual(estado, 'vacio')
        self.assertIsNone(producto)
    
    @patch('builtins.input', side_effect=['producto inexistente', '1', '5.00'])
    def test_20_intentar_actualizar_producto_no_encontrado(self, mock_input):
        """Test: Actualizar producto que no existe"""
        with redirect_stdout(StringIO()):
            estado, producto = intentar_actualizar_producto(self.bd_conexion)
        self.assertEqual(estado, 'no_encontrado')
        self.assertEqual(producto, 'producto inexistente')
    
    @patch('builtins.input', side_effect=['pera', '1', '-10'])
    def test_21_intentar_actualizar_producto_precio_invalido(self, mock_input):
        """Test: Actualizar con precio inválido"""
        agregar_producto_bd("pera", "fruta", 1.80, 40, self.bd_conexion)
        estado, producto = intentar_actualizar_producto(self.bd_conexion)
        self.assertEqual(estado, 'invalido')
        self.assertIsNone(producto)
    
    @patch('builtins.input', side_effect=['banana', '2', '-5'])
    def test_22_intentar_actualizar_producto_stock_invalido(self, mock_input):
        """Test: Actualizar con stock inválido"""
        agregar_producto_bd("banana", "fruta", 0.80, 50, self.bd_conexion)
        estado, producto = intentar_actualizar_producto(self.bd_conexion)
        self.assertEqual(estado, 'invalido')
        self.assertIsNone(producto)
    
    @patch('builtins.input', side_effect=['naranja', '3'])
    def test_23_intentar_actualizar_producto_opcion_invalida(self, mock_input):
        """Test: Opción de actualización inválida"""
        agregar_producto_bd("naranja", "fruta", 1.00, 50, self.bd_conexion)
        estado, producto = intentar_actualizar_producto(self.bd_conexion)
        self.assertEqual(estado, 'invalido')
        self.assertIsNone(producto)
    
    @patch('builtins.input', side_effect=['apio', 's'])
    def test_24_intentar_eliminar_producto_exitoso(self, mock_input):
        """Test: Eliminar producto interactivo exitoso"""
        agregar_producto_bd("apio", "verdura", 1.50, 15, self.bd_conexion)
        estado, producto = intentar_eliminar_producto(self.bd_conexion)
        self.assertEqual(estado, 'ok')
        self.assertEqual(producto, 'apio')
    
    @patch('builtins.input', side_effect=['zanahoria', 'n'])
    def test_25_intentar_eliminar_producto_cancelar_confirmacion(self, mock_input):
        """Test: Cancelar confirmación de eliminación"""
        agregar_producto_bd("zanahoria", "verdura", 0.80, 60, self.bd_conexion)
        estado, producto = intentar_eliminar_producto(self.bd_conexion)
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(producto)
    
    @patch('builtins.input', return_value='cancelar')
    def test_26_intentar_eliminar_producto_cancelar_nombre(self, mock_input):
        """Test: Cancelar al ingresar nombre para eliminar"""
        agregar_producto_bd("espinaca", "verdura", 2.50, 15, self.bd_conexion)
        estado, producto = intentar_eliminar_producto(self.bd_conexion)
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(producto)
    
    @patch('builtins.input', return_value='')
    def test_27_intentar_eliminar_producto_nombre_vacio(self, mock_input):
        """Test: Entrada vacía al eliminar producto"""
        agregar_producto_bd("brocoli", "verdura", 3.00, 20, self.bd_conexion)
        estado, producto = intentar_eliminar_producto(self.bd_conexion)
        self.assertEqual(estado, 'vacio')
        self.assertIsNone(producto)

    @patch('builtins.input', side_effect=['producto inexistente', 's'])
    def test_28_intentar_eliminar_producto_no_encontrado(self, mock_input):
        """Test: Eliminar producto que no existe"""
        agregar_producto_bd("producto_real", "fruta", 1.00, 10, self.bd_conexion)
        with redirect_stdout(StringIO()):
            estado, producto = intentar_eliminar_producto(self.bd_conexion)
        self.assertEqual(estado, 'no_encontrado')
        self.assertEqual(producto, 'producto inexistente')
    
    def test_29_intentar_eliminar_producto_bd_vacia(self):
        """Test: Eliminar producto cuando la BD está vacía"""
        estado, producto = intentar_eliminar_producto(self.bd_conexion)
        self.assertEqual(estado, 'no_encontrado')
        self.assertIsNone(producto)

if __name__ == '__main__':
    unittest.main()
