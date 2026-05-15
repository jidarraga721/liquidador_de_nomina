import sys

sys.path.append(".")
sys.path.append("src")

from controller.nomina_controller import NominaController


id_nomina = int(input("ID nomina: "))

nomina = NominaController.buscar_nomina(id_nomina)

if nomina is None:

    print("Nomina no encontrada")

else:

    print("Empleado:", nomina.id_empleado)

    print("Fecha:", nomina.fecha_liquidacion)

    print("Dias trabajados:", nomina.dias_trabajados)

    print("Devengado:", nomina.total_devengado)

    print("Deducciones:", nomina.total_deducciones)

    print("Salario neto:", nomina.salario_neto)