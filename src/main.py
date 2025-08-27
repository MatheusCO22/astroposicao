import tkinter as tk
from window import AstroPosicaoApp


default_args = {
    "latitude": "-25.439346",
    "longitude": "-49.268244",
    "fuso": -3
}

if __name__ == "__main__":
    root = tk.Tk()
    app = AstroPosicaoApp(root, **default_args)
    root.mainloop()