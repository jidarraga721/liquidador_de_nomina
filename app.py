from flask import Flask

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
    NominaController.crear_tabla()
    DetalleNominaController.crear_tabla()

    return "Tablas creadas correctamente"


if __name__ == '__main__':
    app.run(debug=True)