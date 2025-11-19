# Ej03_NomAP

import tkinter as tk


def mostrar_nombre():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    etiqueta_resultado.config(text=f"Nombre completo: {nombre} {apellido}")


ventana = tk.Tk()
ventana.title("Mostrar Nombre y Apellido")
ventana.geometry("300x200")


tk.Label(ventana, text="Nombre:").pack(pady=0)
entry_nombre = tk.Entry(ventana)
entry_nombre.pack(pady=0)


tk.Label(ventana, text="Apellido:").pack(pady=0)
entry_apellido = tk.Entry(ventana)
entry_apellido.pack(pady=0)


boton_mostrar = tk.Button(ventana, text="Mostrar el Nombre", command=mostrar_nombre)
boton_mostrar.pack(pady=10)


etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12))
etiqueta_resultado.pack(pady=10)


ventana.mainloop()