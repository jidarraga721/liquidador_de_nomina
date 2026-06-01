import sys
sys.path.append(".")


import secret_config
import psycopg2

from src.model.empleado import Empleado
import sys



class EmpleadosController:

    def crear_tabla():

        cursor = EmpleadosController.obtener_cursor()

        with open("sql/crear-empleados.sql", "r") as archivo:
            consulta = archivo.read()

        cursor.execute(consulta)

        cursor.connection.commit()

    def insertar(empleado: Empleado):

        cursor = EmpleadosController.obtener_cursor()

        consulta = f"""
        INSERT INTO empleados
        (nombre, cedula, cargo, salario_base, fecha_ingreso)

        VALUES
        ('{empleado.nombre}',
         '{empleado.cedula}',
         '{empleado.cargo}',
         {empleado.salario_base},
         '{empleado.fecha_ingreso}')
        """

        cursor.execute(consulta)

        cursor.connection.commit()

    def obtener_cursor():

        connection = psycopg2.connect(
            database=secret_config.PGDATABASE,
            user=secret_config.PGUSER,
            password=secret_config.PGPASSWORD,
            host=secret_config.PGHOST,
            port=secret_config.PGPORT,
            sslmode="require"
    )

        cursor = connection.cursor()

        return cursor
    def buscar_empleado(cedula):

            cursor = EmpleadosController.obtener_cursor()

            consulta = f"""
        SELECT nombre,
       cedula,
       cargo,
       salario_base,
       fecha_ingreso

        FROM empleados

        WHERE cedula = '{cedula}'
"""

            cursor.execute(consulta)

            fila = cursor.fetchone()

            if fila is None:
                return None

            empleado = Empleado(
            nombre=fila[0],
            cedula=fila[1],
            cargo=fila[2],
            salario_base=fila[3],
            fecha_ingreso=fila[4]
        )
            return empleado
    
    def borrar_tabla():

        cursor = EmpleadosController.obtener_cursor()

        with open("sql/borrar-empleados.sql", "r") as archivo:
            consulta = archivo.read()

        cursor.execute(consulta)

        cursor.connection.commit()