# ========================================
# SCRIPT DE CONFIGURACIÓN COMPLETA DE BD
# Proyecto: Sistema de Inventario
# ========================================
# 
# COMPATIBILIDAD:
# - XAMPP (Linux/Windows/Mac)
# - MySQL del sistema (systemctl)
# - Detecta automáticamente cuál está corriendo
#
# REQUISITOS:
# - MySQL ejecutándose (XAMPP o sistema)
# - Credenciales de root para crear BD y usuarios
# ========================================

echo "🔧 Configurando base de datos MySQL para inventario..."

# Verificar que MySQL esté corriendo (XAMPP o sistema)
if pgrep -f "mysqld" > /dev/null || systemctl is-active --quiet mysql 2>/dev/null; then
    echo "✅ MySQL está ejecutándose"
else
    echo "❌ MySQL no está ejecutándose. Por favor inicia MySQL primero."
    echo "   Para XAMPP: sudo /opt/lampp/xampp start"
    echo "   Para sistema: sudo systemctl start mysql"
    exit 1
fi

# Detectar qué MySQL usar
MYSQL_CMD="mysql"
if [ -f "/opt/lampp/bin/mysql" ]; then
    MYSQL_CMD="/opt/lampp/bin/mysql"
    echo "🔍 Detectado: MySQL de XAMPP"
elif command -v mysql >/dev/null 2>&1; then
    MYSQL_CMD="mysql"
    echo "🔍 Detectado: MySQL del sistema"
else
    echo "❌ No se encontró comando mysql. Instala MySQL o XAMPP."
    exit 1
fi

# Solicitar credenciales de root
echo "📝 Se necesitan credenciales de root de MySQL para configurar la BD"
echo "    (Se usarán para crear las bases de datos y usuarios)"
read -p "Usuario root de MySQL [root]: " ROOT_USER
ROOT_USER=${ROOT_USER:-root}

echo "🗄️  Ejecutando script de configuración de base de datos..."
echo "    📋 Ingresa la contraseña de ROOT para crear las bases de datos:"
$MYSQL_CMD -u "$ROOT_USER" -p < sql/database_setup.sql

if [ $? -eq 0 ]; then
    echo "✅ Base de datos configurada"
else
    echo "❌ Error configurando base de datos"
    exit 1
fi

echo "🔐 Ejecutando script de configuración de seguridad..."
echo "    👥 Ingresa la MISMA contraseña de ROOT para crear los usuarios:"
$MYSQL_CMD -u "$ROOT_USER" -p < sql/security_setup.sql

if [ $? -eq 0 ]; then
    echo "✅ Usuarios y permisos configurados"
else
    echo "❌ Error configurando seguridad"
    exit 1
fi

echo ""
echo "🎉 ¡Configuración completada exitosamente!"
echo ""
echo "📋 Resumen de configuración:"
echo "   • Base de datos: inventario_db"
echo "   • Base de datos de pruebas: inventario_test_db"
echo "   • Usuario: dev_user"
echo "   • Contraseña: (configurada según .env.example)"
echo ""
echo "🚀 Próximos pasos:"
echo "   1. Verifica que tu archivo .env esté actualizado"
echo "   2. Ejecuta: python productos/database.py"
echo "   3. Ejecuta los tests: python -m unittest discover tests -v"
