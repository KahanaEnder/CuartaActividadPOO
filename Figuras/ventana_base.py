import tkinter as tk
from tkinter import messagebox

class VentanaBase(tk.Toplevel):
    def __init__(self, master, titulo, campos):
        super().__init__(master)
        self.title(titulo)
        self.geometry("256x192")
        self.resizable(False, False)
        self.entradas = {}

        for i, campo in enumerate(campos):
            tk.Label(self, text=f"{campo} (cm):").grid(row=i, column=0, padx=10, pady=5, sticky="e")
            ent = tk.Entry(self)
            ent.grid(row=i, column=1, padx=10, pady=5)
            self.entradas[campo.lower()] = ent

        self.resultado = tk.StringVar()
        tk.Label(self, textvariable=self.resultado, justify="left", fg="green").grid(
            row=len(campos)+1, column=0, columnspan=2, pady=10)

        tk.Button(self, text="Calcular", command=self._on_calcular).grid(
            row=len(campos), column=0, columnspan=2, pady=10)

    def _on_calcular(self):
        try:
            vals = {k: float(v.get()) for k, v in self.entradas.items()}
            vol, sup = self.calcular(vals)
            self.resultado.set(f"Volumen: {vol:.2f} cm³\nSuperficie: {sup:.2f} cm²")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa solo números válidos.")

    def calcular(self, valores):
        raise NotImplementedError("Este método debe implementarse en la subclase")