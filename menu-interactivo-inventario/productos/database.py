"""
Módulo para manejo de la base de datos MySQL del inventario.
Contiene la configuración de conexión, creación de tablas y operaciones básicas.
"""

import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class DatabaseConnection:
    """Maneja la conexión y operaciones básicas con MySQL"""
    
    def __init__(self, modo_prueba=False):
        """
        Inicializa la conexión a la base de datos
        
        Args:
            modo_prueba (bool): Si True, usa la base de datos de pruebas
        """
        self.modo_prueba = modo_prueba
        self.conexion = None
        self.cursor = None
        
        # Configuración de la base de datos
        self.configuracion = {
            'host': os.getenv('TEST_DB_HOST', 'localhost') if modo_prueba else os.getenv('DB_HOST', 'localhost'),
            'port': int(os.getenv('TEST_DB_PORT', 3306)) if modo_prueba else int(os.getenv('DB_PORT', 3306)),
            'user': os.getenv('TEST_DB_USER', 'dev_user') if modo_prueba else os.getenv('DB_USER', 'dev_user'),
            'password': os.getenv('TEST_DB_PASSWORD', 'dev_pass') if modo_prueba else os.getenv('DB_PASSWORD', 'dev_pass'),
            'database': os.getenv('TEST_DB_NAME', 'inventario_test_db') if modo_prueba else os.getenv('DB_NAME', 'inventario_db'),
            'charset': 'utf8mb4',
            'collation': 'utf8mb4_unicode_ci'
        }
    
    def conectar(self):
        """Establece la conexión con la base de datos"""
        try:
            self.conexion = mysql.connector.connect(**self.configuracion)
            if self.conexion.is_connected():
                self.cursor = self.conexion.cursor(dictionary=True)
                return True
        except Error as e:
            print(f"❌ Error conectando a MySQL: {e}")
            return False
    
    def desconectar(self):
        """Cierra la conexión con la base de datos"""
        if self.cursor:
            self.cursor.close()
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()
    

    
    def crear_tablas(self):
        """Crea las tablas necesarias para el inventario"""
        try:
            # Tabla productos
            crear_tabla_productos = """
            CREATE TABLE IF NOT EXISTS productos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL UNIQUE,
                tipo ENUM('fruta', 'verdura') NOT NULL,
                precio DECIMAL(10, 2) NOT NULL CHECK (precio > 0),
                stock INT NOT NULL DEFAULT 0 CHECK (stock >= 0),
                fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                INDEX idx_nombre (nombre),
                INDEX idx_tipo (tipo)
            ) ENGINE=InnoDB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci
            """
            
            self.cursor.execute(crear_tabla_productos)
            self.conexion.commit()
            return True
            
        except Error as e:
            print(f"❌ Error creando tablas: {e}")
            return False
    
    def configurar_base_datos(self):
        """Configura completamente la base de datos (conectar y crear tablas)"""
        # Las bases de datos ya existen (creadas por scripts SQL con root)
        
        if not self.conectar():
            return False
        
        if not self.crear_tablas():
            return False
            
        return True
    
    def ejecutar_consulta(self, consulta, parametros=None, obtener_resultados=False):
        """
        Ejecuta una consulta SQL
        
        Args:
            consulta (str): Consulta SQL a ejecutar
            parametros (tuple): Parámetros para la consulta
            obtener_resultados (bool): Si True, retorna los resultados
            
        Returns:
            list|bool: Resultados si obtener_resultados=True, sino bool indicando éxito
        """
        try:
            self.cursor.execute(consulta, parametros or ())
            
            if obtener_resultados:
                return self.cursor.fetchall()
            else:
                self.conexion.commit()
                return True
                
        except Error as e:
            print(f"❌ Error ejecutando consulta: {e}")
            self.conexion.rollback()
            return False if not obtener_resultados else []
    
    def limpiar_todos_los_datos(self):
        """Limpia todos los datos (útil para tests)"""
        if self.modo_prueba:
            try:
                self.cursor.execute("DELETE FROM productos")
                self.conexion.commit()
                print("🧹 Datos de prueba limpiados")
                return True
            except Error as e:
                print(f"❌ Error limpiando datos: {e}")
                return False
        else:
            print("⚠️  No se puede limpiar datos en producción")
            return False


def obtener_conexion_base_datos(modo_prueba=False):
    """
    Función factory para obtener una conexión a la base de datos
    
    Args:
        modo_prueba (bool): Si True, conecta a la BD de pruebas
        
    Returns:
        DatabaseConnection: Instancia de conexión configurada
    """
    bd = DatabaseConnection(modo_prueba=modo_prueba)
    if bd.configurar_base_datos():
        return bd
    else:
        return None


if __name__ == "__main__":
    # Script para configurar la base de datos manualmente
    print("🔧 Configurando base de datos...")
    
    bd = obtener_conexion_base_datos()
    if bd:
        print("✅ Base de datos configurada exitosamente!")
        bd.desconectar()
    else:
        print("❌ Error configurando base de datos")
