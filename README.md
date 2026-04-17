# 🏨 Restful Booker — Selenium Automation

Suite de pruebas automatizadas para el sitio [Restful Booker](https://automationintesting.online), construida con **Python + Selenium + Pytest** siguiendo el patrón **Page Object Model (POM)**.

---

## 🧪 ¿Qué se testea?

### 🔐 Login (`tests/test_login.py`)
| Test | Descripción |
|------|-------------|
| `test_valid_login_shows_admin_panel` | Login con credenciales válidas → panel de admin visible |
| `test_invalid_login_stays_on_login_page` | Login inválido → no accede al panel |
| `test_logout_returns_to_login_form` | Logout → regresa al formulario de login |

### 🛏️ Habitaciones (`tests/test_rooms.py`)
| Test | Descripción |
|------|-------------|
| `test_create_single_room` | Crea habitación tipo Single y verifica que aparece |
| `test_create_double_room` | Crea habitación tipo Double y verifica que aparece |
| `test_create_suite_accessible` | Crea Suite accesible y verifica que aparece |
| `test_delete_room_removes_it_from_list` | Crea y elimina habitación, verifica que desaparece |

### 📬 Contacto (`tests/test_contact.py`)
| Test | Descripción |
|------|-------------|
| `test_valid_contact_form_shows_success` | Formulario completo → mensaje de éxito visible |
| `test_empty_contact_form_does_not_show_success` | Formulario vacío → no muestra mensaje de éxito |

---

## 🏗️ Estructura del proyecto

```
restful-booker-selenium/
├── .github/
│   └── workflows/
│       └── tests.yml        # Pipeline CI/CD en GitHub Actions
├── pages/                   # Page Object Model
│   ├── login_page.py        # Acciones de login y logout
│   ├── admin_page.py        # Gestión de habitaciones (CRUD)
│   └── contact_page.py      # Formulario de contacto
├── tests/                   # Casos de prueba
│   ├── test_login.py
│   ├── test_rooms.py
│   └── test_contact.py
├── conftest.py              # Fixtures globales (driver, login, screenshots)
├── pytest.ini               # Configuración de pytest + reporte HTML
└── requirements.txt         # Dependencias
```

---

## ⚙️ Requisitos

- Python 3.11+
- Google Chrome instalado
- pip

---

## 🚀 Instalación y ejecución local

```bash
# 1. Clonar el repositorio
git clone https://github.com/andres-simbana/restful-booker-selenium.git
cd restful-booker-selenium

# 2. Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar todos los tests
pytest

# 5. Ver el reporte HTML generado
open reports/report.html        # Mac
start reports/report.html       # Windows
```

---

## 📊 Reporte de resultados

Cada ejecución genera automáticamente un reporte HTML en `reports/report.html` con:
- Estado de cada test (passed / failed)
- Tiempo de ejecución
- Screenshots automáticos de los tests fallidos en `reports/screenshots/`

---

## 🤖 CI/CD con GitHub Actions

El pipeline se ejecuta automáticamente en cada `push` o `pull_request` a `main`.

El reporte de resultados queda disponible como artefacto descargable en la pestaña **Actions** de GitHub.

---

## 🔑 Credenciales del sitio de prueba

| Campo | Valor |
|-------|-------|
| URL   | https://automationintesting.online |
| Usuario admin | `admin` |
| Contraseña | `password` |

> ⚠️ Este sitio es público y está diseñado específicamente para practicar automatización de pruebas.

---

## 🛠️ Tecnologías utilizadas

| Herramienta | Versión | Uso |
|-------------|---------|-----|
| Python | 3.11 | Lenguaje base |
| Selenium | 4.18.1 | Automatización del navegador |
| Pytest | 8.1.1 | Framework de testing |
| pytest-html | 4.1.1 | Generación de reportes HTML |
| GitHub Actions | — | CI/CD pipeline |
