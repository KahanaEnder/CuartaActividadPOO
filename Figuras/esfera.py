import math
from figuras import FiguraGeometrica

class Esfera(FiguraGeometrica):
    def __init__(self, radio: float):
        self.radio = radio

    def volumen(self) -> float:
        return (4/3) * math.pi * self.radio ** 3

    def superficie(self) -> float:
        return 4 * math.pi * self.radio ** 2