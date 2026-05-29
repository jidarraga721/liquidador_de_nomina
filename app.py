import sys
from xmlrpc import server 
sys.path.append("src")

from flask import Flask, render_template, request


from model.detalle_nomina import DetalleNomina
from model.empleado import Empleado
from model.nomina import Nomina 

from controller.empleados_controller import EmpleadosController
from controller.nomina_controller import NominaController
from controller.detalle_nomina_controller import DetalleNominaController    

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("crear_empleado.html")

@app.route("/crear_tablas")
def crear_tablas():
    EmpleadosController.crear_tabla()
    return "Tablas creadas correctamente. Ya puede usar la aplicación."

@app.route("/guardar_empleado")
def guardar_empleado():
    nombre = request.args.get("nombre")
    cedula = request.args.get("cedula")
    cargo = request.args.get("cargo")
    salario_base = float(request.args.get("salario_base"))
    fecha_ingreso = request.args.get("fecha_ingreso")

    empleado = Empleado(
        nombre=nombre,
        cedula=cedula,
        cargo=cargo,
        salario_base=salario_base,
        fecha_ingreso=fecha_ingreso
    )

    EmpleadosController.insertar(empleado)

    return "Empleado insertado correctamente:" + request.args["nombre"]

if __name__ == "__main__":
    server.run(debug=True)

