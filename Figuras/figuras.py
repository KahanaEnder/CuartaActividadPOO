import tkinter as tk
from tkinter import messagebox
import math

def abrir_cilindro():
    ventana_figura("Cilindro", campos=["Radio", "Altura"])

def abrir_esfera():
    ventana_figura("Esfera", campos=["Radio"])

def abrir_piramide():
    ventana_figura("Pirámide", campos=["Base", "Altura", "Apotema"])

def ventana_figura(nombre, campos):
    nueva = tk.Toplevel()
    nueva.title(nombre)
    nueva.geometry("256x192")
    nueva.resizable(False, False)
    entradas = {}

    for i, campo in enumerate(campos):
        tk.Label(nueva, text=f"{campo} (cm):").grid(row=i, column=0, padx=10, pady=5, sticky="e")
        entrada = tk.Entry(nueva)
        entrada.grid(row=i, column=1, padx=10, pady=5)
        entradas[campo.lower()] = entrada

    resultado = tk.StringVar()
    tk.Label(nueva, textvariable=resultado, justify="left", fg="green").grid(row=len(campos)+1, column=0, columnspan=2, pady=10)

    def calcular():
        try:
            valores = {k: float(e.get()) for k, e in entradas.items()}
            if nombre == "Cilindro":
                r = valores["radio"]
                h = valores["altura"]
                volumen = math.pi * r**2 * h
                superficie = 2 * math.pi * r * (h + r)

            elif nombre == "Esfera":
                r = valores["radio"]
                volumen = (4/3) * math.pi * r**3
                superficie = 4 * math.pi * r**2

            elif nombre == "Pirámide":
                b = valores["base"]
                h = valores["altura"]
                a = valores["apotema"]
                volumen = (1/3) * b**2 * h
                superficie = b**2 + 2 * b * a

            resultado.set(f"Volumen: {volumen:.2f} cm³\nSuperficie: {superficie:.2f} cm²")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa solo números válidos.")

    tk.Button(nueva, text="Calcular", command=calcular).grid(row=len(campos), column=0, columnspan=2, pady=10)

# Ventana principal
root = tk.Tk()
root.title("Figuras")
root.geometry("350x120")
root.resizable(False, False)

# Botones en una misma fila
frame = tk.Frame(root)
frame.pack(pady=30)

tk.Button(frame, text="Cilindro", width=10, command=abrir_cilindro).grid(row=0, column=0, padx=10)
tk.Button(frame, text="Esfera", width=10, command=abrir_esfera).grid(row=0, column=1, padx=10)
tk.Button(frame, text="Pirámide", width=10, command=abrir_piramide).grid(row=0, column=2, padx=10)

root.mainloop()
