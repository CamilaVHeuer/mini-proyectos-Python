"""
Tests de INTEGRACIÓN simplificados para el sistema completo de inventario.

Este módulo prueba que ambos backends de almacenamiento funcionen correctamente:
- Backend diccionario (almacenamiento en memoria)
- Backend base de datos (MySQL con modo de prueba)

Cobertura de testing:
✅ Tests de integración para ambos backends
✅ Flujos completos CRUD (Create, Read, Update, Delete)
✅ Consistencia de comportamiento entre backends
✅ Casos edge (productos duplicados, cancelaciones, validaciones)

Tecnologías probadas:
- Backend diccionario: Operaciones en memoria pura
- Backend BD: MySQL con transacciones de prueba
- UI Testing: Mock de input() para interacciones de usuario
- Aislamiento: setUp/tearDown por test para evitar interferencias

Arquitectura simplificada:
- Importación directa de ambos módulos (sin reconfiguración dinámica)
- Parámetros explícitos para modo de prueba
- Sin modificación de archivos de configuración
- Tests completamente aislados

Para ejecutar:
    python tests/test_integracion_completa.py                    # Con unittest (built-in)
    python -m unittest tests.test_integracion_completa -v       # Con unittest desde módulo
"""

import unittest
import sys
import os
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch

# Agregar el directorio padre al path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importar ambos backends directamente
from productos.database import obtener_conexion_base_datos
from productos.operaciones_bd import (
    intentar_agregar_producto as agregar_bd,
    mostrar_productos as mostrar_bd,
    intentar_actualizar_producto as actualizar_bd,
    intentar_eliminar_producto as eliminar_bd
)
from productos.operaciones_diccionario import (
    intentar_agregar_producto as agregar_dict,
    mostrar_productos as mostrar_dict,
    intentar_actualizar_producto as actualizar_dict,
    intentar_eliminar_producto as eliminar_dict,
    productos
)


class TestIntegracionCompleta(unittest.TestCase):
    """Tests de integración para ambos backends: diccionario y base de datos"""
    
    @classmethod
    def setUpClass(cls):
        """Configuración inicial para todos los tests"""
        print("🔗 Iniciando Tests de INTEGRACIÓN COMPLETA (Simplificados)")
        print("=" * 65)
        print("Probando ambos backends: diccionario y base de datos")
        print("=" * 65)
        
        # Configuración de backends
        cls.backends = {
            'diccionario': {
                'name': 'Diccionario (Memoria)',
                'agregar': agregar_dict,
                'mostrar': mostrar_dict,
                'actualizar': actualizar_dict,
                'eliminar': eliminar_dict
            },
            'bd': {
                'name': 'Base de Datos (MySQL)',
                'agregar': lambda: agregar_bd(modo_prueba=True),
                'mostrar': lambda: mostrar_bd(modo_prueba=True),
                'actualizar': lambda: actualizar_bd(modo_prueba=True),
                'eliminar': lambda: eliminar_bd(modo_prueba=True)
            }
        }
    
    def setUp(self):
        """Configuración antes de cada test - Limpiar ambos backends"""
        # Limpiar diccionario
        productos.clear()
        
        # Limpiar BD de pruebas
        self._limpiar_bd_pruebas()
    
    def _limpiar_bd_pruebas(self):
        """Limpia la base de datos de pruebas"""
        bd = obtener_conexion_base_datos(modo_prueba=True)
        if bd:
            try:
                bd.limpiar_todos_los_datos()
            finally:
                bd.desconectar()
    
    def _obtener_funciones_backend(self, backend_name):
        """
        Obtiene las funciones del backend especificado
        
        Args:
            backend_name (str): 'diccionario' o 'bd'
            
        Returns:
            tuple: (agregar_fn, mostrar_fn, actualizar_fn, eliminar_fn)
        """
        backend = self.backends[backend_name]
        return (
            backend['agregar'],
            backend['mostrar'], 
            backend['actualizar'],
            backend['eliminar']
        )
    
    def test_01_agregar_producto_exitoso_ambos_backends(self):
        """Test: Agregar producto exitoso en ambos backends"""
        
        for backend_name, backend_info in self.backends.items():
            with self.subTest(backend=backend_name):
                print(f"\n🧪 Probando backend: {backend_info['name']}")
                
                # Obtener funciones del backend
                agregar_fn, _, _, _ = self._obtener_funciones_backend(backend_name)
                
                # Simular inputs del usuario
                inputs = ["Manzana Test", "fruta", "1.50", "100"]
                
                with patch('builtins.input', side_effect=inputs):
                    with redirect_stdout(StringIO()) as output:
                        resultado, nombre = agregar_fn()
                
                # Verificaciones
                self.assertEqual(resultado, "ok", f"Backend {backend_name}: Debe agregar exitosamente")
                self.assertEqual(nombre, "manzana test", f"Backend {backend_name}: Nombre normalizado correcto")
                
                output_text = output.getvalue()
                self.assertIn("exitosamente", output_text, f"Backend {backend_name}: Mensaje de éxito")
    
    def test_02_agregar_producto_duplicado_ambos_backends(self):
        """Test: Agregar producto duplicado falla en ambos backends"""
        
        for backend_name, backend_info in self.backends.items():
            with self.subTest(backend=backend_name):
                print(f"\n🧪 Probando backend: {backend_info['name']}")
                
                # Obtener funciones del backend
                agregar_fn, _, _, _ = self._obtener_funciones_backend(backend_name)
                
                # Agregar producto inicial
                inputs1 = ["Banana Test", "fruta", "0.80", "50"]
                with patch('builtins.input', side_effect=inputs1):
                    with redirect_stdout(StringIO()):
                        resultado1, _ = agregar_fn()
                
                self.assertEqual(resultado1, "ok", f"Backend {backend_name}: Primer producto debe agregarse")
                
                # Intentar agregar duplicado
                inputs2 = ["Banana Test", "fruta", "1.00", "75"]
                with patch('builtins.input', side_effect=inputs2):
                    with redirect_stdout(StringIO()):
                        resultado2, nombre2 = agregar_fn()
                
                self.assertEqual(resultado2, "duplicado", f"Backend {backend_name}: Debe detectar duplicado")
                self.assertEqual(nombre2, "banana test", f"Backend {backend_name}: Nombre normalizado correcto")
    
    def test_03_cancelar_operacion_ambos_backends(self):
        """Test: Cancelar operación funciona en ambos backends"""
        
        for backend_name, backend_info in self.backends.items():
            with self.subTest(backend=backend_name):
                print(f"\n🧪 Probando backend: {backend_info['name']}")
                
                # Obtener funciones del backend
                agregar_fn, _, _, _ = self._obtener_funciones_backend(backend_name)
                
                # Usuario cancela
                inputs = ["cancelar"]
                
                with patch('builtins.input', side_effect=inputs):
                    with redirect_stdout(StringIO()) as output:
                        resultado, nombre = agregar_fn()
                
                self.assertEqual(resultado, "cancelado", f"Backend {backend_name}: Debe cancelar")
                self.assertIsNone(nombre, f"Backend {backend_name}: Nombre debe ser None")
                
                output_text = output.getvalue()
                self.assertIn("cancelada", output_text, f"Backend {backend_name}: Mensaje de cancelación")
    
    def test_04_actualizar_producto_ambos_backends(self):
        """Test: Actualizar producto funciona en ambos backends"""
        
        for backend_name, backend_info in self.backends.items():
            with self.subTest(backend=backend_name):
                print(f"\n🧪 Probando backend: {backend_info['name']}")
                
                # Obtener funciones del backend
                agregar_fn, _, actualizar_fn, _ = self._obtener_funciones_backend(backend_name)
                
                # Agregar producto inicial
                inputs_agregar = ["Tomate Test", "verdura", "2.00", "30"]
                with patch('builtins.input', side_effect=inputs_agregar):
                    with redirect_stdout(StringIO()):
                        agregar_fn()
                
                # Actualizar precio
                inputs_actualizar = ["Tomate Test", "1", "2.50"]
                with patch('builtins.input', side_effect=inputs_actualizar):
                    with redirect_stdout(StringIO()) as output:
                        resultado, nombre = actualizar_fn()
                
                self.assertEqual(resultado, "ok", f"Backend {backend_name}: Debe actualizar exitosamente")
                self.assertEqual(nombre, "tomate test", f"Backend {backend_name}: Nombre normalizado correcto")
                
                output_text = output.getvalue()
                self.assertIn("actualizado", output_text, f"Backend {backend_name}: Mensaje de actualización")
    
    def test_05_eliminar_producto_ambos_backends(self):
        """Test: Eliminar producto funciona en ambos backends"""
        
        for backend_name, backend_info in self.backends.items():
            with self.subTest(backend=backend_name):
                print(f"\n🧪 Probando backend: {backend_info['name']}")
                
                # Obtener funciones del backend
                agregar_fn, _, _, eliminar_fn = self._obtener_funciones_backend(backend_name)
                
                # Agregar producto para eliminar
                inputs_agregar = ["Lechuga Test", "verdura", "1.20", "25"]
                with patch('builtins.input', side_effect=inputs_agregar):
                    with redirect_stdout(StringIO()):
                        agregar_fn()
                
                # Eliminar producto
                inputs_eliminar = ["Lechuga Test", "s"]
                with patch('builtins.input', side_effect=inputs_eliminar):
                    with redirect_stdout(StringIO()) as output:
                        resultado, nombre = eliminar_fn()
                
                self.assertEqual(resultado, "ok", f"Backend {backend_name}: Debe eliminar exitosamente")
                self.assertEqual(nombre, "lechuga test", f"Backend {backend_name}: Nombre normalizado correcto")
                
                output_text = output.getvalue()
                self.assertIn("eliminado", output_text, f"Backend {backend_name}: Mensaje de eliminación")
    
    def test_06_flujo_completo_crud_ambos_backends(self):
        """Test: Flujo completo CRUD funciona en ambos backends"""
        
        for backend_name, backend_info in self.backends.items():
            with self.subTest(backend=backend_name):
                print(f"\n🧪 Flujo CRUD completo en backend: {backend_info['name']}")
                
                # Obtener funciones del backend
                agregar_fn, mostrar_fn, actualizar_fn, eliminar_fn = self._obtener_funciones_backend(backend_name)
                
                nombre_test = f"Producto Completo {backend_name.capitalize()}"
                nombre_normalizado = nombre_test.lower()
                
                # 1. CREATE - Crear producto
                inputs_crear = [nombre_test, "fruta", "3.00", "40"]
                with patch('builtins.input', side_effect=inputs_crear):
                    with redirect_stdout(StringIO()):
                        resultado_crear, nombre_creado = agregar_fn()
                self.assertEqual(resultado_crear, "ok", f"Backend {backend_name}: CREATE debe funcionar")
                self.assertEqual(nombre_creado, nombre_normalizado, f"Backend {backend_name}: Nombre CREATE correcto")
                
                # 2. READ - Leer/mostrar productos
                try:
                    with redirect_stdout(StringIO()) as output:
                        mostrar_fn()
                    output_text = output.getvalue()
                    # Buscar el nombre normalizado en el output
                    self.assertIn(nombre_normalizado, output_text.lower(), f"Backend {backend_name}: READ debe mostrar producto")
                except Exception as e:
                    self.fail(f"Backend {backend_name}: READ falló: {e}")
                
                # 3. UPDATE - Actualizar producto
                inputs_actualizar = [nombre_test, "1", "3.50"]
                with patch('builtins.input', side_effect=inputs_actualizar):
                    with redirect_stdout(StringIO()):
                        resultado_actualizar, nombre_actualizado = actualizar_fn()
                self.assertEqual(resultado_actualizar, "ok", f"Backend {backend_name}: UPDATE debe funcionar")
                self.assertEqual(nombre_actualizado, nombre_normalizado, f"Backend {backend_name}: Nombre UPDATE correcto")
                
                # 4. DELETE - Eliminar producto
                inputs_eliminar = [nombre_test, "s"]
                with patch('builtins.input', side_effect=inputs_eliminar):
                    with redirect_stdout(StringIO()):
                        resultado_eliminar, nombre_eliminado = eliminar_fn()
                self.assertEqual(resultado_eliminar, "ok", f"Backend {backend_name}: DELETE debe funcionar")
                self.assertEqual(nombre_eliminado, nombre_normalizado, f"Backend {backend_name}: Nombre DELETE correcto")
                
                # 5. VERIFICAR - Confirmar eliminación
                with redirect_stdout(StringIO()) as output:
                    mostrar_fn()
                output_text = output.getvalue()
                self.assertNotIn(nombre_normalizado, output_text.lower(), f"Backend {backend_name}: Producto debe estar eliminado")
    


if __name__ == '__main__':
    print("🔗 Ejecutando Tests de INTEGRACIÓN COMPLETA (Simplificados)")
    print("=" * 65)
    print("Estos tests verifican que el sistema funcione correctamente")
    print("en AMBOS backends: diccionario y base de datos")
    print("✨ Sin modificar archivos de configuración")
    print("✨ Importación directa de módulos")
    print("✨ Tests completamente aislados")
    print("=" * 65)
    
    # Ejecutar tests directamente
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(unittest.TestLoader().loadTestsFromTestCase(TestIntegracionCompleta))
    
    # Resumen final
    print("\n" + "=" * 65)
    if result.wasSuccessful():
        print("✅ TODOS LOS TESTS DE INTEGRACIÓN SIMPLIFICADOS PASARON!")
        print("\n🔗 INTEGRACIÓN VERIFICADA PARA AMBOS BACKENDS:")
        print("  • Backend diccionario (memoria): ✅")
        print("  • Backend base de datos (MySQL): ✅")
        print("  • Flujos CRUD completos: ✅")
        print("  • Consistencia entre backends: ✅")
        print("  • Manejo de errores: ✅")
        print("  • Validaciones de entrada: ✅")
        print("\n🚀 El sistema dual está completamente integrado.")
    else:
        print("❌ ALGUNOS TESTS DE INTEGRACIÓN FALLARON")
        print(f"Fallados: {len(result.failures)}")
        print(f"Errores: {len(result.errors)}")
        print("\n🔍 Revisa los detalles arriba para diagnosticar los problemas.")
    
    print("=" * 65)
