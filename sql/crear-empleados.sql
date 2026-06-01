CREATE TABLE IF NOT EXISTS empleados (

    id_empleado SERIAL PRIMARY KEY,

    nombre VARCHAR(100),
    cedula VARCHAR(20),
    cargo VARCHAR(50),

    salario_base NUMERIC(10,2),

    fecha_ingreso DATE
);