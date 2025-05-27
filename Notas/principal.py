from Notas import VentanaPrincipal

class Principal:
    """
    Clase principal para ejecutar la aplicación.
    """
    def __init__(self):
        self.app = VentanaPrincipal()

    def run(self):
        """Ejecuta la aplicación de notas."""
        self.app.run()

if __name__ == '__main__':
    Principal().run()

'''
Para ejecutar el
programa no debe ejecutarse
este archivo solamente,
debe cargarse primero el modulo 
usando el comando en la terminal

[python -m Notas.principal]

'''