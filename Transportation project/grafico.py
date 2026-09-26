import tkinter as tk
from tkinter import ttk, messagebox

import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from Transporte import grafo, percurso

FUNDO = "#151515"
PAINEL = "#202020"
TEXTO = "#FFFFFF"
CINZA = "#AAAAAA"
AZUL = "#1976D2"
VERDE = "#00C853"
CINZA_ARESTA = "#888888"

janela = tk.Tk()

janela.title("Sistema de Transporte entre Cidades")
janela.geometry("1250x780")
janela.minsize(1100, 700)
janela.configure(bg=FUNDO)


tk.Label(
    janela,
    text="SISTEMA DE TRANSPORTE",
    font=("Arial", 24, "bold"),
    bg=FUNDO,
    fg=TEXTO
).pack(pady=(20, 0))


tk.Label(
    janela,
    text="Análise de caminhos entre cidades",
    font=("Arial", 11),
    bg=FUNDO,
    fg=CINZA
).pack(pady=(0, 15))


area = tk.Frame(
    janela,
    bg=FUNDO
)

area.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)

painel = tk.Frame(
    area,
    bg=PAINEL,
    width=310
)

painel.pack(
    side="left",
    fill="y",
    padx=(0, 15)
)

painel.pack_propagate(False)


tk.Label(
    painel,
    text="CALCULAR CAMINHO",
    font=("Arial", 15, "bold"),
    bg=PAINEL,
    fg=TEXTO
).pack(pady=(30, 30))


tk.Label(
    painel,
    text="Origem",
    font=("Arial", 11, "bold"),
    bg=PAINEL,
    fg=CINZA
).pack(
    anchor="w",
    padx=30
)


combo_origem = ttk.Combobox(
    painel,
    values=list(grafo.keys()),
    state="readonly",
    font=("Arial", 11)
)

combo_origem.pack(
    fill="x",
    padx=30,
    pady=(5, 25)
)

tk.Label(
    painel,
    text="Destino",
    font=("Arial", 11, "bold"),
    bg=PAINEL,
    fg=CINZA
).pack(
    anchor="w",
    padx=30
)


combo_destino = ttk.Combobox(
    painel,
    values=list(grafo.keys()),
    state="readonly",
    font=("Arial", 11)
)

combo_destino.pack(
    fill="x",
    padx=30,
    pady=(5, 25)
)

tk.Label(
    painel,
    text="RESULTADO",
    font=("Arial", 12, "bold"),
    bg=PAINEL,
    fg=TEXTO
).pack(
    anchor="w",
    padx=30,
    pady=(20, 10)
)


tk.Label(
    painel,
    text="Caminho:",
    font=("Arial", 10),
    bg=PAINEL,
    fg=CINZA
).pack(
    anchor="w",
    padx=30
)


resultado_caminho = tk.Label(
    painel,
    text="-",
    font=("Arial", 10),
    bg=PAINEL,
    fg=TEXTO,
    wraplength=250,
    justify="left"
)

resultado_caminho.pack(
    anchor="w",
    padx=30,
    pady=(5, 20)
)


tk.Label(
    painel,
    text="Distância total:",
    font=("Arial", 10),
    bg=PAINEL,
    fg=CINZA
).pack(
    anchor="w",
    padx=30
)


resultado_distancia = tk.Label(
    painel,
    text="-",
    font=("Arial", 21, "bold"),
    bg=PAINEL,
    fg=VERDE
)

resultado_distancia.pack(
    anchor="w",
    padx=30,
    pady=5
)


botao = tk.Button(
    painel,
    text="CALCULAR CAMINHO",
    font=("Arial", 11, "bold"),
    bg=VERDE,
    fg="white",
    activebackground="#00A844",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=lambda: calcular()
)

botao.pack(
    fill="x",
    padx=30,
    pady=30,
    ipady=10
)

frame_grafo = tk.Frame(
    area,
    bg="white"
)

frame_grafo.pack(
    side="right",
    fill="both",
    expand=True
)

figura = Figure(
    figsize=(9, 6),
    dpi=100
)

ax = figura.add_subplot(111)


canvas = FigureCanvasTkAgg(
    figura,
    master=frame_grafo
)

canvas.get_tk_widget().pack(
    fill="both",
    expand=True
)

G = nx.Graph()

for origem in grafo:

    for destino, distancia in grafo[origem].items():

        G.add_edge(
            origem,
            destino,
            weight=distancia
        )


pos = {
    "Manga": (0, 2),
    "Missões": (2.5, 2),
    "Itacarambi": (5, 2),
    "Januária": (7.5, 2),
    "Maria da Cruz": (10, 2),

    "Lontra": (10, 0),
    "Japonvar": (7.5, 0),
    "Mirabela": (5, 0),
    "Montes Claros": (2.5, 0),
    "Bocaiuva": (0, 0)
}


tamanho_cidade = 5000


def desenhar_grafo(caminho=None):

    ax.clear()

    nx.draw_networkx_edges(
        G,
        pos,
        ax=ax,
        edge_color=CINZA_ARESTA,
        width=3,
        arrows=False
    )

    if caminho:

        arestas_caminho = []

        for i in range(len(caminho) - 1):

            arestas_caminho.append(
                (
                    caminho[i],
                    caminho[i + 1]
                )
            )


        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=arestas_caminho,
            ax=ax,
            edge_color=VERDE,
            width=8,
            arrows=False
        )

    nx.draw_networkx_nodes(
        G,
        pos,
        ax=ax,
        node_color=AZUL,
        node_size=tamanho_cidade,
        edgecolors="white",
        linewidths=3
    )

    nx.draw_networkx_labels(
        G,
        pos,
        ax=ax,
        font_color="white",
        font_size=8,
        font_weight="bold"
    )

    pesos = nx.get_edge_attributes(
        G,
        "weight"
    )


    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=pesos,
        ax=ax,
        font_size=9,
        font_weight="bold",
        label_pos=0.5,
        rotate=False
    )

    ax.set_title(
        "Mapa das Cidades",
        fontsize=18,
        fontweight="bold",
        pad=20
    )

    ax.set_xlim(-2, 12)

    ax.set_ylim(-1.5, 3.5)


    ax.axis("off")

    figura.tight_layout()

    canvas.draw()

def calcular():

    origem = combo_origem.get()

    destino = combo_destino.get()

    if not origem or not destino:

        messagebox.showwarning(
            "Atenção",
            "Selecione a origem e o destino."
        )

        return

    if origem == destino:

        messagebox.showwarning(
            "Atenção",
            "A origem e o destino devem ser diferentes."
        )

        return

    resultado = percurso(
        grafo,
        origem,
        destino
    )


    if resultado is False or resultado is None:

        resultado_caminho.config(
            text="Nenhuma conexão encontrada."
        )

        resultado_distancia.config(
            text="-"
        )

        desenhar_grafo()

        return


    caminho, distancia = resultado


    resultado_caminho.config(
        text=" → ".join(caminho)
    )


    resultado_distancia.config(
        text=f"{distancia} km"
    )


    desenhar_grafo(caminho)


desenhar_grafo()


janela.mainloop()
