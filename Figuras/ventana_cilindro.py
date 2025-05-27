from figuras import VentanaBase,Cilindro

class VentanaCilindro(VentanaBase):
    def __init__(self, master):
        super().__init__(master, "Cilindro", ["Radio", "Altura"])

    def calcular(self, valores):
        r = valores["radio"]
        h = valores["altura"]
        figura = Cilindro(r, h)
        return figura.volumen(), figura.superficie()