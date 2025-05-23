import tkinter as tk
from tkinter import messagebox
import statistics


ventana = tk.Tk()
ventana.title("Cálculo de Notas")
ventana.geometry("192x284")
ventana.resizable(False, False)
entradas = []

def calcular():
    """
    Calcula estadísticas de notas ingresadas en el formulario.
    Esta función:
    - Obtiene los valores de las entradas de texto
    - Convierte los valores a números flotantes
    - Valida que se hayan ingresado exactamente 5 notas
    - Calcula el promedio, desviación estándar, nota máxima y mínima
    - Actualiza la variable resultado con los cálculos formateados
    Raises:
        ValueError: Si no se ingresan exactamente 5 notas o si hay entradas no numéricas
    Returns:
        None
    """
    try:
        notas = [float(entry.get()) for entry in entradas]

        if len(notas) != 5:
            raise ValueError("Debes ingresar exactamente 5 notas.")

        promedio = sum(notas) / len(notas)
        desviacion = statistics.stdev(notas)
        nota_max = max(notas)
        nota_min = min(notas)

        resultado.set(
            f"Promedio: {promedio:.2f}\n"
            f"Desviación estándar: {desviacion:.2f}\n"
            f"Nota máxima: {nota_max}\n"
            f"Nota mínima: {nota_min}"
        )
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa solo números válidos.")

def limpiar():
    for entry in entradas:
        entry.delete(0, tk.END)
    resultado.set("")


# Crear y organizar los campos con grid

for i in range(5):
    tk.Label(ventana, text=f"Nota {i+1}:").grid(row=i, column=0, padx=10, pady=5, sticky="e")
    entrada = tk.Entry(ventana, width=10)
    entrada.grid(row=i, column=1, padx=5, pady=5)
    entradas.append(entrada)

# Botones de Calcular y Limpiar
tk.Button(ventana, text="Calcular", command=calcular, width=12).grid(row=5, column=0, pady=15)
tk.Button(ventana, text="Limpiar", command=limpiar, width=12).grid(row=5, column=1, pady=15)

# Área de resultado
resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado, justify="left", fg="green").grid(row=6, column=0, columnspan=2, padx=10, sticky="w")

# Ejecutar aplicación
ventana.mainloop()
