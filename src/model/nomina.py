class Nomina:

    def __init__(
        self,
        id_empleado,
        fecha_liquidacion,
        dias_trabajados,
        total_devengado,
        total_deducciones,
        salario_neto
    ):

        self.id_empleado = id_empleado
        self.fecha_liquidacion = fecha_liquidacion
        self.dias_trabajados = dias_trabajados
        self.total_devengado = total_devengado
        self.total_deducciones = total_deducciones
        self.salario_neto = salario_neto

    def is_equal(self, nomina):

        return (
            self.id_empleado == nomina.id_empleado and
            str(self.fecha_liquidacion) == str(nomina.fecha_liquidacion) and
            self.dias_trabajados == nomina.dias_trabajados and
            self.total_devengado == nomina.total_devengado and
            self.total_deducciones == nomina.total_deducciones and
            self.salario_neto == nomina.salario_neto
        )