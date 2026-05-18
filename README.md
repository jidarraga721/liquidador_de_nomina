# Liquidador de Nómina

Proyecto académico desarrollado en Python para la materia **Código Limpio**.  
La aplicación permite liquidar la nómina de un trabajador dependiente en Colombia, calculando devengados, deducciones legales y el valor neto a pagar, incorporando reglas básicas de incapacidades y validaciones.

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
PGHOST = "localhost"
PGDATABASE = "liquidador_nomina"
PGUSER = "postgres"
PGPASSWORD = "TU_PASSWORD"
PGPORT = "5432"
```

### 6. Ejecutar la aplicación

```bash
python main.py
```

> Nota: Si el archivo principal tiene otro nombre, reemplácelo en el comando anterior.

---

## Uso de la aplicación

Al ejecutar el programa, el sistema solicitará los datos necesarios para realizar la liquidación de la nómina.

El usuario debe ingresar la información en el siguiente orden:

1. Salario base mensual
2. Días del periodo (por defecto 30 si no se ingresa)
3. Días trabajados
4. Días de incapacidad
5. Horas extra trabajadas
6. Tipo de horas extra (día o noche)
7. Auxilio de transporte (si aplica)
8. Bonificaciones u otros ingresos
9. Deducciones adicionales

Una vez ingresados los datos, el sistema procesará la información automáticamente y mostrará en pantalla:

* Total devengado
* Total deducciones
* Neto a pagar

---

## Ejemplo de ejecución

```text
Ingrese salario base: 1300000
Ingrese días del periodo: 30
Ingrese días trabajados: 30
Ingrese días de incapacidad: 0
Ingrese horas extra: 5
Ingrese tipo de horas extra: dia
Ingrese auxilio de transporte: si
Ingrese bonificaciones: 0
Ingrese deducciones adicionales: 0
```

### Salida esperada

```text
Total devengado: $1.450.000
Total deducciones: $116.000
Neto a pagar: $1.334.000
```

---

## Entradas del sistema

* Salario base mensual
* Días del periodo (por defecto 30)
* Días trabajados
* Días de incapacidad
* Horas extra trabajadas
* Lapso del día de horas extra (día o noche)
* Auxilio de transporte (si aplica)
* Bonificaciones u otros ingresos
* Deducciones adicionales

---

## Procesos

### 1. Cálculo del salario proporcional

* Valor día = salario_base / días_periodo
* Pago por días trabajados
* Cálculo de horas extra
* Ajuste por incapacidades

### 2. Gestión de incapacidades

* Días 1 y 2: 100% del salario
* Desde el día 3: 66.66%
* Validación: los días de incapacidad no pueden superar el periodo

### 3. Auxilio de transporte

* Aplica hasta 2 salarios mínimos
* Se liquida de forma proporcional

### 4. Deducciones

* Salud: 4%
* Pensión: 4%
* Fondo de solidaridad: 1% desde 4 SMMLV (opcional)

### 5. Cálculo final

* Total devengado
* Total deducciones
* Neto a pagar

---

## Salidas

* Total devengado
* Total deducciones
* Neto a pagar

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