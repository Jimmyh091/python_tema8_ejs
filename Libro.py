class Libro:

    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def __eq__(self, other):
        return self.isbn == other.isbn

    def __str__(self):
        return f"Titulo: {self.titulo}, autor: {self.autor}, isbn: {self.isbn}"