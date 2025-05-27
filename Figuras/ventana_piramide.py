from figuras import VentanaBase,Piramide


class VentanaPiramide(VentanaBase):
    def __init__(self, master):
        super().__init__(master, "Pirámide", ["Base", "Altura", "Apotema"])

    def calcular(self, valores):
        b = valores["base"]
        h = valores["altura"]
        a = valores["apotema"]
        figura = Piramide(b, h, a)
        return figura.volumen(), figura.superficie()