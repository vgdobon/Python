
class Personaje:
    avail_colors = ['red', 'blue', 'green']  # class attribute
    def __init__(self, nombre, status_inic, color):
        # Propiedades (atributos)
        self.name = nombre  # instance attribute (lo "normal")
        self.status = status_inic
        self.color = color

    # Métodos (acciones)
    def die(self):
        self.status = "dead"