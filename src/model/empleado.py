class Empleado:

    def __init__(
        self,
        nombre,
        cedula,
        cargo,
        salario_base,
        fecha_ingreso
    ):

        self.nombre = nombre
        self.cedula = cedula
        self.cargo = cargo
        self.salario_base = salario_base
        self.fecha_ingreso = fecha_ingreso

    def is_equal(self, empleado):

        return (
            self.nombre == empleado.nombre and
            self.cedula == empleado.cedula and
            self.cargo == empleado.cargo and
            self.salario_base == empleado.salario_base and
            str(self.fecha_ingreso) == str(empleado.fecha_ingreso)
        )