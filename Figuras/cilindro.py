import math
from figuras import FiguraGeometrica

class Cilindro(FiguraGeometrica):
    def __init__(self, radio: float, altura: float):
        self.radio = radio
        self.altura = altura

    def volumen(self) -> float:
        return math.pi * self.radio ** 2 * self.altura

    def superficie(self) -> float:
        return 2 * math.pi * self.radio * (self.altura + self.radio)