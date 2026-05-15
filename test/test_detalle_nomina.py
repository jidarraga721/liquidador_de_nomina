import unittest
import sys

sys.path.append("src")

from model.detalle_nomina import DetalleNomina
from model.nomina import Nomina
from model.empleado import Empleado

from controller.detalle_nomina_controller import DetalleNominaController
from controller.nomina_controller import NominaController
from controller.empleados_controller import EmpleadosController


class TestDetalleNomina(unittest.TestCase):

    def setUpClass():

        # BORRAR TABLAS
        DetalleNominaController.borrar_tabla()
        NominaController.borrar_tabla()
        EmpleadosController.borrar_tabla()

        # CREAR TABLAS
        EmpleadosController.crear_tabla()
        NominaController.crear_tabla()
        DetalleNominaController.crear_tabla()

        # CREAR EMPLEADO
        empleado = Empleado(
            nombre="Juan",
            cedula="123456",
            cargo="Ingeniero",
            salario_base=2500000,
            fecha_ingreso="2025-05-15"
        )

        EmpleadosController.insertar(empleado)

        # CREAR NOMINA
        nomina = Nomina(
            id_empleado=1,
            fecha_liquidacion="2025-05-30",
            dias_trabajados=30,
            total_devengado=3000000,
            total_deducciones=240000,
            salario_neto=2760000
        )

        NominaController.insertar(nomina)

    def test_insert_1(self):

        detalle = DetalleNomina(
            id_nomina=1,
            tipo="DEVENGO",
            concepto="Horas extra",
            valor=200000
        )

        # INSERTAR
        DetalleNominaController.insertar(detalle)

        # BUSCAR
        detalle_buscado = DetalleNominaController.buscar_detalle(1)

        # VALIDAR
        self.assertTrue(
            detalle_buscado.is_equal(detalle)
        )

    def test_insert_2(self):

        detalle = DetalleNomina(
            id_nomina=1,
            tipo="DEDUCCION",
            concepto="Salud",
            valor=120000
        )

        # INSERTAR
        DetalleNominaController.insertar(detalle)

        # BUSCAR
        detalle_buscado = DetalleNominaController.buscar_detalle(2)

        # VALIDAR
        self.assertTrue(
            detalle_buscado.is_equal(detalle)
        )


if __name__ == '__main__':
    unittest.main()