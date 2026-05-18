import unittest
import sys

sys.path.append("src")

from model.empleado import Empleado
from controller.empleados_controller import EmpleadosController


class TestEmpleado(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        EmpleadosController.borrar_tabla()

        EmpleadosController.crear_tabla()

    def test_insert_1(self):

        empleado = Empleado(
            nombre="Julian",
            cedula="12345",
            cargo="Programador",
            salario_base=2500000,
            fecha_ingreso="2025-05-15"
        )

        EmpleadosController.insertar(empleado)

        empleado_buscado = EmpleadosController.buscar_empleado(
            empleado.cedula
        )

        self.assertTrue(
            empleado_buscado.is_equal(empleado)
        )

    def test_insert_2(self):

        empleado = Empleado(
            nombre="David",
            cedula="99999",
            cargo="Analista",
            salario_base=3000000,
            fecha_ingreso="2025-06-01"
        )

        EmpleadosController.insertar(empleado)

        empleado_buscado = EmpleadosController.buscar_empleado(
            empleado.cedula
        )

        self.assertTrue(
            empleado_buscado.is_equal(empleado)
        )


if __name__ == '__main__':
    unittest.main()