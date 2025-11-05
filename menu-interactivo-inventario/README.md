# 🍎 Sistema de Gestión de Inventario

Un sistema completo de gestión de inventario desarrollado en Python que permite administrar productos (frutas y verduras) con **almacenamiento dual** (diccionario en memoria + base de datos MySQL) a través de un menú interactivo de consola. Sistema de Gestión de Inventario

## 🚀 Características

- ✅ **Agregar productos** con validación completa (nombre, tipo, precio, stock)
- 📝 **Actualizar productos** existentes (precio y stock)
- ❌ **Eliminar productos** con confirmación de seguridad
- 📋 **Mostrar inventario** con información detallada
- 🔄 **Validación robusta** con regex para caracteres españoles (ñ, acentos)
- 🛡️ **Manejo de duplicados** automático
- 🚪 **Cancelación de operaciones** con palabras clave
- 💰 **Gestión de precios** con validación numérica
- 📦 **Control de stock** con números enteros
- 🥬 **Categorización** por tipo (frutas/verduras)
- 🧪 **Suite completa de tests** (unitarios e integración)
- 🏗️ **Arquitectura modular** con separación de responsabilidades
- 📦 **Paquetes Python** organizados y reutilizables
- 🎯 **Almacenamiento dual**: Diccionario (memoria) + MySQL (persistente)
- ⚙️ **Configuración flexible** con variables de entorno (.env)

## 📁 Estructura del Proyecto

```
menu-interactivo-inventario/
├── menu_inventario.py              # 📄 Módulo principal del menú interactivo
├── run_menu_inventario.py          # 🚀 Script de ejecución
├── .env.example                    # 📋 Plantilla de configuración
├── productos/                      # 📦 Paquete modular del sistema
│   ├── __init__.py                # 🔧 Configuración del paquete
│   ├── validaciones.py            # ✅ Funciones puras de validación
│   ├── database.py                # 🗄️ Conexión MySQL + estructura de tablas
│   ├── operaciones_diccionario.py # 💾 Operaciones CRUD en memoria
│   └── operaciones_bd.py          # �️ Operaciones CRUD en MySQL
├── tests/                          # 🧪 Suite completa de tests
│   ├── __init__.py                # 📦 Paquete de tests
│   ├── test_validaciones.py       # 🔬 Tests de validaciones (27 tests)
│   ├── test_operaciones_diccionario.py # 💾 Tests backend memoria
│   ├── test_operaciones_bd.py     # 🗃️ Tests backend MySQL
│   └── test_integracion_menu.py   # 🔄 Tests de integración completa
├── sql/                           # 🗄️ Scripts de base de datos
│   └── database_setup.sql         # 📜 Creación de bases de datos
├── setup_database.sh              # 🚀 Script automático de configuración BD
└── README.md                      # 📖 Este archivo
```

## 🛠️ Instalación

### Requisitos

- Python 3.11 o superior
- MySQL 8.0 o superior (para almacenamiento persistente)
- Sistema operativo: Windows, macOS, Linux

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/CamilaVHeuer/mini-proyectos-Python.git

# Navegar al directorio del proyecto
cd mini-proyectos-Python/menu-interactivo-inventario

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus credenciales de MySQL

# Crear archivo de configuración de usuarios MySQL
# IMPORTANTE: Crea sql/security_setup.sql con tus usuarios y contraseñas
# (Este archivo es requerido por setup_database.sh)

# (Opcional) Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install mysql-connector-python python-dotenv

# Configurar base de datos (solo si usarás almacenamiento BD)
chmod +x setup_database.sh
./setup_database.sh

# Alternativa: Configuración manual de BD
# mysql -u root -p < sql/database_setup.sql
# Luego crear usuarios MySQL manualmente
```

## 🎮 Uso

### Configuración del Almacenamiento

El sistema soporta **dos tipos de almacenamiento**:

```bash
# Archivo .env
INVENTARIO_MODO=diccionario  # Almacenamiento en memoria (temporal)
INVENTARIO_MODO=bd          # Almacenamiento en MySQL (persistente)
```

> **Nota:** Para modo `bd` es necesario ejecutar `./setup_database.sh` primero para configurar las bases de datos y usuarios de MySQL.

### Ejecutar la aplicación

```bash
python run_menu_inventario.py
```

### Menú Principal

```
--- Menú de Gestión de Inventario ---
1. ➕ Agregar producto
2. 📋 Mostrar productos
3. ✏️ Actualizar producto
4. ❌ Eliminar producto
5. 🚪 Salir
-----------------------------------
```

### Ejemplos de Uso

#### ✅ Agregar Productos

```
Seleccione una opción del 1 al 5: 1
Ingrese el nombre del producto (o "cancelar" para volver): manzana
Ingrese el tipo de producto (fruta/verdura): fruta
Ingrese el precio del producto: 100.50
Ingrese el stock del producto: 50
✅ Producto 'manzana' agregado con éxito.
```

#### 📋 Mostrar Inventario

```
Seleccione una opción del 1 al 5: 2
Lista de productos:
1. manzana - Tipo: fruta, Precio: $100.50, Stock: 50
2. tomate - Tipo: verdura, Precio: $25.00, Stock: 100
3. lechuga - Tipo: verdura, Precio: $15.00, Stock: 75
```

#### 📝 Actualizar Productos

```
Seleccione una opción del 1 al 5: 3
Ingrese el nombre del producto a actualizar: manzana
¿Qué desea actualizar?
1. Precio
2. Stock
Seleccione una opción: 1
Ingrese el nuevo precio: 120.00
✅ Precio del producto 'manzana' actualizado a 120.0.
```

#### ❌ Eliminar Productos

```
Seleccione una opción del 1 al 5: 4
Ingrese el nombre del producto a eliminar: tomate
¿Está seguro que desea eliminar el producto 'tomate'? (s/n): s
Producto tomate eliminado con éxito.
```

## 🔧 Funcionalidades Avanzadas

### Validación de Entrada

#### Nombres de Productos

- ✅ Acepta caracteres españoles: `ñ`, `á`, `é`, `í`, `ó`, `ú`
- ✅ Permite espacios en nombres: `"fruta del dragón"`
- ❌ Rechaza números: `"manzana123"`
- ❌ Rechaza caracteres especiales: `"piña-colada"`

#### Tipos de Productos

- ✅ Acepta: `"fruta"`, `"verdura"` (case-insensitive)
- ❌ Rechaza cualquier otro tipo: `"cereal"`, `"lacteo"`

#### Precios

- ✅ Acepta números decimales positivos: `100.50`, `25`
- ❌ Rechaza precios negativos o cero: `-10`, `0`
- ❌ Rechaza texto: `"gratis"`, `"abc"`

#### Stock

- ✅ Acepta números enteros no negativos: `50`, `0`, `100`
- ❌ Rechaza números negativos: `-5`
- ❌ Rechaza decimales: `10.5`

### Palabras de Cancelación

Puedes cancelar cualquier operación usando:

- `cancelar`
- `volver`
- `salir`

### Normalización Automática

- `"manzana"` → `"manzana"` (minúsculas)
- `"  TOMATE  "` → `"tomate"` (limpio y minúsculas)
- `"FRUTA"` → `"fruta"` (tipo normalizado)

## 🧪 Testing

El proyecto cuenta con una suite completa de tests unitarios y de integración, que cubre validaciones, operaciones en memoria, operaciones en base de datos y flujos de integración. Esta suite se ejecuta de forma completa en local.

### Ejecución de tests

```bash
# Todos los tests (local)
python -m unittest discover tests -v
```

> **Nota:** Los tests de base de datos e integración requieren tener MySQL y el archivo `.env` configurados correctamente.

### Cobertura de Tests

#### Tests de Validaciones (`test_validaciones.py`)

- ✅ Validación de nombres con caracteres españoles
- ✅ Validación de tipos (fruta/verdura)
- ✅ Validación de precios numéricos
- ✅ Validación de stock entero
- ✅ Casos edge y entradas inválidas
- ✅ **46 tests** de funciones puras sin efectos secundarios

#### Tests de Backend Diccionario (`test_operaciones_diccionario.py`)

- ✅ Operaciones CRUD en memoria (diccionario Python)
- ✅ Manejo de estado temporal del inventario
- ✅ Validación de duplicados en memoria
- ✅ Tests rápidos sin dependencias externas

#### Tests de Backend Base de Datos (`test_operaciones_bd.py`)

- ✅ Operaciones CRUD en MySQL con transacciones
- ✅ Tests en modo aislado (base de datos de prueba)
- ✅ Manejo de concurrencia y consistencia de datos
- ✅ Validación de persistencia entre sesiones

#### Tests de Integración (`test_integracion_menu.py`)

- ✅ Flujos CRUD completos en **ambos backends**
- ✅ Consistencia de comportamiento (diccionario vs MySQL)
- ✅ Tests de casos edge y validación de estados
- ✅ Simulación realista de interacciones de usuario

## 🤖 CI/CD

El proyecto utiliza **GitHub Actions** para integración continua:

```yaml
# ../../.github/workflows/ci.yml (nivel repositorio)
- Ejecuta tests automáticamente en cada Pull Request
- Soporta Python 3.11
- En CI solo se ejecutan tests de validaciones y de backend diccionario
- Los tests de base de datos e integración se ejecutan solo en local
```

## 🏗️ Arquitectura

El proyecto usa **almacenamiento dual** con una arquitectura modular clara:

- **`validaciones.py`** - Funciones puras de validación (sin efectos secundarios)
- **`operaciones_diccionario.py`** - Backend de memoria (rápido, temporal)
- **`operaciones_bd.py`** - Backend MySQL (persistente, transaccional)
- **`database.py`** - Gestión de conexiones y estructura de tablas
- **`menu_inventario.py`** - Selección automática de backend según configuración

**Patrón de conexión única:**

- En el backend MySQL, la conexión a la base de datos se crea una sola vez al inicio del programa o test, y se pasa como argumento a todas las funciones de operaciones.
- Esto permite mayor eficiencia y control, evitando abrir/cerrar conexiones repetidamente.
- Las funciones de operaciones en BD ahora reciben la conexión como primer argumento, por ejemplo:
  ```python
  resultado, nombre = agregar_bd(conexion)
  ```
- En el backend de diccionario, las funciones no requieren argumentos de conexión y operan directamente sobre la estructura en memoria.

**Sistema de Estados:** Las funciones retornan tuplas descriptivas como `('ok', producto)`, `('cancelado', None)`, `('duplicado', producto)`, etc.

## 🧪 Testing

La suite de tests está adaptada al nuevo patrón de conexión:

- En los tests de backend BD e integración, la conexión se crea en el método `setUp` y se cierra en `tearDown`.
- Todas las funciones de operaciones BD reciben la conexión como argumento en los tests.
- Ejemplo:
  ```python
  def setUp(self):
      self.bd_conexion = obtener_conexion_base_datos(modo_prueba=True)
  def tearDown(self):
      self.bd_conexion.desconectar()
  def test_agregar(self):
      resultado, nombre = agregar_bd(self.bd_conexion)
  ```
- Los tests de diccionario siguen funcionando sin argumentos adicionales.

## 👥 Autor

- **Camila V. Heuer**
  - GitHub: [@CamilaVHeuer](https://github.com/CamilaVHeuer)
  - LinkedIn: [Camila V. Heuer](https://www.linkedin.com/in/camilavheuer/)

---

### Enlaces Útiles

- [Documentación de Python unittest](https://docs.python.org/3/library/unittest.html)
- [Regex en Python](https://docs.python.org/3/library/re.html)
- [GitHub Actions](https://docs.github.com/en/actions)

¡Disfruta gestionando tu inventario de productos! 🍎🥬📦
