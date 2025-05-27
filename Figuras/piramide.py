from figuras import FiguraGeometrica

class Piramide(FiguraGeometrica):
    def __init__(self, base: float, altura: float, apotema: float):
        self.base = base
        self.altura = altura
        self.apotema = apotema

    def volumen(self) -> float:
        return (1/3) * self.base ** 2 * self.altura

    def superficie(self) -> float:
        return self.base ** 2 + 2 * self.base * self.apotema