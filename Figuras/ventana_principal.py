import tkinter as tk
from figuras import VentanaCilindro,VentanaEsfera,VentanaPiramide

class VentanaPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Figuras")
        self.root.geometry("350x120")
        self.root.resizable(False, False)
        self._create_widgets()

    def _create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=30)
        tk.Button(frame, text="Cilindro", width=10, command=lambda: VentanaCilindro(self.root)).grid(row=0, column=0, padx=10)
        tk.Button(frame, text="Esfera", width=10, command=lambda: VentanaEsfera(self.root)).grid(row=0, column=1, padx=10)
        tk.Button(frame, text="Pirámide", width=10, command=lambda: VentanaPiramide(self.root)).grid(row=0, column=2, padx=10)

    def run(self):
        self.root.mainloop()