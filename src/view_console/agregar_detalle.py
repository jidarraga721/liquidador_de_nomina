import sys

sys.path.append(".")
sys.path.append("src")

from model.detalle_nomina import DetalleNomina

from controller.detalle_nomina_controller import DetalleNominaController


id_nomina = int(input("ID nomina: "))

tipo = input("Tipo (DEVENGO o DEDUCCION): ")

concepto = input("Concepto: ")

valor = float(input("Valor: "))


detalle = DetalleNomina(
    id_nomina=id_nomina,
    tipo=tipo,
    concepto=concepto,
    valor=valor
)

DetalleNominaController.insertar(detalle)

print("Detalle agregado correctamente")