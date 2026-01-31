# 🐍 Mini Proyectos Python - Portfolio de Ingeniería y Desarrollo

Un repositorio completo que combina **ingeniería técnica** con **desarrollo de software**, mostrando soluciones prácticas a problemas reales mediante Python, bases de datos y testing comprehensivo.

## 👩‍💻 Sobre este Portfolio

Este repositorio documenta mi evolución como **Ingeniera-Desarrolladora**, aplicando conocimientos técnicos de ingeniería a través de soluciones de software robustas y bien testeadas. Cada proyecto resuelve problemas del mundo real con enfoque en **calidad**, **testing** y **arquitectura escalable**.

## 🚀 Tecnologías Principales

- **🐍 Python** - Desarrollo backend y lógica de negocio
- **🗄️ MySQL** - Gestión y persistencia de datos con transacciones
- **🧪 Testing** - Suite completa: unitarios, integración y backends múltiples
- **⚙️ CI/CD** - GitHub Actions con tests automáticos por backend
- **🏗️ Arquitectura Dual** - Backends intercambiables (memoria/BD)

## 📋 Proyectos

### 🗂️ [Sistema de Gestión de Inventario](./menu-interactivo-inventario/)

**Estado:** ✅ Completado | **Complejidad:** Intermedia

Un sistema completo de inventario con **almacenamiento dual** (memoria + MySQL) y arquitectura modular que permite gestionar productos con validaciones robustas y operaciones CRUD.

**Características técnicas:**

- � **Almacenamiento dual** - Backend de memoria (temporal) + MySQL (persistente)
- �🏗️ **Arquitectura modular** - Separación clara entre backends y responsabilidades
- 🧪 **90+ tests** - Suite completa: validaciones, diccionario, BD e integración
- 🔄 **Validaciones avanzadas** - Regex para caracteres españoles, manejo de errores
- ⚙️ **Configuración flexible** - Variables de entorno (.env) para múltiples modos
- 🤖 **GitHub Actions** - CI/CD con tests automáticos por backend

**Tecnologías:** Python, MySQL, unittest, python-dotenv, GitHub Actions

```bash
# Ejecutar el proyecto (modo diccionario)
cd menu-interactivo-inventario
cp .env.example .env  # Configurar INVENTARIO_MODO=diccionario
python run_menu_inventario.py

# Ejecutar con MySQL (requiere configuración)
# Editar .env: INVENTARIO_MODO=bd
# ./setup_database.sh  # Configurar BD
# python run_menu_inventario.py

# Ejecutar tests (4 suites: validaciones, diccionario, BD, integración)
python -m unittest discover tests -v
```

---

## 🔮 Próximos Proyectos

### Por descubrir...

El portfolio está en **evolución constante**. Los próximos proyectos dependerán de:

- 🎯 **Necesidades identificadas** - Problemas reales que requieran soluciones técnicas
- 🚀 **Nuevas tecnologías** - Herramientas emergentes que aporten valor
- 🏭 **Aplicaciones de ingeniería** - Oportunidades para combinar conocimiento técnico con desarrollo

**Filosofía:** Calidad sobre cantidad. Cada proyecto debe aportar aprendizaje significativo y demostrar crecimiento técnico.

---

## 🎯 Enfoque y Metodología

### **Calidad del Código**

- ✅ **Testing comprehensivo** - Cobertura completa con tests unitarios e integración
- ✅ **Documentación clara** - READMEs detallados y código autodocumentado
- ✅ **Arquitectura escalable** - Diseño modular que permite crecimiento

### **Aplicación Práctica**

- 🔧 **Problemas reales** - Cada proyecto resuelve necesidades del mundo real
- 🏭 **Perspectiva de ingeniería** - Aplicación de conocimientos técnicos especializados
- 📊 **Gestión de datos** - Focus en manejo eficiente y seguro de información

### **Evolución Técnica**

- 📈 **Complejidad creciente** - Proyectos que escalan en sofisticación técnica
- 🔄 **Iteración continua** - Mejoras y refactorización basada en aprendizajes
- 🚀 **Tecnologías emergentes** - Adopción progresiva de herramientas avanzadas

---

## 🛠️ Cómo Explorar este Portfolio

### **Para Reclutadores:**

1. **Revisa el [Sistema de Inventario](./menu-interactivo-inventario/)** - Proyecto más completo
2. **Examina la arquitectura modular** - Demuestra capacidad de diseño
3. **Revisa los tests** - Muestra compromiso con la calidad
4. **Observa el CI/CD** - Conocimiento de mejores prácticas

### **Para Desarrolladores:**

1. **Clona el repositorio** y ejecuta los proyectos localmente
2. **Revisa la estructura** de cada proyecto para ver patrones
3. **Ejecuta los tests** para entender la cobertura
4. **Estudia la documentación** para ver el proceso de pensamiento

### **Para Estudiantes:**

1. **Sigue la evolución** de los commits para ver el proceso
2. **Aprende de la organización** modular del código
3. **Estudia los tests** para entender testing en Python
4. **Observa las mejores prácticas** aplicadas

---

## 📊 Estadísticas del Portfolio

- **Proyectos completados:** 1
- **Tests totales:** 50+
- **Líneas de código:** 600+
- **Tecnologías dominadas:** Python, MySQL, Testing, CI/CD, Arquitecturas Duales
- **Cobertura de tests:** Completa en todos los proyectos

---

## 🧪 Testing y CI/CD

- En GitHub Actions (CI) **solo se ejecutan automáticamente los tests de validaciones y de operaciones con diccionario** (memoria), para garantizar compatibilidad multiplataforma y evitar dependencias externas.
- Los tests de base de datos y de integración **deben ejecutarse localmente**, donde puedes configurar MySQL y los usuarios según tu entorno.

### Ejecución de tests

```bash
# En CI (GitHub Actions):
python -m unittest tests.test_validaciones -v
python -m unittest tests.test_operaciones_dicc -v

# En local (todos los tests):
python -m unittest discover tests -v
```

> **Nota:** Si quieres correr los tests de base de datos/integración, asegúrate de tener MySQL configurado y el archivo `.env` con los datos correctos.

---

## 👥 Contacto

**Camila V. Heuer** - Ingeniera & Desarrolladora

- LinkedIn: [camilavheuer](https://www.linkedin.com/in/camilavheuer/)
- GitHub: [@CamilaVHeuer](https://github.com/CamilaVHeuer)
- Portfolio: [mini-proyectos-Python](https://github.com/CamilaVHeuer/mini-proyectos-Python)

---

### 🔗 Enlaces Útiles

- [Documentación de Python](https://docs.python.org/3/)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Python Testing](https://docs.python.org/3/library/unittest.html)

---

_"Combinando ingeniería técnica con desarrollo de software para crear soluciones robustas y escalables."_

📈 **Portfolio en evolución** - ¡Nuevos proyectos próximamente!
