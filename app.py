from flask import Flask,render_template, request


from src.routes.empleados_routes import empleados_bp
from src.routes.nomina_routes import nomina_bp
from src.routes.detalle_routes import detalle_bp
from src.controller.empleados_controller import EmpleadosController
from src.controller.nomina_controller import NominaController
from src.controller.detalle_nomina_controller import DetalleNominaController
app = Flask(__name__)

app.register_blueprint(empleados_bp)
app.register_blueprint(nomina_bp)
app.register_blueprint(detalle_bp)

@app.route('/crear_tablas')
def crear_tablas():

    EmpleadosController.crear_tabla()

    return "Tablas creadas correctamente"

@app.route('/buscar_empleado', methods=['GET', 'POST'])
def buscar_empleado():

    empleado = None

    if request.method == 'POST':

        cedula = request.form['cedula']

        empleado = EmpleadosController.buscar_empleado(cedula)

    return render_template(
        'buscar_empleado.html',
        empleado=empleado
    )

@app.route('/insertar_empleado', methods=['GET', 'POST'])
def insertar_empleado():

    if request.method == 'POST':

        nombre = request.form['nombre']
        cedula = request.form['cedula']
        cargo = request.form['cargo']
        salario_base = request.form['salario_base']
        fecha_ingreso = request.form['fecha_ingreso']

        return f"Empleado {nombre} guardado correctamente"

    return render_template('insertar_empleado.html')

if __name__ == '__main__':
    app.run(debug=True)