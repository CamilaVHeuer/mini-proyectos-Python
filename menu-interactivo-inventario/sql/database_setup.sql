-- ========================================
-- SCRIPT DE CONFIGURACIÓN DE BASE DE DATOS
-- Proyecto: Sistema de Inventario
-- ========================================

-- 1. Crear la base de datos principal
CREATE DATABASE IF NOT EXISTS inventario_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 2. Crear la base de datos de pruebas
CREATE DATABASE IF NOT EXISTS inventario_test_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 3. Mostrar bases de datos creadas
SHOW DATABASES LIKE 'inventario%';

-- 4. Mensaje de confirmación
SELECT 'Bases de datos creadas exitosamente' AS mensaje;