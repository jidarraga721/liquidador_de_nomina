import sys

sys.path.append(".")
sys.path.append("src")

from controller.empleados_controller import EmpleadosController


cedula = input("Cedula: ")

empleado = EmpleadosController.buscar_empleado(cedula)

if empleado is None:

    print("Empleado no encontrado")

else:

    print("Nombre:", empleado.nombre)
    print("Cargo:", empleado.cargo)
    print("Salario:", empleado.salario_base)