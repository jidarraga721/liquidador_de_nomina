import sys

sys.path.append(".")
sys.path.append("src")

from model.nomina import Nomina
from controller.nomina_controller import NominaController


id_empleado = int(input("ID empleado: "))

fecha = input("Fecha liquidacion: ")

dias = int(input("Dias trabajados: "))

devengado = float(input("Total devengado: "))

deducciones = float(input("Total deducciones: "))

neto = devengado - deducciones


nomina = Nomina(
    id_empleado=id_empleado,
    fecha_liquidacion=fecha,
    dias_trabajados=dias,
    total_devengado=devengado,
    total_deducciones=deducciones,
    salario_neto=neto
)

NominaController.insertar(nomina)

print("Nomina creada correctamente")