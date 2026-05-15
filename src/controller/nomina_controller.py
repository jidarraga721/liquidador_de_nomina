import sys

sys.path.append(".")
sys.path.append("src")

import psycopg2

from model.nomina import Nomina

import secret_config_sample


class NominaController:

    def crear_tabla():

        cursor = NominaController.obtener_cursor()

        with open("sql/crear-nomina.sql", "r") as archivo:
            consulta = archivo.read()

        cursor.execute(consulta)

        cursor.connection.commit()

    def insertar(nomina: Nomina):

        cursor = NominaController.obtener_cursor()

        consulta = f"""
        INSERT INTO nomina
        (
            id_empleado,
            fecha_liquidacion,
            dias_trabajados,
            total_devengado,
            total_deducciones,
            salario_neto
        )

        VALUES
        (
            {nomina.id_empleado},
            '{nomina.fecha_liquidacion}',
            {nomina.dias_trabajados},
            {nomina.total_devengado},
            {nomina.total_deducciones},
            {nomina.salario_neto}
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
    def buscar_nomina(id_nomina):

        cursor = NominaController.obtener_cursor()

        consulta = f"""
        SELECT
        id_empleado,
        fecha_liquidacion,
        dias_trabajados,
        total_devengado,
        total_deducciones,
        salario_neto

        FROM nomina

        WHERE id_nomina = {id_nomina}
        """

        cursor.execute(consulta)

        fila = cursor.fetchone()

        if fila is None:
            return None

        nomina = Nomina(
            id_empleado=fila[0],
            fecha_liquidacion=fila[1],
            dias_trabajados=fila[2],
            total_devengado=fila[3],
            total_deducciones=fila[4],
            salario_neto=fila[5]
        )

        return nomina
    def borrar_tabla():

        cursor = NominaController.obtener_cursor()

        with open("sql/borrar-nomina.sql", "r") as archivo:
            consulta = archivo.read()

        cursor.execute(consulta)

        cursor.connection.commit()