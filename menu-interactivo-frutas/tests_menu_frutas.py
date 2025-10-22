import unittest
from unittest.mock import patch
import sys
import os
import re

# Agregar el directorio actual al path para importar menu_frutas
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Patch para evitar que se ejecute el menú automáticamente al importar
with patch('builtins.input') as mock_input:
    mock_input.return_value = '4'  # Simular salir del menú
    import menu_frutas

class TestMenuFrutas(unittest.TestCase):
    
    def setUp(self):
        """Configurar el estado inicial antes de cada test"""
        # Limpiar la lista de frutas antes de cada test
        menu_frutas.frutas.clear()
    
    def tearDown(self):
        """Limpiar después de cada test"""
        # Limpiar la lista de frutas después de cada test
        menu_frutas.frutas.clear()

class TestValidarEntrada(TestMenuFrutas):
    
    def test_validar_entrada_texto_valido(self):
        """Test: validar entrada con texto válido"""
        resultado = menu_frutas.validar_entrada("manzana")
        self.assertEqual(resultado, "Manzana")
    
    def test_validar_entrada_con_espacios(self):
        """Test: validar entrada con espacios extra"""
        resultado = menu_frutas.validar_entrada("  banana  ")
        self.assertEqual(resultado, "Banana")
    
    def test_validar_entrada_multiple_palabras(self):
        """Test: validar entrada con múltiples palabras"""
        resultado = menu_frutas.validar_entrada("banana ecuador")
        self.assertEqual(resultado, "Banana Ecuador")
    
    def test_validar_entrada_con_acentos(self):
        """Test: validar entrada con acentos y ñ"""
        resultado = menu_frutas.validar_entrada("piña")
        self.assertEqual(resultado, "Piña")
        
        resultado = menu_frutas.validar_entrada("melón")
        self.assertEqual(resultado, "Melón")
    
    def test_validar_entrada_cancelar(self):
        """Test: validar entrada con palabras de cancelación"""
        self.assertEqual(menu_frutas.validar_entrada("cancelar"), "cancelado")
        self.assertEqual(menu_frutas.validar_entrada("volver"), "cancelado")
        self.assertEqual(menu_frutas.validar_entrada("salir"), "cancelado")
        self.assertEqual(menu_frutas.validar_entrada("CANCELAR"), "cancelado")
    
    def test_validar_entrada_vacia(self):
        """Test: validar entrada vacía"""
        self.assertEqual(menu_frutas.validar_entrada(""), "vacio")
        self.assertEqual(menu_frutas.validar_entrada("   "), "vacio")
    
    def test_validar_entrada_invalida(self):
        """Test: validar entrada con caracteres inválidos"""
        self.assertEqual(menu_frutas.validar_entrada("manzana123"), "invalido")
        self.assertEqual(menu_frutas.validar_entrada("manzana!"), "invalido")
        self.assertEqual(menu_frutas.validar_entrada("piña-colada"), "invalido")
    
    def test_validar_entrada_sin_permitir_cancelar(self):
        """Test: validar entrada sin permitir cancelación"""
        resultado = menu_frutas.validar_entrada("cancelar", permitir_cancelar=False)
        self.assertEqual(resultado, "Cancelar")

class TestIntentarAgregarFruta(TestMenuFrutas):
    
    @patch('builtins.input', return_value='Manzana')
    @patch('builtins.print')
    def test_agregar_fruta_valida(self, mock_print, mock_input):
        """Test: agregar una fruta válida"""
        estado, fruta = menu_frutas.intentar_agregar_fruta()
        
        self.assertEqual(estado, 'ok')
        self.assertEqual(fruta, 'Manzana')
        self.assertIn('Manzana', menu_frutas.frutas)
        self.assertEqual(len(menu_frutas.frutas), 1)
        mock_print.assert_called_with("Fruta Manzana agregada con éxito.\n")
    
    @patch('builtins.input', return_value='')
    @patch('builtins.print')
    def test_agregar_fruta_vacia(self, mock_print, mock_input):
        """Test: intentar agregar una fruta vacía"""
        estado, fruta = menu_frutas.intentar_agregar_fruta()
        
        self.assertEqual(estado, 'vacio')
        self.assertIsNone(fruta)
        self.assertEqual(len(menu_frutas.frutas), 0)
        mock_print.assert_called_with("No se ingresó ninguna fruta, por favor intente nuevamente.\n")
    
    @patch('builtins.input', return_value='   ')
    @patch('builtins.print')
    def test_agregar_fruta_solo_espacios(self, mock_print, mock_input):
        """Test: intentar agregar una fruta que solo contiene espacios"""
        estado, fruta = menu_frutas.intentar_agregar_fruta()
        
        self.assertEqual(estado, 'vacio')
        self.assertIsNone(fruta)
        self.assertEqual(len(menu_frutas.frutas), 0)
        mock_print.assert_called_with("No se ingresó ninguna fruta, por favor intente nuevamente.\n")
    
    @patch('builtins.input', return_value='Manzana')
    @patch('builtins.print')
    def test_agregar_fruta_duplicada(self, mock_print, mock_input):
        """Test: intentar agregar una fruta que ya existe"""
        # Primero agregar una fruta
        menu_frutas.frutas.append('Manzana')
        
        estado, fruta = menu_frutas.intentar_agregar_fruta()
        
        self.assertEqual(estado, 'duplicado')
        self.assertEqual(fruta, 'Manzana')
        self.assertEqual(len(menu_frutas.frutas), 1)  # No debe agregar duplicados
        mock_print.assert_called_with("La fruta ya está en la lista.\n")
    
    @patch('builtins.input', return_value='manzana')
    @patch('builtins.print')
    def test_agregar_fruta_minuscula_title_case(self, mock_print, mock_input):
        """Test: agregar una fruta en minúsculas se convierte a title case automáticamente"""
        estado, fruta = menu_frutas.intentar_agregar_fruta()
        
        self.assertEqual(estado, 'ok')
        self.assertEqual(fruta, 'Manzana')
        self.assertIn('Manzana', menu_frutas.frutas)
        self.assertEqual(len(menu_frutas.frutas), 1)
        mock_print.assert_called_with("Fruta Manzana agregada con éxito.\n")
    
    @patch('builtins.input', return_value='  banana  ')
    @patch('builtins.print')
    def test_agregar_fruta_con_espacios_extra(self, mock_print, mock_input):
        """Test: agregar una fruta con espacios extra se limpia automáticamente"""
        estado, fruta = menu_frutas.intentar_agregar_fruta()
        
        self.assertEqual(estado, 'ok')
        self.assertEqual(fruta, 'Banana')
        self.assertIn('Banana', menu_frutas.frutas)
        self.assertEqual(len(menu_frutas.frutas), 1)
        mock_print.assert_called_with("Fruta Banana agregada con éxito.\n")
    
    @patch('builtins.input', return_value='Manzana123')
    @patch('builtins.print')
    def test_agregar_fruta_con_numeros(self, mock_print, mock_input):
        """Test: rechazar fruta que contiene números"""
        estado, fruta = menu_frutas.intentar_agregar_fruta()
        
        self.assertEqual(estado, 'invalido')
        self.assertIsNone(fruta)
        self.assertEqual(len(menu_frutas.frutas), 0)
        mock_print.assert_called_with("La fruta debe contener solo letras y espacios, sin números ni caracteres especiales.\n")
    
    @patch('builtins.input', return_value='Manzana!')
    @patch('builtins.print')
    def test_agregar_fruta_con_caracteres_especiales(self, mock_print, mock_input):
        """Test: rechazar fruta que contiene caracteres especiales"""
        estado, fruta = menu_frutas.intentar_agregar_fruta()
        
        self.assertEqual(estado, 'invalido')
        self.assertIsNone(fruta)
        self.assertEqual(len(menu_frutas.frutas), 0)
        mock_print.assert_called_with("La fruta debe contener solo letras y espacios, sin números ni caracteres especiales.\n")
    
    @patch('builtins.input', return_value='Piña-colada')
    @patch('builtins.print')
    def test_agregar_fruta_con_guion(self, mock_print, mock_input):
        """Test: rechazar fruta que contiene guión"""
        estado, fruta = menu_frutas.intentar_agregar_fruta()
        
        self.assertEqual(estado, 'invalido')
        self.assertIsNone(fruta)
        self.assertEqual(len(menu_frutas.frutas), 0)
        mock_print.assert_called_with("La fruta debe contener solo letras y espacios, sin números ni caracteres especiales.\n")
    
    @patch('builtins.input', return_value='banana ecuador')
    @patch('builtins.print')
    def test_agregar_fruta_con_espacios_internos_validos(self, mock_print, mock_input):
        """Test: aceptar fruta que contiene espacios internos válidos"""
        estado, fruta = menu_frutas.intentar_agregar_fruta()
        
        self.assertEqual(estado, 'ok')
        self.assertEqual(fruta, 'Banana Ecuador')
        self.assertIn('Banana Ecuador', menu_frutas.frutas)
        self.assertEqual(len(menu_frutas.frutas), 1)
        mock_print.assert_called_with("Fruta Banana Ecuador agregada con éxito.\n")
    
    @patch('builtins.input', return_value='piña')
    @patch('builtins.print')
    def test_agregar_fruta_con_enie(self, mock_print, mock_input):
        """Test: aceptar fruta con ñ"""
        estado, fruta = menu_frutas.intentar_agregar_fruta()
        
        self.assertEqual(estado, 'ok')
        self.assertEqual(fruta, 'Piña')
        self.assertIn('Piña', menu_frutas.frutas)
        self.assertEqual(len(menu_frutas.frutas), 1)
        mock_print.assert_called_with("Fruta Piña agregada con éxito.\n")
    
    @patch('builtins.input', return_value='melón')
    @patch('builtins.print')
    def test_agregar_fruta_con_acento(self, mock_print, mock_input):
        """Test: aceptar fruta con acentos"""
        estado, fruta = menu_frutas.intentar_agregar_fruta()
        
        self.assertEqual(estado, 'ok')
        self.assertEqual(fruta, 'Melón')
        self.assertIn('Melón', menu_frutas.frutas)
        self.assertEqual(len(menu_frutas.frutas), 1)
        mock_print.assert_called_with("Fruta Melón agregada con éxito.\n")
    
    @patch('builtins.input', return_value='cancelar')
    @patch('builtins.print')
    def test_agregar_fruta_cancelar_operacion(self, mock_print, mock_input):
        """Test: cancelar la operación de agregar fruta"""
        estado, fruta = menu_frutas.intentar_agregar_fruta()
        
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(fruta)
        self.assertEqual(len(menu_frutas.frutas), 0)
        mock_print.assert_called_with("Operación cancelada. Volviendo al menú principal.\n")
    
    @patch('builtins.input', return_value='volver')
    @patch('builtins.print')
    def test_agregar_fruta_volver_menu(self, mock_print, mock_input):
        """Test: volver al menú desde agregar fruta"""
        estado, fruta = menu_frutas.intentar_agregar_fruta()
        
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(fruta)
        self.assertEqual(len(menu_frutas.frutas), 0)
        mock_print.assert_called_with("Operación cancelada. Volviendo al menú principal.\n")
    
    @patch('builtins.input', return_value='SALIR')
    @patch('builtins.print')
    def test_agregar_fruta_salir_mayusculas(self, mock_print, mock_input):
        """Test: salir de agregar fruta con texto en mayúsculas"""
        estado, fruta = menu_frutas.intentar_agregar_fruta()
        
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(fruta)
        self.assertEqual(len(menu_frutas.frutas), 0)
        mock_print.assert_called_with("Operación cancelada. Volviendo al menú principal.\n")

class TestIntentarEliminarFruta(TestMenuFrutas):
    
    @patch('builtins.input', side_effect=['Manzana', 's'])
    @patch('builtins.print')
    def test_eliminar_fruta_existente_confirmada(self, mock_print, mock_input):
        """Test: eliminar una fruta existente con confirmación"""
        # Agregar fruta primero
        menu_frutas.frutas.append('Manzana')
        
        estado, fruta = menu_frutas.intentar_eliminar_fruta()
        
        self.assertEqual(estado, 'ok')
        self.assertEqual(fruta, 'Manzana')
        self.assertNotIn('Manzana', menu_frutas.frutas)
        self.assertEqual(len(menu_frutas.frutas), 0)
        mock_print.assert_called_with("Fruta Manzana eliminada con éxito.\n")
    
    @patch('builtins.input', side_effect=['Manzana', 'n'])
    @patch('builtins.print')
    def test_eliminar_fruta_existente_cancelada(self, mock_print, mock_input):
        """Test: cancelar eliminación de fruta existente y volver al menú"""
        # Agregar fruta primero
        menu_frutas.frutas.append('Manzana')
        
        estado, fruta = menu_frutas.intentar_eliminar_fruta()
        
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(fruta)
        self.assertIn('Manzana', menu_frutas.frutas)  # La fruta debe seguir en la lista
        self.assertEqual(len(menu_frutas.frutas), 1)
        mock_print.assert_called_with("Operación cancelada.\n")
    
    @patch('builtins.input', return_value='Banana')
    @patch('builtins.print')
    def test_eliminar_fruta_no_existente(self, mock_print, mock_input):
        """Test: intentar eliminar una fruta que no está en la lista"""
        # Agregar una fruta diferente
        menu_frutas.frutas.append('Manzana')
        
        estado, fruta = menu_frutas.intentar_eliminar_fruta()
        
        self.assertEqual(estado, 'no_encontrado')
        self.assertIsNone(fruta)
        self.assertIn('Manzana', menu_frutas.frutas)  # La fruta original debe seguir
        self.assertEqual(len(menu_frutas.frutas), 1)
        mock_print.assert_called_with("La fruta no se encuentra en la lista.\n")
    
    @patch('builtins.input', return_value='')
    @patch('builtins.print')
    def test_eliminar_fruta_vacia(self, mock_print, mock_input):
        """Test: intentar eliminar con entrada vacía"""
        # Agregar una fruta
        menu_frutas.frutas.append('Manzana')
        
        estado, fruta = menu_frutas.intentar_eliminar_fruta()
        
        self.assertEqual(estado, 'vacio')
        self.assertIsNone(fruta)
        self.assertIn('Manzana', menu_frutas.frutas)  # La fruta debe seguir
        self.assertEqual(len(menu_frutas.frutas), 1)
        mock_print.assert_called_with("No se ingresó ninguna fruta, por favor intente nuevamente.\n")
    
    @patch('builtins.print')
    def test_eliminar_fruta_lista_vacia(self, mock_print):
        """Test: intentar eliminar cuando la lista está vacía"""
        estado = menu_frutas.intentar_eliminar_fruta()
        
        self.assertEqual(estado, 'no_encontrado')
        self.assertEqual(len(menu_frutas.frutas), 0)
        mock_print.assert_called_with("No hay frutas en la lista.\n")
    
    @patch('builtins.input', side_effect=['manzana', 's'])
    @patch('builtins.print')
    def test_eliminar_fruta_minuscula_title_case(self, mock_print, mock_input):
        """Test: eliminar fruta ingresada en minúsculas se convierte a title case"""
        # Agregar fruta en formato title case
        menu_frutas.frutas.append('Manzana')
        
        estado, fruta = menu_frutas.intentar_eliminar_fruta()
        
        self.assertEqual(estado, 'ok')
        self.assertEqual(fruta, 'Manzana')
        self.assertNotIn('Manzana', menu_frutas.frutas)
        self.assertEqual(len(menu_frutas.frutas), 0)
        mock_print.assert_called_with("Fruta Manzana eliminada con éxito.\n")
    
    @patch('builtins.input', side_effect=['  Manzana  ', 's'])
    @patch('builtins.print')
    def test_eliminar_fruta_con_espacios_extra(self, mock_print, mock_input):
        """Test: eliminar fruta con espacios extra"""
        # Agregar fruta
        menu_frutas.frutas.append('Manzana')
        
        estado, fruta = menu_frutas.intentar_eliminar_fruta()
        
        self.assertEqual(estado, 'ok')
        self.assertEqual(fruta, 'Manzana')
        self.assertNotIn('Manzana', menu_frutas.frutas)
        self.assertEqual(len(menu_frutas.frutas), 0)
        mock_print.assert_called_with("Fruta Manzana eliminada con éxito.\n")
    
    @patch('builtins.input', return_value='cancelar')
    @patch('builtins.print')
    def test_eliminar_fruta_cancelar_operacion(self, mock_print, mock_input):
        """Test: cancelar la operación de eliminar fruta"""
        # Agregar una fruta
        menu_frutas.frutas.append('Manzana')
        
        estado, fruta = menu_frutas.intentar_eliminar_fruta()
        
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(fruta)
        self.assertIn('Manzana', menu_frutas.frutas)  # La fruta debe seguir
        self.assertEqual(len(menu_frutas.frutas), 1)
        mock_print.assert_called_with("Operación cancelada. Volviendo al menú principal.\n")
    
    @patch('builtins.input', return_value='volver')
    @patch('builtins.print')
    def test_eliminar_fruta_volver_menu(self, mock_print, mock_input):
        """Test: volver al menú desde eliminar fruta"""
        # Agregar una fruta
        menu_frutas.frutas.append('Manzana')
        
        estado, fruta = menu_frutas.intentar_eliminar_fruta()
        
        self.assertEqual(estado, 'cancelado')
        self.assertIsNone(fruta)
        self.assertIn('Manzana', menu_frutas.frutas)  # La fruta debe seguir
        self.assertEqual(len(menu_frutas.frutas), 1)
        mock_print.assert_called_with("Operación cancelada. Volviendo al menú principal.\n")

class TestMostrarFrutas(TestMenuFrutas):
    
    @patch('builtins.print')
    def test_mostrar_frutas_lista_vacia(self, mock_print):
        """Test: mostrar mensaje cuando la lista está vacía"""
        menu_frutas.mostrar_frutas()
        
        mock_print.assert_called_with("No hay frutas en la lista.\n")
    
    @patch('builtins.print')
    def test_mostrar_frutas_una_fruta(self, mock_print):
        """Test: mostrar lista con una sola fruta"""
        menu_frutas.frutas.append('Manzana')
        
        menu_frutas.mostrar_frutas()
        
        # Verificar todas las llamadas a print
        expected_calls = [
            unittest.mock.call("Lista de frutas:"),
            unittest.mock.call("1. Manzana"),
            unittest.mock.call()  # Línea en blanco
        ]
        mock_print.assert_has_calls(expected_calls)
    
    @patch('builtins.print')
    def test_mostrar_frutas_multiples_frutas(self, mock_print):
        """Test: mostrar lista con múltiples frutas"""
        menu_frutas.frutas.extend(['Manzana', 'Banana', 'Naranja'])
        
        menu_frutas.mostrar_frutas()
        
        # Verificar todas las llamadas a print
        expected_calls = [
            unittest.mock.call("Lista de frutas:"),
            unittest.mock.call("1. Manzana"),
            unittest.mock.call("2. Banana"),
            unittest.mock.call("3. Naranja"),
            unittest.mock.call()  # Línea en blanco
        ]
        mock_print.assert_has_calls(expected_calls)
    
    @patch('builtins.print')
    def test_mostrar_frutas_orden_numerado(self, mock_print):
        """Test: verificar que las frutas se muestren con numeración correcta"""
        frutas_test = ['Pera', 'Uva', 'Frutilla', 'Kiwi', 'Durazno']
        menu_frutas.frutas.extend(frutas_test)
        
        menu_frutas.mostrar_frutas()
        
        # Verificar que se llamó con la cabecera
        mock_print.assert_any_call("Lista de frutas:")
        
        # Verificar que cada fruta se muestre con su número correspondiente
        for i, fruta in enumerate(frutas_test, start=1):
            mock_print.assert_any_call(f"{i}. {fruta}")
        
        # Verificar que se agregue una línea en blanco al final
        mock_print.assert_any_call()

if __name__ == '__main__':
    unittest.main() 