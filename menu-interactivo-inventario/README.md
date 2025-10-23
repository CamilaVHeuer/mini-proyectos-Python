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

## 📁 Estructura del Proyecto

```
menu-interactivo-inventario/
├── menu_inventario.py         # 📄 Lógica principal del sistema de inventario
├── run_menu_inventario.py         # 🚀 Script de ejecución
├── tests/                     # 🧪 Suite de tests
│   ├── __init__.py           # 📦 Paquete Python
│   ├── test_unitario_menu.py   # 🔬 Tests unitarios (60+ tests)
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

El proyecto incluye una suite completa de tests con **67+ casos de prueba**.

### Ejecutar Tests

```bash
# Tests unitarios (60+ tests)
python -m unittest tests.test_unitario_menu -v

# Tests de integración (7 tests)
python -m unittest tests.test_integracion_menu -v

# Todos los tests
python -m unittest discover tests -v

# Con pytest (si está instalado)
pytest tests/ -v
```

### Cobertura de Tests

#### Tests Unitarios

- ✅ Validación de nombres, tipos, precios y stock
- ✅ Agregar productos (casos válidos e inválidos)
- ✅ Actualizar productos (precio y stock)
- ✅ Eliminar productos (confirmación y cancelación)
- ✅ Mostrar productos (inventario vacío y con elementos)
- ✅ Manejo de duplicados y productos no encontrados

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

## 🏗️ Arquitectura

### Componentes Principales

#### `menu_inventario.py`

- `validar_nombre()`: Validación de nombres con regex
- `validar_tipo()`: Validación de tipos (fruta/verdura)
- `validar_precio()`: Validación de precios numéricos
- `validar_stock()`: Validación de stock entero
- `intentar_agregar_producto()`: Lógica completa de agregado
- `intentar_actualizar_producto()`: Lógica de actualización
- `intentar_eliminar_producto()`: Lógica de eliminación
- `mostrar_productos()`: Visualización del inventario
- `mostrar_menu()`: Bucle principal del menú

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

#### Estructura de Datos

```python
productos = {
    'manzana': {
        'tipo': 'fruta',
        'precio': 100.50,
        'stock': 50
    },
    'tomate': {
        'tipo': 'verdura',
        'precio': 25.00,
        'stock': 100
    }
}
```

## 👥 Autor

- **Camila V. Heuer** - [@CamilaVHeuer](https://github.com/CamilaVHeuer)

## 📊 Sobre el Proyecto

- Proyecto desarrollado como parte del aprendizaje de Python
- Implementa mejores prácticas de testing y CI/CD
- Ejemplo de aplicación de gestión de inventario con consola interactiva
- Manejo completo de CRUD (Create, Read, Update, Delete)
- Validación robusta de datos de entrada
- Arquitectura modular y escalable

---

### 📊 Estadísticas del Proyecto

- **Líneas de código**: ~600+
- **Tests**: 67+ casos de prueba
- **Cobertura**: Funcionalidad completa
- **Funciones de validación**: 4 especializadas
- **Operaciones CRUD**: Completas
- **Dependencias**: Solo biblioteca estándar de Python

### 🔗 Enlaces Útiles

- [Documentación de Python unittest](https://docs.python.org/3/library/unittest.html)
- [Regex en Python](https://docs.python.org/3/library/re.html)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

¡Disfruta gestionando tu inventario de productos! 🍎🥬📦
