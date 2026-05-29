class DetalleNomina:

    def __init__(
        self,
        id_nomina,
        tipo,
        concepto,
        valor
    ):

        self.id_nomina = id_nomina
        self.tipo = tipo
        self.concepto = concepto
        self.valor = valor

    def is_equal(self, detalle):

        return (
            self.id_nomina == detalle.id_nomina and
            self.tipo == detalle.tipo and
            self.concepto == detalle.concepto and
            self.valor == detalle.valor
        )