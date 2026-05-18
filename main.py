import sys

sys.path.append("src")

from model.empleado import Empleado
from model.nomina import Nomina
from model.detalle_nomina import DetalleNomina

from controller.empleados_controller import EmpleadosController
from controller.nomina_controller import NominaController
from controller.detalle_nomina_controller import DetalleNominaController


def insertar_empleado():

    print("\n=== INSERTAR EMPLEADO ===")

    nombre = input("Nombre: ")
    cedula = input("Cedula: ")
    cargo = input("Cargo: ")

    salario_base = float(input("Salario base: "))

    fecha_ingreso = input("Fecha ingreso (YYYY-MM-DD): ")

    empleado = Empleado(
        nombre=nombre,
        cedula=cedula,
        cargo=cargo,
        salario_base=salario_base,
        fecha_ingreso=fecha_ingreso
    )

    EmpleadosController.insertar(empleado)

    print("\nEmpleado insertado correctamente")


def buscar_empleado():

    print("\n=== BUSCAR EMPLEADO ===")

    cedula = input("Cedula: ")

    empleado = EmpleadosController.buscar_empleado(cedula)

    if empleado is None:

        print("\nEmpleado no encontrado")

    else:

        print("\n=== EMPLEADO ===")
        print("Nombre:", empleado.nombre)
        print("Cedula:", empleado.cedula)
        print("Cargo:", empleado.cargo)
        print("Salario:", empleado.salario_base)
        print("Fecha ingreso:", empleado.fecha_ingreso)


def insertar_nomina():

    print("\n=== INSERTAR NOMINA ===")

    id_empleado = int(input("ID empleado: "))

    fecha_liquidacion = input("Fecha liquidacion (YYYY-MM-DD): ")

    dias_trabajados = int(input("Dias trabajados: "))

    total_devengado = float(input("Total devengado: "))

    total_deducciones = float(input("Total deducciones: "))

    salario_neto = total_devengado - total_deducciones

    nomina = Nomina(
        id_empleado=id_empleado,
        fecha_liquidacion=fecha_liquidacion,
        dias_trabajados=dias_trabajados,
        total_devengado=total_devengado,
        total_deducciones=total_deducciones,
        salario_neto=salario_neto
    )

    NominaController.insertar(nomina)

    print("\nNomina insertada correctamente")


def buscar_nomina():

    print("\n=== BUSCAR NOMINA ===")

    id_nomina = int(input("ID nomina: "))

    nomina = NominaController.buscar_nomina(id_nomina)

    if nomina is None:

        print("\nNomina no encontrada")

    else:

        print("\n=== NOMINA ===")
        print("ID empleado:", nomina.id_empleado)
        print("Fecha liquidacion:", nomina.fecha_liquidacion)
        print("Dias trabajados:", nomina.dias_trabajados)
        print("Total devengado:", nomina.total_devengado)
        print("Total deducciones:", nomina.total_deducciones)
        print("Salario neto:", nomina.salario_neto)


def insertar_detalle():

    print("\n=== INSERTAR DETALLE NOMINA ===")

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

    print("\nDetalle insertado correctamente")


def buscar_detalle():

    print("\n=== BUSCAR DETALLE ===")

    id_detalle = int(input("ID detalle: "))

    detalle = DetalleNominaController.buscar_detalle(id_detalle)

    if detalle is None:

        print("\nDetalle no encontrado")

    else:

        print("\n=== DETALLE ===")
        print("ID nomina:", detalle.id_nomina)
        print("Tipo:", detalle.tipo)
        print("Concepto:", detalle.concepto)
        print("Valor:", detalle.valor)


while True:

    print("\n============================")
    print(" SISTEMA DE NOMINA ")
    print("============================")

    print("1. Insertar empleado")
    print("2. Buscar empleado")
    print("3. Insertar nomina")
    print("4. Buscar nomina")
    print("5. Insertar detalle nomina")
    print("6. Buscar detalle nomina")
    print("7. Salir")

    opcion = input("\nSeleccione una opcion: ")

    if opcion == "1":

        insertar_empleado()

    elif opcion == "2":

        buscar_empleado()

    elif opcion == "3":

        insertar_nomina()

    elif opcion == "4":

        buscar_nomina()

    elif opcion == "5":

        insertar_detalle()

    elif opcion == "6":

        buscar_detalle()

    elif opcion == "7":

        print("\nSaliendo del sistema...")
        break

    else:

        print("\nOpcion invalida")
