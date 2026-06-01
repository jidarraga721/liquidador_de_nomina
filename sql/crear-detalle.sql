CREATE TABLE IF NOT EXISTS detalle_nomina (

    id_detalle SERIAL PRIMARY KEY,

    id_nomina INTEGER,

    tipo VARCHAR(20),

    concepto VARCHAR(100),

    valor NUMERIC(10,2),

    FOREIGN KEY (id_nomina)
    REFERENCES nomina(id_nomina)
);