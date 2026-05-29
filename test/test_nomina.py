import unittest
import sys

sys.path.append("src")

from model.nomina import Nomina
from model.empleado import Empleado

from controller.nomina_controller import NominaController
from controller.empleados_controller import EmpleadosController


class TestNomina(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # BORRAR TABLAS
        NominaController.borrar_tabla()
        EmpleadosController.borrar_tabla()

        # CREAR TABLAS
        EmpleadosController.crear_tabla()
        NominaController.crear_tabla()

        # INSERTAR EMPLEADO NECESARIO
        empleado = Empleado(
            nombre="Juan",
            cedula="123456",
            cargo="Ingeniero",
            salario_base=2500000,
            fecha_ingreso="2025-05-15"
        )

        EmpleadosController.insertar(empleado)

    def test_insert_1(self):

        nomina = Nomina(
            id_empleado=1,
            fecha_liquidacion="2025-05-30",
            dias_trabajados=30,
            total_devengado=3000000,
            total_deducciones=240000,
            salario_neto=2760000
        )

        # INSERTAR
        NominaController.insertar(nomina)

        # BUSCAR
        nomina_buscada = NominaController.buscar_nomina(1)

        # VALIDAR
        self.assertTrue(
            nomina_buscada.is_equal(nomina)
        )

    def test_insert_2(self):

        nomina = Nomina(
            id_empleado=1,
            fecha_liquidacion="2025-06-30",
            dias_trabajados=15,
            total_devengado=1500000,
            total_deducciones=120000,
            salario_neto=1380000
        )

        # INSERTAR
        NominaController.insertar(nomina)

        # BUSCAR
        nomina_buscada = NominaController.buscar_nomina(2)

        # VALIDAR
        self.assertTrue(
            nomina_buscada.is_equal(nomina)
        )


if __name__ == '__main__':
    unittest.main()