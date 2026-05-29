from flask import Blueprint, render_template

detalle_bp = Blueprint(
    'detalle_bp',
    __name__
)

@detalle_bp.route('/detalles')
def detalles():

    return render_template(
        'detalles.html'
    )