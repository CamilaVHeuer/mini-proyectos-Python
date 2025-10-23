import unittest
import sys
import os

# Agregar el directorio padre al path para importar el módulo
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from productos.validaciones import (validar_nombre, validar_tipo, validar_precio, validar_stock)

class TestValidaciones(unittest.TestCase):
    """
    Tests unitarios para las funciones de validación.
    Estas funciones son puras y no dependen de ningún estado global.
    """

    # Tests para validar_nombre
    def test_validar_nombre_texto_valido(self):
        """Test para validar nombre con texto válido"""
        resultado = validar_nombre("Manzana")
        self.assertEqual(resultado, "manzana")
    
    def test_validar_nombre_texto_con_acentos(self):
        """Test para validar nombre con acentos"""
        resultado = validar_nombre("Limón")
        self.assertEqual(resultado, "limón")
    
    def test_validar_nombre_texto_con_espacios(self):
        """Test para validar nombre con espacios"""
        resultado = validar_nombre("Fruta del Dragón")
        self.assertEqual(resultado, "fruta del dragón")
    
    def test_validar_nombre_texto_mixto(self):
        """Test para validar nombre con mayúsculas y minúsculas"""
        resultado = validar_nombre("PeRa")
        self.assertEqual(resultado, "pera")
    
    def test_validar_nombre_vacio(self):
        """Test para validar nombre vacío"""
        resultado = validar_nombre("")
        self.assertEqual(resultado, "vacio")
    
    def test_validar_nombre_cancelar(self):
        """Test para validar entrada de cancelación"""
        resultado = validar_nombre("cancelar")
        self.assertEqual(resultado, "cancelado")
    
    def test_validar_nombre_cancelar_mayusculas(self):
        """Test para validar entrada de cancelación en mayúsculas"""
        resultado = validar_nombre("CANCELAR")
        self.assertEqual(resultado, "cancelado")
    
    def test_validar_nombre_volver(self):
        """Test para validar entrada de 'volver'"""
        resultado = validar_nombre("volver")
        self.assertEqual(resultado, "cancelado")
    
    def test_validar_nombre_salir(self):
        """Test para validar entrada de 'salir'"""
        resultado = validar_nombre("salir")
        self.assertEqual(resultado, "cancelado")
    
    def test_validar_nombre_numeros(self):
        """Test para validar nombre con números (debe ser inválido)"""
        resultado = validar_nombre("123")
        self.assertEqual(resultado, "invalido")
    
    def test_validar_nombre_caracteres_especiales(self):
        """Test para validar nombre con caracteres especiales (debe ser inválido)"""
        resultado = validar_nombre("Manzana!")
        self.assertEqual(resultado, "invalido")
    
    def test_validar_nombre_con_numeros_mezclados(self):
        """Test para validar nombre con números mezclados"""
        resultado = validar_nombre("Manzana123")
        self.assertEqual(resultado, "invalido")
    
    def test_validar_nombre_sin_permitir_cancelar(self):
        """Test para validar nombre sin permitir cancelación"""
        resultado = validar_nombre("cancelar", permitir_cancelar=False)
        self.assertEqual(resultado, "cancelar")

    # Tests para validar_tipo
    def test_validar_tipo_fruta_minuscula(self):
        """Test para validar tipo 'fruta' en minúsculas"""
        resultado = validar_tipo("fruta")
        self.assertEqual(resultado, "fruta")
    
    def test_validar_tipo_fruta_mayuscula(self):
        """Test para validar tipo 'FRUTA' en mayúsculas"""
        resultado = validar_tipo("FRUTA")
        self.assertEqual(resultado, "fruta")
    
    def test_validar_tipo_verdura_minuscula(self):
        """Test para validar tipo 'verdura' en minúsculas"""
        resultado = validar_tipo("verdura")
        self.assertEqual(resultado, "verdura")
    
    def test_validar_tipo_verdura_mayuscula(self):
        """Test para validar tipo 'VERDURA' en mayúsculas"""
        resultado = validar_tipo("VERDURA")
        self.assertEqual(resultado, "verdura")
    
    def test_validar_tipo_con_espacios(self):
        """Test para validar tipo con espacios"""
        resultado = validar_tipo("  fruta  ")
        self.assertEqual(resultado, "fruta")
    
    def test_validar_tipo_cancelar(self):
        """Test para validar cancelación en tipo"""
        resultado = validar_tipo("cancelar")
        self.assertEqual(resultado, "cancelado")
    
    def test_validar_tipo_volver(self):
        """Test para validar 'volver' en tipo"""
        resultado = validar_tipo("volver")
        self.assertEqual(resultado, "cancelado")
    
    def test_validar_tipo_salir(self):
        """Test para validar 'salir' en tipo"""
        resultado = validar_tipo("salir")
        self.assertEqual(resultado, "cancelado")
    
    def test_validar_tipo_invalido(self):
        """Test para validar tipo inválido"""
        resultado = validar_tipo("cereal")
        self.assertEqual(resultado, "invalido")
    
    def test_validar_tipo_vacio(self):
        """Test para validar tipo vacío"""
        resultado = validar_tipo("")
        self.assertEqual(resultado, "invalido")

    # Tests para validar_precio
    def test_validar_precio_valido_entero(self):
        """Test para validar precio válido entero"""
        resultado = validar_precio("100")
        self.assertEqual(resultado, 100.0)
    
    def test_validar_precio_valido_decimal(self):
        """Test para validar precio válido decimal"""
        resultado = validar_precio("99.50")
        self.assertEqual(resultado, 99.5)
    
    def test_validar_precio_con_espacios(self):
        """Test para validar precio con espacios"""
        resultado = validar_precio("  100.50  ")
        self.assertEqual(resultado, 100.5)
    
    def test_validar_precio_decimal_con_coma(self):
        """Test para validar precio con coma decimal (inválido en Python)"""
        resultado = validar_precio("99,50")
        self.assertEqual(resultado, "invalido")
    
    def test_validar_precio_cancelar(self):
        """Test para validar cancelación en precio"""
        resultado = validar_precio("cancelar")
        self.assertEqual(resultado, "cancelado")
    
    def test_validar_precio_volver(self):
        """Test para validar 'volver' en precio"""
        resultado = validar_precio("volver")
        self.assertEqual(resultado, "cancelado")
    
    def test_validar_precio_salir(self):
        """Test para validar 'salir' en precio"""
        resultado = validar_precio("salir")
        self.assertEqual(resultado, "cancelado")
    
    def test_validar_precio_negativo(self):
        """Test para validar precio negativo (inválido)"""
        resultado = validar_precio("-10")
        self.assertEqual(resultado, "invalido")
    
    def test_validar_precio_cero(self):
        """Test para validar precio cero (inválido)"""
        resultado = validar_precio("0")
        self.assertEqual(resultado, "invalido")
    
    def test_validar_precio_cero_decimal(self):
        """Test para validar precio cero decimal (inválido)"""
        resultado = validar_precio("0.00")
        self.assertEqual(resultado, "invalido")
    
    def test_validar_precio_texto(self):
        """Test para validar precio con texto (inválido)"""
        resultado = validar_precio("abc")
        self.assertEqual(resultado, "invalido")
    
    def test_validar_precio_vacio(self):
        """Test para validar precio vacío"""
        resultado = validar_precio("")
        self.assertEqual(resultado, "invalido")


    # Tests para validar_stock
    def test_validar_stock_valido_positivo(self):
        """Test para validar stock válido positivo"""
        resultado = validar_stock("50")
        self.assertEqual(resultado, 50)
    
    def test_validar_stock_cero(self):
        """Test para validar stock cero (válido)"""
        resultado = validar_stock("0")
        self.assertEqual(resultado, 0)
    
    def test_validar_stock_con_espacios(self):
        """Test para validar stock con espacios"""
        resultado = validar_stock("  50  ")
        self.assertEqual(resultado, 50)
    
    def test_validar_stock_cancelar(self):
        """Test para validar cancelación en stock"""
        resultado = validar_stock("cancelar")
        self.assertEqual(resultado, "cancelado")
    
    def test_validar_stock_volver(self):
        """Test para validar 'volver' en stock"""
        resultado = validar_stock("volver")
        self.assertEqual(resultado, "cancelado")
    
    def test_validar_stock_salir(self):
        """Test para validar 'salir' en stock"""
        resultado = validar_stock("salir")
        self.assertEqual(resultado, "cancelado")
    
    def test_validar_stock_negativo(self):
        """Test para validar stock negativo (inválido)"""
        resultado = validar_stock("-5")
        self.assertEqual(resultado, "invalido")
    
    def test_validar_stock_decimal(self):
        """Test para validar stock decimal (inválido)"""
        resultado = validar_stock("10.5")
        self.assertEqual(resultado, "invalido")
    
    def test_validar_stock_texto(self):
        """Test para validar stock con texto (inválido)"""
        resultado = validar_stock("abc")
        self.assertEqual(resultado, "invalido")
    
    def test_validar_stock_vacio(self):
        """Test para validar stock vacío"""
        resultado = validar_stock("")
        self.assertEqual(resultado, "invalido")
    
    def test_validar_stock_numero_muy_grande(self):
        """Test para validar stock con número muy grande"""
        resultado = validar_stock("999999")
        self.assertEqual(resultado, 999999)

if __name__ == '__main__':
    unittest.main() 