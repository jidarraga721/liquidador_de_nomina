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

# Requisitos

* Python 3.x instalado en el sistema
* PostgreSQL instalado y en ejecución
* Git instalado
* Librería psycopg2

---

# Tecnologías utilizadas

* Python 3
* Flask
* PostgreSQL
* psycopg2
* unittest
* HTML5
* CSS3
* Arquitectura MVC
* Blueprints de Flask

---

# Instalación y ejecución

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

o manualmente:

```bash
pip install psycopg2-binary
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

Ejecutar:

```bash
python main.py
```

y seleccionar la opción correspondiente para crear tablas desde el menú principal.

Las tablas creadas son:

* empleados
* nomina
* detalle_nomina

---

## 8. Ejecutar la aplicación

```bash
python main.py
```

> Nota: Si el archivo principal tiene otro nombre, reemplácelo en el comando anterior.

La aplicación iniciará localmente permitiendo acceder a las funcionalidades web y de consola.

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

---

# Uso de la aplicación

Al ejecutar el programa, el sistema mostrará un menú con funcionalidades para:

```text
1. Insertar empleado
2. Buscar empleado
3. Insertar nomina
4. Buscar nomina
5. Insertar detalle nomina
6. Buscar detalle nomina
7. Crear tablas
8. Salir
```

El usuario podrá insertar y consultar información relacionada con empleados, nómina y detalles de nómina utilizando PostgreSQL.

---

# Ejemplo de ejecución

```text
============================
 SISTEMA DE NOMINA
============================

1. Insertar empleado
2. Buscar empleado
3. Insertar nomina
4. Buscar nomina
5. Insertar detalle nomina
6. Buscar detalle nomina
7. Crear tablas
8. Salir
```

---

# Salida esperada

```text
Total devengado: $1.450.000
Total deducciones: $116.000
Neto a pagar: $1.334.000
```

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
│   ├── view_console/
│   ├── views/
│   └── templates/
│
├── test/
│   ├── __init__.py
│   ├── test_empleado.py
│   ├── test_nomina.py
│   └── test_detalle_nomina.py
│
├── sql/
│
├── secret_config_sample.py
├── README.md
├── requirements.txt
└── main.py
```

---

# Aplicación Web

La aplicación incluye funcionalidades web desarrolladas con Flask utilizando Blueprints bajo arquitectura MVC.

Funcionalidades disponibles:

* Página principal
* Inserción de empleados
* Consulta de empleados
* Gestión de nómina
* Navegación mediante menú principal

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
