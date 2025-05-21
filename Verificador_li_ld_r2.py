import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import messagebox

def verificador(vetores):
    matriz = np.array(vetores).T
    posto = np.linalg.matrix_rank(matriz)
    if posto == len(vetores):
        return "LI → Linearmente Independentes"
    else:
        return "LD → Linearmente Dependentes"

def desenhar_vetores(vetores, frame_canvas):
    fig, ax = plt.subplots(figsize=(5, 5))

    origem = [0, 0]
    for v in vetores:
        ax.quiver(
            origem[0], origem[1], v[0], v[1],
            angles='xy', scale_units='xy', scale=1,
            color='green'
        )
    
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_xticks(np.arange(-10, 11, 1))
    ax.set_yticks(np.arange(-10, 11, 1))
    ax.grid(True)
    ax.axhline(0, color='red')
    ax.axvline(0, color='red')
    ax.set_aspect('equal')
    ax.set_title("Vetores no plano 2D")

    
    for widget in frame_canvas.winfo_children(): # Limpa anterior
        widget.destroy() 

    canvas = FigureCanvasTkAgg(fig, master=frame_canvas)
    canvas.draw()
    canvas.get_tk_widget().pack()

def analisar():
    texto = entrada_vetores.get("1.0", tk.END).strip()
    linhas = texto.split("\n")
    vetores = []
    try:
        for linha in linhas:
            if linha.strip():
                x, y = map(float, linha.strip().split(","))
                vetores.append([x, y])
        if len(vetores) == 0:
            raise ValueError("Nenhum vetor válido.")
        resultado = verificador(vetores)
        label_resultado.config(text=f"Resultado: {resultado}")
        desenhar_vetores(vetores, frame_canvas)
    except Exception as e:
        messagebox.showerror("Erro", f"Entrada inválida. Use o formato x,y\nEx: 1,2\n2,1")
        label_resultado.config(text="")


root = tk.Tk()
root.title("Verificador de Vetores 2D")

frame_input = tk.Frame(root)
frame_input.pack(padx=10, pady=10)

tk.Label(frame_input, text="Digite os vetores (um por linha no formato x,y):").pack()
entrada_vetores = tk.Text(frame_input, width=30, height=5)
entrada_vetores.pack(pady=5)

btn_analisar = tk.Button(frame_input, text="Analisar Vetores", command=analisar)
btn_analisar.pack(pady=5)

label_resultado = tk.Label(root, text="", font=("Arial", 12, "bold"))
label_resultado.pack(pady=5)

frame_canvas = tk.Frame(root)
frame_canvas.pack(padx=10, pady=10)

root.mainloop()
