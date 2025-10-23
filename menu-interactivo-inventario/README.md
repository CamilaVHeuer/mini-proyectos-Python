# � Sistema de Gestión de Inventario

Un sistema completo de gestión de inventario desarrollado en Python que permite administrar productos (frutas y verduras) con información detallada de tipo, precio y stock a través de un menú interactivo de consola.

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

## 📁 Estructura del Proyecto

```
menu-interactivo-inventario/
├── menu_inventario.py         # 📄 Módulo principal del menú interactivo
├── run_menu_inventario.py     # 🚀 Script de ejecución
├── productos/                 # 📦 Paquete modular del sistema
│   ├── __init__.py           # 🔧 Configuración del paquete
│   ├── validaciones.py       # ✅ Funciones puras de validación
│   └── operaciones.py        # 🔄 Operaciones CRUD con estado
├── tests/                     # 🧪 Suite completa de tests
│   ├── __init__.py           # 📦 Paquete de tests
│   ├── test_validaciones.py  # 🔬 Tests de validaciones (46 tests)
│   ├── test_operaciones.py   # ⚙️ Tests de operaciones CRUD
│   └── test_integracion_menu.py # 🔄 Tests de integración (7 tests)
├── .github/                   # ⚙️ CI/CD
│   └── workflows/
│       └── ci.yml            # 🤖 GitHub Actions
└── README.md                 # 📖 Este archivo
```

## 🛠️ Instalación

### Requisitos

- Python 3.11 o superior
- Sistema operativo: Windows, macOS, Linux

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/CamilaVHeuer/mini-proyectos-Python.git

# Navegar al directorio del proyecto
cd mini-proyectos-Python/menu-interactivo-inventario

# (Opcional) Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

## 🎮 Uso

### Ejecutar la aplicación

```bash
python run_menu_inventario.py
```

### Menú Principal

```
--- Menú de Gestión de Inventario ---
1. Agregar producto
2. Mostrar productos
3. Actualizar producto
4. Eliminar producto
5. Salir
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

El proyecto incluye una suite completa de tests modularizada con **50+ casos de prueba** organizados por responsabilidades.

### Ejecutar Tests

```bash
# Tests de validaciones (46 tests - funciones puras)
python -m unittest tests.test_validaciones -v

# Tests de operaciones CRUD
python -m unittest tests.test_operaciones -v

# Tests de integración (7 tests - flujo completo)
python -m unittest tests.test_integracion_menu -v

# Todos los tests
python -m unittest discover tests -v

# Con pytest (si está instalado)
pytest tests/ -v
```

### Cobertura de Tests

#### Tests de Validaciones (`test_validaciones.py`)

- ✅ Validación de nombres con caracteres españoles
- ✅ Validación de tipos (fruta/verdura)
- ✅ Validación de precios numéricos
- ✅ Validación de stock entero
- ✅ Casos edge y entradas inválidas
- ✅ **46 tests** de funciones puras sin efectos secundarios

#### Tests de Operaciones (`test_operaciones.py`)

- ✅ Agregar productos (casos válidos e inválidos)
- ✅ Actualizar productos (precio y stock)
- ✅ Eliminar productos (confirmación y cancelación)
- ✅ Mostrar productos (inventario vacío y con elementos)
- ✅ Manejo de duplicados y productos no encontrados
- ✅ Tests con manejo de estado del diccionario `productos`

#### Tests de Integración

- ✅ Flujos completos de usuario
- ✅ Operaciones múltiples en secuencia
- ✅ Manejo de entradas inválidas con retry
- ✅ Cancelaciones en diferentes puntos
- ✅ Casos edge y validación de estados

## 🤖 CI/CD

El proyecto utiliza **GitHub Actions** para integración continua:

```yaml
# .github/workflows/ci.yml
- Ejecuta tests automáticamente en cada Pull Request
- Soporta Python 3.11
- Ejecuta tests unitarios e integración por separado
```

## 🏗️ Arquitectura Modular

### Organización del Código

El proyecto sigue una **arquitectura modular** que separa las responsabilidades:

#### Paquete `productos/`

**`validaciones.py` - Funciones Puras**

```python
# Funciones sin efectos secundarios - fáciles de testear
validar_nombre(entrada)     # Valida nombres con regex español
validar_tipo(entrada)       # Valida tipos fruta/verdura
validar_precio(entrada)     # Valida precios numéricos positivos
validar_stock(entrada)      # Valida stock entero no negativo
```

**`operaciones.py` - Operaciones CRUD**

```python
# Funciones con estado - manejan el diccionario productos
intentar_agregar_producto()     # Lógica completa de agregado
mostrar_productos()             # Visualización del inventario
intentar_actualizar_producto()  # Lógica de actualización
intentar_eliminar_producto()    # Lógica de eliminación
productos = {}                  # Diccionario global del inventario
```

**`__init__.py` - Configuración del Paquete**

```python
# Permite importaciones flexibles:
from productos import validar_nombre, productos
from productos.validaciones import validar_precio
from productos.operaciones import intentar_agregar_producto
```

#### Módulo Principal

**`menu_inventario.py`**

```python
# Importa funciones desde el paquete modular
from productos.operaciones import (
    intentar_agregar_producto,
    mostrar_productos,
    intentar_actualizar_producto,
    intentar_eliminar_producto
)

def mostrar_menu():  # Bucle principal del menú interactivo
```

#### Sistema de Estados

Las funciones retornan tuplas con estados descriptivos:

```python
('ok', producto)        # Operación exitosa
('cancelado', None)     # Usuario canceló
('vacio', None)         # Entrada vacía
('invalido', None)      # Entrada no válida
('duplicado', producto) # Producto ya existe
('no_encontrado', None) # Producto no existe
```

## 👥 Autor

- **Camila V. Heuer** - [@CamilaVHeuer](https://github.com/CamilaVHeuer)

---

### Enlaces Útiles

- [Documentación de Python unittest](https://docs.python.org/3/library/unittest.html)
- [Regex en Python](https://docs.python.org/3/library/re.html)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

¡Disfruta gestionando tu inventario de productos! 🍎🥬📦
