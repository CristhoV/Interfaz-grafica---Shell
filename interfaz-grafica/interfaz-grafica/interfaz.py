# herramientas 

import tkinter as tk
from tkinter import PhotoImage
import subprocess
import os

# Ruta base
base_path = os.path.dirname(os.path.abspath(__file__))
icons_path = os.path.join(base_path, "Icons")

# Comandos para lanzar apps
commands = {
    "Calculadora": "gnome-calculator",
    "Terminal": "gnome-terminal",
    "Navegador": "firefox"
}

# Función para lanzar una app
def launch(app_name):
    cmd = commands.get(app_name)
    if cmd:
        subprocess.Popen(cmd.split())

# Crear ventana principal
root = tk.Tk()
root.title("Lanzador de Aplicaciones")
root.geometry("600x220")

# Cargar imágenes y redimensionar con subsample para hacerlas más pequeñas
icons = {
    name: PhotoImage(file=os.path.join(icons_path, f"{name.lower()}.png")).subsample(3, 3)  # reduce a 1/3 tamaño
    for name in commands
}

# Crear botones con íconos y etiquetas debajo
for i, name in enumerate(commands):
    btn = tk.Button(root, image=icons[name], command=lambda n=name: launch(n),  cursor="hand2")
    btn.grid(row=0, column=i, padx=10, pady=5)
    
    label = tk.Label(root, text=name)
    label.grid(row=1, column=i)

root.mainloop()
