# 🍎 Menú Interactivo de Frutas

Un sistema de gestión de frutas interactivo desarrollado en Python que permite agregar, eliminar y visualizar una lista de frutas a través de un menú de consola.

## 🚀 Características

- ✅ **Agregar frutas** con validación de entrada
- ❌ **Eliminar frutas** con confirmación de seguridad
- 📋 **Mostrar lista** de frutas numerada
- 🔄 **Validación robusta** con regex para caracteres españoles (ñ, acentos)
- 🛡️ **Manejo de duplicados** automático
- 🚪 **Cancelación de operaciones** con palabras clave
- 🎨 **Normalización de texto** automática (Title Case)
- 🧪 **Suite completa de tests** (unitarios e integración)

## 📁 Estructura del Proyecto

```
menu-interactivo-frutas/
├── menu_frutas.py              # 📄 Lógica principal del menú
├── run_menu_frutas.py         # 🚀 Script de ejecución
├── tests/                     # 🧪 Suite de tests
│   ├── __init__.py           # 📦 Paquete Python
│   ├── test_menu_frutas.py   # 🔬 Tests unitarios (36 tests)
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
cd mini-proyectos-Python/menu-interactivo-frutas

# (Opcional) Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

## 🎮 Uso

### Ejecutar la aplicación

```bash
python run_menu_frutas.py
```

### Menú Principal

```
--- Menú ---
1. Agregar fruta
2. Mostrar frutas
3. Eliminar fruta
4. Salir
---------------
```

### Ejemplos de Uso

#### ✅ Agregar Frutas

```
Seleccione una opción del 1 al 4: 1
Ingrese la fruta que desea agregar (o "cancelar" para volver al menú): manzana
Fruta Manzana agregada con éxito.
```

#### 📋 Mostrar Lista

```
Seleccione una opción del 1 al 4: 2
Lista de frutas:
1. Manzana
2. Banana
3. Piña
```

#### ❌ Eliminar Frutas

```
Seleccione una opción del 1 al 4: 3
Ingrese la fruta que desea eliminar (o "cancelar" para volver al menú): manzana
Está seguro que desea eliminar la fruta? (s/n): s
Fruta Manzana eliminada con éxito.
```

## 🔧 Funcionalidades Avanzadas

### Validación de Entrada

- ✅ Acepta caracteres españoles: `ñ`, `á`, `é`, `í`, `ó`, `ú`
- ✅ Permite espacios en nombres: `"banana ecuador"`
- ❌ Rechaza números: `"manzana123"`
- ❌ Rechaza caracteres especiales: `"piña-colada"`

### Palabras de Cancelación

Puedes cancelar cualquier operación usando:

- `cancelar`
- `volver`
- `salir`

### Normalización Automática

- `"manzana"` → `"Manzana"`
- `"  PIÑA COLADA  "` → `"Piña Colada"`

## 🧪 Testing

El proyecto incluye una suite completa de tests con **43 casos de prueba**.

### Ejecutar Tests

```bash
# Tests unitarios (36 tests)
python -m unittest tests.test_menu_frutas -v

# Tests de integración (7 tests)
python -m unittest tests.test_integracion_menu -v

# Todos los tests
python -m unittest discover tests -v
```

### Cobertura de Tests

- ✅ Validación de entrada
- ✅ Agregar frutas (casos válidos e inválidos)
- ✅ Eliminar frutas (confirmación y cancelación)
- ✅ Mostrar frutas (lista vacía y con elementos)
- ✅ Flujos de integración completos
- ✅ Manejo de errores y casos edge

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

#### `menu_frutas.py`

- `validar_entrada()`: Validación con regex
- `intentar_agregar_fruta()`: Lógica de agregado
- `intentar_eliminar_fruta()`: Lógica de eliminación
- `mostrar_frutas()`: Visualización de lista
- `mostrar_menu()`: Bucle principal del menú

#### Sistema de Estados

Las funciones retornan tuplas con estados descriptivos:

```python
('ok', fruta)           # Operación exitosa
('cancelado', None)     # Usuario canceló
('vacio', None)         # Entrada vacía
('invalido', None)      # Caracteres no válidos
('duplicado', fruta)    # Fruta ya existe
('no_encontrado', None) # Fruta no existe
```

## 👥 Autor

- **Camila V. Heuer** - [@CamilaVHeuer](https://github.com/CamilaVHeuer)

## � Sobre el Proyecto

- Proyecto desarrollado como parte del aprendizaje de Python
- Implementa mejores prácticas de testing y CI/CD
- Ejemplo de aplicación interactiva de consola

---

### 📊 Estadísticas del Proyecto

- **Líneas de código**: ~400
- **Tests**: 43 casos de prueba
- **Cobertura**: Funcionalidad completa
- **Dependencias**: Solo biblioteca estándar de Python

### 🔗 Enlaces Útiles

- [Documentación de Python unittest](https://docs.python.org/3/library/unittest.html)
- [Regex en Python](https://docs.python.org/3/library/re.html)
- [GitHub Actions](https://docs.github.com/en/actions)

¡Disfruta gestionando tu lista de frutas! 🍎🍌🍊
