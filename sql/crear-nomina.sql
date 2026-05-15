CREATE TABLE nomina (

    id_nomina SERIAL PRIMARY KEY,

    id_empleado INTEGER,

    fecha_liquidacion DATE,

    dias_trabajados INTEGER,

    total_devengado NUMERIC(10,2),

    total_deducciones NUMERIC(10,2),

    salario_neto NUMERIC(10,2),

    FOREIGN KEY (id_empleado)
    REFERENCES empleados(id_empleado)
);