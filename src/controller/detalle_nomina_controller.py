import sys

sys.path.append(".")
sys.path.append("src")

import psycopg2

from model.detalle_nomina import DetalleNomina

import secret_config


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
            database=secret_config.PGDATABASE,
            user=secret_config.PGUSER,
            password=secret_config.PGPASSWORD,
            host=secret_config.PGHOST,
            port=secret_config.PGPORT
        )

        cursor = connection.cursor()

        return cursor