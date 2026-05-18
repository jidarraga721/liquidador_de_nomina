# Liquidador de Nómina

Proyecto académico desarrollado en Python para la materia **Código Limpio**.  
La aplicación permite gestionar empleados, nóminas y detalles de nómina utilizando arquitectura MVC, PostgreSQL y pruebas unitarias. El sistema permite insertar y consultar información desde una interfaz de consola.

---

## Autores

* Manolo Restrepo Gil  
* Juan David Idarraga Porras  
* Hans Schoonewolff Otero  

---

## Requisitos

* Python 3.x instalado en el sistema
* PostgreSQL instalado y en ejecución
* Librería psycopg2

---

## Tecnologías utilizadas

- Python 3
- PostgreSQL
- psycopg2
- unittest
- Arquitectura MVC

---

## Instalación y ejecución
q
Siga los siguientes pasos para ejecutar el proyecto:

### 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/repositorio.git
```

### 2. Ingresar al directorio del proyecto

```bash
cd liquidador_de_nomina
```

### 3. Instalar dependencias

```bash
pip install psycopg2-binary
```

### 4. Crear base de datos PostgreSQL

```sql
CREATE DATABASE liquidador_nomina;
```

### 5. Configurar credenciales

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
PGDATABASE = "NOMBRE_DATABASE"
PGUSER = "USUARIO_DATABASE"
PGPASSWORD = "PASSWORD_DATABASE"
PGPORT = "5432"
```

Las credenciales pueden corresponder a una base de datos local PostgreSQL o a un servicio en la nube como Render.
### 6. Ejecutar la aplicación

```bash
python main.py
```

> Nota: Si el archivo principal tiene otro nombre, reemplácelo en el comando anterior.

---

## Uso de la aplicación

Al ejecutar el programa, el sistema mostrará un menú en consola con las siguientes opciones:

```text
1. Insertar empleado
2. Buscar empleado
3. Insertar nomina
4. Buscar nomina
5. Insertar detalle nomina
6. Buscar detalle nomina
7. Salir
```

El usuario podrá insertar y consultar información relacionada con empleados, nómina y detalles de nómina utilizando PostgreSQL.

---

## Ejemplo de ejecución

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
7. Salir
```

### Salida esperada

```text
Total devengado: $1.450.000
Total deducciones: $116.000
Neto a pagar: $1.334.000
```

---





---

## Funcionalidades implementadas

- Crear tablas
- Borrar tablas
- Insertar registros
- Consultar registros
- Liquidación de nómina
- Validaciones de negocio
- Pruebas unitarias con unittest

Tablas utilizadas:

- empleados
- nomina
- detalle_nomina

---

## Ejecutar pruebas unitarias

Desde la raíz del proyecto ejecutar:

```bash
python -m unittest discover -s test -p "test_*.py" -v
```

---

## Arquitectura MVC

### Model

Contiene las entidades y modelos del sistema.

### Controller

Contiene la lógica SQL y operaciones CRUD.

### View Console

Contiene la interfaz de consola para interacción con el usuario.

### Test

Contiene las pruebas unitarias utilizando unittest.

---

## Estructura del proyecto

```text
liquidador_de_nomina/
│
├── src/
│   ├── controller/
│   ├── model/
│   ├── logica/
│   └── view_console/
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
└── requirements.txt
```

---

## Consideraciones

* Los días de incapacidad no pueden superar los días del periodo.
* El auxilio de transporte solo aplica para salarios hasta 2 SMMLV.
* El fondo de solidaridad aplica únicamente para salarios superiores a 4 SMMLV.
* PostgreSQL debe estar instalado y en ejecución.
* La base de datos debe existir antes de ejecutar las pruebas.
* Las credenciales reales no deben subirse al repositorio.