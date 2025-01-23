class Producto:

    def __init__(self, nombre, precio, codigo):
        self.nombre = nombre
        self.precio = precio
        self.codigo = codigo

    def __eq__(self, other):
        return self.codigo == other.codigo