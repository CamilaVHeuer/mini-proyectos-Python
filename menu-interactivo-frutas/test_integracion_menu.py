import unittest
from unittest.mock import patch, call

# Patch para evitar que se ejecute el menú automáticamente al importar
with patch('builtins.input') as mock_input:
    mock_input.return_value = '4'  # Simular salir del menú
    import menu_frutas

class TestIntegracionMenuFrutas(unittest.TestCase):
    
    def setUp(self):
        """Configurar el estado inicial antes de cada test"""
        # Limpiar la lista de frutas antes de cada test
        menu_frutas.frutas.clear()
    
    def tearDown(self):
        """Limpiar después de cada test"""
        # Limpiar la lista de frutas después de cada test
        menu_frutas.frutas.clear()

    @patch('builtins.input', side_effect=[
        '1',           # Agregar fruta
        'Manzana',     # Nombre de la fruta
        '1',           # Agregar otra fruta
        'Banana',      # Nombre de la fruta
        '2',           # Mostrar frutas
        '4'            # Salir
    ])
    @patch('builtins.print')
    def test_flujo_agregar_y_mostrar_frutas(self, mock_print, mock_input):
        """Test de integración: agregar frutas y mostrarlas"""
        menu_frutas.mostrar_menu()
        
        # Verificar que se agregaron las frutas
        self.assertEqual(len(menu_frutas.frutas), 2)
        self.assertIn('Manzana', menu_frutas.frutas)
        self.assertIn('Banana', menu_frutas.frutas)
        
        # Verificar algunas llamadas clave de print
        expected_calls = [
            call("Fruta Manzana agregada con éxito.\n"),
            call("Fruta Banana agregada con éxito.\n"),
            call("Lista de frutas:"),
            call("1. Manzana"),
            call("2. Banana"),
            call("Saliendo del programa...\n")
        ]
        
        for expected_call in expected_calls:
            self.assertIn(expected_call, mock_print.call_args_list)

    @patch('builtins.input', side_effect=[
        '1',           # Agregar fruta
        'Piña',        # Nombre de la fruta
        '1',           # Intentar agregar duplicado
        'Piña',        # Mismo nombre
        '1',           # Agregar otra fruta válida
        'Melón',       # Nombre diferente
        '3',           # Eliminar fruta
        'Piña',        # Fruta a eliminar
        's',           # Confirmar eliminación
        '2',           # Mostrar frutas
        '4'            # Salir
    ])
    @patch('builtins.print')
    def test_flujo_completo_con_duplicados_y_eliminacion(self, mock_print, mock_input):
        """Test de integración: flujo completo con duplicados y eliminación"""
        menu_frutas.mostrar_menu()
        
        # Verificar estado final: solo debe quedar Melón
        self.assertEqual(len(menu_frutas.frutas), 1)
        self.assertIn('Melón', menu_frutas.frutas)
        self.assertNotIn('Piña', menu_frutas.frutas)
        
        # Verificar mensajes clave
        expected_calls = [
            call("Fruta Piña agregada con éxito.\n"),
            call("La fruta ya está en la lista.\n"),
            call("Fruta Melón agregada con éxito.\n"),
            call("Fruta Piña eliminada con éxito.\n"),
            call("Lista de frutas:"),
            call("1. Melón")
        ]
        
        for expected_call in expected_calls:
            self.assertIn(expected_call, mock_print.call_args_list)

    @patch('builtins.input', side_effect=[
        '1',           # Agregar fruta
        'cancelar',    # Cancelar operación
        '1',           # Intentar agregar de nuevo
        'Uva',         # Agregar fruta válida
        '3',           # Eliminar fruta
        'volver',      # Cancelar eliminación
        '2',           # Mostrar frutas
        '4'            # Salir
    ])
    @patch('builtins.print')
    def test_flujo_con_cancelaciones(self, mock_print, mock_input):
        """Test de integración: flujo con cancelaciones"""
        menu_frutas.mostrar_menu()
        
        # Verificar que solo se agregó Uva (cancelar no agregó nada)
        self.assertEqual(len(menu_frutas.frutas), 1)
        self.assertIn('Uva', menu_frutas.frutas)
        
        # Verificar mensajes de cancelación
        expected_calls = [
            call("Operación cancelada. Volviendo al menú principal.\n"),
            call("Fruta Uva agregada con éxito.\n"),
            call("Operación cancelada. Volviendo al menú principal.\n"),
            call("Lista de frutas:"),
            call("1. Uva")
        ]
        
        for expected_call in expected_calls:
            self.assertIn(expected_call, mock_print.call_args_list)

    @patch('builtins.input', side_effect=[
        '1',           # Agregar fruta
        '',            # Entrada vacía
        'Naranja',     # Fruta válida
        '1',           # Agregar otra
        'Kiwi123',     # Fruta con números (inválida)
        'Kiwi',        # Fruta válida
        '2',           # Mostrar frutas
        '4'            # Salir
    ])
    @patch('builtins.print')
    def test_flujo_con_entradas_invalidas(self, mock_print, mock_input):
        """Test de integración: flujo con entradas inválidas"""
        menu_frutas.mostrar_menu()
        
        # Verificar que solo se agregaron las frutas válidas
        self.assertEqual(len(menu_frutas.frutas), 2)
        self.assertIn('Naranja', menu_frutas.frutas)
        self.assertIn('Kiwi', menu_frutas.frutas)
        
        # Verificar mensajes de validación
        expected_calls = [
            call("No se ingresó ninguna fruta, por favor intente nuevamente.\n"),
            call("Fruta Naranja agregada con éxito.\n"),
            call("La fruta debe contener solo letras y espacios, sin números ni caracteres especiales.\n"),
            call("Fruta Kiwi agregada con éxito.\n")
        ]
        
        for expected_call in expected_calls:
            self.assertIn(expected_call, mock_print.call_args_list)

    @patch('builtins.input', side_effect=[
        '3',           # Eliminar fruta (lista vacía)
        '1',           # Agregar fruta
        'Durazno',     # Nombre de la fruta
        '3',           # Eliminar fruta
        'Pera',        # Fruta que no existe
        '3',           # Eliminar fruta
        '',            # Entrada vacía
        'Durazno',     # Fruta existente (continúa en el mismo bucle)
        'n',           # No confirmar eliminación
        '4'            # Salir
    ])
    @patch('builtins.print')
    def test_flujo_eliminacion_casos_edge(self, mock_print, mock_input):
        """Test de integración: casos edge en eliminación"""
        menu_frutas.mostrar_menu()
        
        # Verificar que la fruta sigue ahí (no se eliminó)
        self.assertEqual(len(menu_frutas.frutas), 1)
        self.assertIn('Durazno', menu_frutas.frutas)
        
        # Verificar mensajes de error y cancelación
        expected_calls = [
            call("No hay frutas en la lista.\n"),
            call("Fruta Durazno agregada con éxito.\n"),
            call("La fruta no se encuentra en la lista.\n"),
            call("No se ingresó ninguna fruta, por favor intente nuevamente.\n"),
            call("Operación cancelada.\n")
        ]
        
        for expected_call in expected_calls:
            self.assertIn(expected_call, mock_print.call_args_list)

    @patch('builtins.input', side_effect=[
        '5',           # Opción inválida
        'abc',         # Opción no numérica
        '0',           # Opción fuera de rango
        '1',           # Opción válida
        'Frutilla',    # Agregar fruta
        '4'            # Salir
    ])
    @patch('builtins.print')
    def test_flujo_opciones_menu_invalidas(self, mock_print, mock_input):
        """Test de integración: manejo de opciones inválidas del menú"""
        menu_frutas.mostrar_menu()
        
        # Verificar que se agregó la fruta después de las opciones inválidas
        self.assertEqual(len(menu_frutas.frutas), 1)
        self.assertIn('Frutilla', menu_frutas.frutas)
        
        # Verificar mensajes de error para opciones inválidas
        expected_calls = [
            call("Opción inválida. Por favor, ingrese un número entre 1 y 4.\n"),
            call("Opción inválida. Por favor, ingrese un número entre 1 y 4.\n"),
            call("Opción inválida. Por favor, ingrese un número entre 1 y 4.\n"),
            call("Fruta Frutilla agregada con éxito.\n")
        ]
        
        for expected_call in expected_calls:
            self.assertIn(expected_call, mock_print.call_args_list)

    @patch('builtins.input', side_effect=[
        '1',                    # Agregar fruta
        'banana ecuador',       # Fruta con espacios (válida)
        '1',                    # Agregar otra
        '  PIÑA COLADA  ',     # Mayúsculas con espacios extra
        '2',                    # Mostrar lista
        '4'                     # Salir
    ])
    @patch('builtins.print')
    def test_flujo_normalizacion_texto(self, mock_print, mock_input):
        """Test de integración: normalización de texto con title case"""
        menu_frutas.mostrar_menu()
        
        # Verificar normalización correcta
        self.assertEqual(len(menu_frutas.frutas), 2)
        self.assertIn('Banana Ecuador', menu_frutas.frutas)
        self.assertIn('Piña Colada', menu_frutas.frutas)
        
        # Verificar que se muestran normalizadas
        expected_calls = [
            call("Fruta Banana Ecuador agregada con éxito.\n"),
            call("Fruta Piña Colada agregada con éxito.\n"),
            call("1. Banana Ecuador"),
            call("2. Piña Colada")
        ]
        
        for expected_call in expected_calls:
            self.assertIn(expected_call, mock_print.call_args_list)

if __name__ == '__main__':
    unittest.main()
