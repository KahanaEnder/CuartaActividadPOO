import tkinter as tk
from tkinter import messagebox
from Notas import Notas

class VentanaPrincipal:
    """
    Ventana de la aplicación para ingreso de notas y visualización de estadísticas.
    """
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Cálculo de Notas")
        self.ventana.geometry("192x284")
        self.ventana.resizable(False, False)

        self.entradas = []
        self.resultado = tk.StringVar()

        self._crear_widgets()

    def _crear_widgets(self):
        # Campos de entrada de notas
        for i in range(5):
            tk.Label(self.ventana, text=f"Nota {i+1}:").grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(self.ventana, width=10)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entradas.append(entry)

        # Botones
        tk.Button(self.ventana, text="Calcular", command=self._on_calcular, width=12).grid(row=5, column=0, pady=15)
        tk.Button(self.ventana, text="Limpiar", command=self._on_limpiar, width=12).grid(row=5, column=1, pady=15)

        # Área de resultado
        tk.Label(self.ventana, textvariable=self.resultado, justify="left", fg="green").grid(
            row=6, column=0, columnspan=2, padx=10, sticky="w"
        )

    def _on_calcular(self):
        try:
            notas = [float(entry.get()) for entry in self.entradas]
            stats = Notas.calcular(notas)
            self.resultado.set(
                f"Promedio: {stats['promedio']:.2f}\n"
                f"Desviación estándar: {stats['desviacion']:.2f}\n"
                f"Nota máxima: {stats['max']}\n"
                f"Nota mínima: {stats['min']}"
            )
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception:
            messagebox.showerror("Error", "Por favor ingresa solo números válidos.")

    def _on_limpiar(self):
        for entry in self.entradas:
            entry.delete(0, tk.END)
        self.resultado.set("")

    def run(self):
        """Inicia el bucle principal de la interfaz gráfica."""
        self.ventana.mainloop()