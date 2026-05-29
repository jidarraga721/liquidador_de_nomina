from flask import Flask

from src.routes.empleados_routes import empleados_bp
from src.routes.nomina_routes import nomina_bp
from src.routes.detalle_routes import detalle_bp

app = Flask(__name__)

app.register_blueprint(empleados_bp)
app.register_blueprint(nomina_bp)
app.register_blueprint(detalle_bp)

if __name__ == '__main__':
    app.run(debug=True)