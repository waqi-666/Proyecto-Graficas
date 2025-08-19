import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def grafica_alejandro():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y, label="Seno")
    plt.title("Gráfica de Alejandro")
    plt.legend()
    save_path = Path(__file__).parent / "alejandro.png"
    plt.savefig(save_path)
    plt.close()
    print(f"Gráfica guardada en: {save_path.resolve()}")

if __name__ == "__main__":
    grafica_alejandro()
