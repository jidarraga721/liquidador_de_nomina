import sys

sys.path.append(".")
sys.path.append("src")

from model.empleado import Empleado
from controller.empleados_controller import EmpleadosController


nombre = input("Nombre: ")
cedula = input("Cedula: ")
cargo = input("Cargo: ")

salario = float(input("Salario base: "))

fecha = input("Fecha ingreso: ")


empleado = Empleado(
    nombre=nombre,
    cedula=cedula,
    cargo=cargo,
    salario_base=salario,
    fecha_ingreso=fecha
)

EmpleadosController.insertar(empleado)

print("Empleado creado correctamente")