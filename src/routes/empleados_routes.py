from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect

from src.controller.empleados_controller import EmpleadosController
from src.model.empleado import Empleado

empleados_bp = Blueprint(
    'empleados',
    __name__
)
@empleados_bp.route('/')
def index():

    return render_template('index.html')


@empleados_bp.route('/empleados')
def empleados():

    return render_template('empleados.html')


@empleados_bp.route('/nuevo-empleado')
def nuevo_empleado():

    return render_template('nuevo_empleado.html')


@empleados_bp.route('/guardar-empleado', methods=['POST'])
def guardar_empleado():

    nombre = request.form['nombre']
    cedula = request.form['cedula']
    cargo = request.form['cargo']
    salario_base = request.form['salario_base']
    fecha_ingreso = request.form['fecha_ingreso']

    empleado = Empleado(
        nombre=nombre,
        cedula=cedula,
        cargo=cargo,
        salario_base=salario_base,
        fecha_ingreso=fecha_ingreso
    )


    EmpleadosController.insertar(empleado)

    return redirect('/empleados')

@empleados_bp.route('/buscar_empleado', methods=['GET', 'POST'])
def buscar_empleado():

    empleado = None

    if request.method == 'POST':

        cedula = request.form['cedula']

        empleado = EmpleadosController.buscar_empleado(cedula)

    return render_template(
        'buscar_empleado.html',
        empleado=empleado
    )


@empleados_bp.route('/insertar_empleado')
def insertar_empleado():

    return render_template('insertar_empleado.html')
