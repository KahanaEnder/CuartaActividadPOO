from figuras import VentanaBase,Esfera


class VentanaEsfera(VentanaBase):
    def __init__(self, master):
        super().__init__(master, "Esfera", ["Radio"])

    def calcular(self, valores):
        r = valores["radio"]
        figura = Esfera(r)
        return figura.volumen(), figura.superficie()