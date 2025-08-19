import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def grafica_ramirez():
    # Dominio de 0 a 10 con 100 puntos
    x = np.linspace(0, 10, 100)
    y = np.cos(x)

    # Graficar
    plt.figure()
    plt.plot(x, y, label="Coseno")
    plt.xlabel("x")
    plt.ylabel("cos(x)")
    plt.title("Gráfica de Ramírez")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)

    # Guardar la imagen junto al .py
    save_path = Path(_file_).parent / "ramirez.png"
    plt.savefig(save_path, bbox_inches="tight")
    plt.close()
    print(f"Gráfica guardada en: {save_path.resolve()}")

if _name_ == "_main_":
    grafica_ramirez()