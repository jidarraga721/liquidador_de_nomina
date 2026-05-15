import sys

sys.path.append(".")
sys.path.append("src")

import psycopg2

from model.detalle_nomina import DetalleNomina

import secret_config_sample


class DetalleNominaController:

    def crear_tabla():

        cursor = DetalleNominaController.obtener_cursor()

        with open("sql/crear-detalle.sql", "r") as archivo:
            consulta = archivo.read()

        cursor.execute(consulta)

        cursor.connection.commit()

    def insertar(detalle: DetalleNomina):

        cursor = DetalleNominaController.obtener_cursor()

        consulta = f"""
        INSERT INTO detalle_nomina
        (
            id_nomina,
            tipo,
            concepto,
            valor
        )

        VALUES
        (
            {detalle.id_nomina},
            '{detalle.tipo}',
            '{detalle.concepto}',
            {detalle.valor}
        )
        """

        cursor.execute(consulta)

        cursor.connection.commit()

    def obtener_cursor():

        connection = psycopg2.connect(
            database=secret_config_sample.PGDATABASE,
            user=secret_config_sample.PGUSER,
            password=secret_config_sample.PGPASSWORD,
            host=secret_config_sample.PGHOST,
            port=secret_config_sample.PGPORT
        )

        cursor = connection.cursor()

        return cursor