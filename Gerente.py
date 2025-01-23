import Empleado

class Gerente(Empleado):

    def __init__(self, salario, horas_extra):
        super().__init__(salario, horas_extra)
        self.salario = salario + salario * 0.2
        self.horas_extra = horas_extra