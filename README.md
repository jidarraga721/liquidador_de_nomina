# Liquidador de Nómina

Proyecto académico desarrollado en Python para la materia **Código Limpio**.

La aplicación permite gestionar empleados, nóminas y detalles de nómina utilizando arquitectura MVC, PostgreSQL, Flask y pruebas unitarias.

El sistema cuenta con funcionalidades web para insertar, consultar y gestionar información relacionada con la liquidación de nómina.

---

# Autores

* Manolo Restrepo Gil
* Juan David Idarraga Porras
* Hans Schoonewolff Otero

---

# Tecnologías utilizadas

* Python 3
* Flask
* PostgreSQL
* psycopg2
* Gunicorn
* HTML5
* CSS3
* unittest
* Arquitectura MVC
* Blueprints de Flask

---

# Requisitos

Antes de ejecutar el proyecto asegúrese de tener instalado:

* Python 3.x
* PostgreSQL
* Git

---

# Instalación y ejecución local

Siga los siguientes pasos para ejecutar el proyecto localmente.

---

## 1. Clonar el repositorio

```bash
git clone https://github.com/jidarraga721/liquidador_de_nomina.git
```

---

## 2. Ingresar al directorio del proyecto

```bash
cd liquidador_de_nomina
```

---

## 3. Crear entorno virtual (Opcional pero recomendado)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Configuración desde una Base de Datos Vacía

La aplicación puede ejecutarse desde una base de datos PostgreSQL completamente vacía.

---

## 5. Crear base de datos PostgreSQL

Ingresar a PostgreSQL y ejecutar:

```sql
CREATE DATABASE liquidador_nomina;
```

---

## 6. Configurar credenciales

Crear un archivo llamado:

```text
secret_config.py
```

basado en:

```text
secret_config_sample.py
```

con el siguiente contenido:

```python
PGHOST = "HOST_DATABASE"
PGDATABASE = "liquidador_nomina"
PGUSER = "USUARIO_DATABASE"
PGPASSWORD = "PASSWORD_DATABASE"
PGPORT = "5432"
```

Las credenciales pueden corresponder a una base de datos local PostgreSQL o a un servicio en la nube como Render.

---

## 7. Crear tablas automáticamente

El sistema permite crear automáticamente las tablas necesarias desde una base de datos vacía.

Ejecutar la aplicación:

```bash
python app.py
```

Luego ingresar en el navegador a:

```text
http://127.0.0.1:5000/crear_tablas
```

Las tablas creadas son:

* empleados
* nomina
* detalle_nomina

---

## 8. Ejecutar la aplicación

```bash
python app.py
```

La aplicación iniciará localmente en:

```text
http://127.0.0.1:5000
```

---

# Aplicación desplegada

La aplicación se encuentra publicada en Render:

https://liquidador-de-nomina-pzw0.onrender.com

---

# Funcionalidades implementadas

* Funcionalidad web principal
* Funcionalidad web para insertar registros
* Funcionalidad web para buscar registros
* Menú principal de navegación
* Creación automática de tablas
* Insertar registros
* Consultar registros
* Liquidación de nómina
* Validaciones de negocio
* Pruebas unitarias con unittest
* Arquitectura MVC utilizando Blueprints de Flask
* Aplicación desplegada en la nube mediante Render

---

# Uso de la aplicación

La aplicación cuenta con un menú web principal que permite:

* Crear tablas de base de datos
* Insertar empleados
* Buscar empleados
* Gestionar información de nómina

---

# Ejecutar pruebas unitarias

Desde la raíz del proyecto ejecutar:

```bash
python -m unittest discover -s test -p "test_*.py" -v
```

---

# Arquitectura MVC

## Model

Contiene las entidades y modelos del sistema.

## Controller

Contiene la lógica SQL y operaciones CRUD.

## View

Contiene las vistas web y de consola para interacción con el usuario.

## Routes

Contiene las rutas implementadas mediante Blueprints de Flask.

## Test

Contiene las pruebas unitarias utilizando unittest.

---

# Estructura del proyecto

```text
liquidador_de_nomina/
│
├── src/
│   ├── controller/
│   ├── model/
│   ├── logica/
│   ├── routes/
│   └── views/
│
├── templates/
│
├── test/
│   ├── __init__.py
│   ├── test_empleado.py
│   ├── test_nomina.py
│   └── test_detalle_nomina.py
│
├── sql/
│
├── app.py
├── requirements.txt
├── README.md
├── secret_config_sample.py
└── .gitignore
```

---

# Aplicación Web

La aplicación incluye funcionalidades web desarrolladas con Flask utilizando Blueprints bajo arquitectura MVC.

Funcionalidades disponibles:

* Página principal
* Inserción de empleados
* Consulta de empleados
* Navegación mediante menú principal
* Creación automática de tablas

---

# Consideraciones

* Los días de incapacidad no pueden superar los días del periodo.
* El auxilio de transporte solo aplica para salarios hasta 2 SMMLV.
* El fondo de solidaridad aplica únicamente para salarios superiores a 4 SMMLV.
* PostgreSQL debe estar instalado y en ejecución.
* La base de datos puede iniciarse completamente vacía.
* Las credenciales reales no deben subirse al repositorio.
* Las pruebas unitarias requieren conexión válida a PostgreSQL.

---

# Repositorio GitHub

Repositorio oficial del proyecto:

https://github.com/jidarraga721/liquidador_de_nomina

---
