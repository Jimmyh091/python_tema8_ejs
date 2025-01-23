import Empleado

class Desarrollador(Empleado):

    def __init__(self, salario, horas_extra):
        super.__init__(salario, horas_extra)
        self.salario = horas_extra * 30
        self.horas_extra = horas_extra