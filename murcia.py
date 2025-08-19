import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def grafica_murcia():
    # Dominio de 0 a 10 con 1000 puntos para ver mejor la tangente
    x = np.linspace(0, 10, 1000)
    y = np.tan(x)

    # Evitar valores extremos/infinito para que la imagen quede legible
    y[np.abs(y) > 10] = np.nan

    # Graficar
    plt.figure()
    plt.plot(x, y, label="Tangente")
    plt.xlabel("x")
    plt.ylabel("tan(x)")
    plt.title("Gráfica de Murcia")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)

    # Guardar la imagen junto al .py
    save_path = Path(__file__).parent / "murcia.png"
    plt.savefig(save_path, bbox_inches="tight")
    plt.close()
    print(f"Gráfica guardada en: {save_path.resolve()}")

if __name__ == "__main__":
    grafica_murcia()
