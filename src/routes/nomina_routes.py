from flask import Blueprint, render_template

nomina_bp = Blueprint(
    'nomina_bp',
    __name__
)

@nomina_bp.route('/nominas')
def nominas():

    return render_template(
        'nominas.html'
    )