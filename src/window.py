import stars
import convertion
import temposideral

import math as m
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import datetime

class AstroPosicaoApp:
    def __init__(self, root, **defaultargs):
        self.root = root
        self.root.title("Astroposição")
        self.root.geometry("930x600")

        # Variáveis de resultado
        self.var_nome_estrela = tk.StringVar()
        self.var_altura = tk.StringVar()
        self.var_azimute = tk.StringVar()

        # Variáveis de entrada
        self.var_latitude = tk.StringVar(value=defaultargs.get("latitude"))
        self.var_longitude = tk.StringVar(value=defaultargs.get("longitude"))
        self.var_fuso = tk.IntVar(value=defaultargs.get("fuso"))
        self.var_hora = tk.IntVar(value=datetime.datetime.now().hour)
        self.var_minuto = tk.IntVar(value=datetime.datetime.now().minute)

        self.dados_observacao = {
            "nome": self.var_nome_estrela,
            "altura": self.var_altura,
            "azimute": self.var_azimute
        }

        # Criar componentes
        self.criar_treeview()
        self.stars_arr = self.carregar_dados()
        self.criar_painel()

    # interface

    def criar_treeview(self):
        colunas = ("nome", "identificador", "constelacao", "distancia",
                   "amagnitude", "vmagnitude", "ra", "dec")

        self.tree = ttk.Treeview(self.root, columns=colunas,
                                 show="headings", selectmode="browse")
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_item_select)

        # Headers
        self.tree.heading("nome", text="Nome")
        self.tree.heading("identificador", text="Identificador")
        self.tree.heading("distancia", text="Distância")
        self.tree.heading("constelacao", text="Constelação")
        self.tree.heading("vmagnitude", text="Magnitude Aparente")
        self.tree.heading("amagnitude", text="Magnitude Absoluta")
        self.tree.heading("ra", text="RA")
        self.tree.heading("dec", text="Dec")

        self.tree.column("nome", width=100)
        self.tree.column("identificador", width=80, anchor="center")
        self.tree.column("distancia", width=60, anchor="e")
        self.tree.column("constelacao", width=75, anchor="center")
        self.tree.column("vmagnitude", width=100, anchor="e")
        self.tree.column("amagnitude", width=100, anchor="e")
        self.tree.column("ra", width=100, anchor="e")
        self.tree.column("dec", width=100, anchor="e")

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.root, orient="vertical",
                                  command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self.tree.pack(expand=True, fill="both", padx=10, pady=10)

    def criar_painel(self):
        painel = tk.Frame(self.root, bd=2, relief="groove", padx=10, pady=5)
        painel.pack(fill="x", padx=(10, 25), pady=5)

        # Painel esquerdo
        painel_esquerda = tk.Frame(painel, width=150)
        painel_esquerda.pack(side="left", fill="x")

        sep = ttk.Separator(painel, orient="vertical")
        sep.pack(side="left", fill="y", padx=5)

        # Painel direito
        painel_direita = tk.Frame(painel)
        painel_direita.pack(side="left", fill="y")

        # Data de observação
        tk.Label(painel_esquerda, text="Data de observação:",
                 font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w")
        self.entrada_data = DateEntry(painel_esquerda,
                                      date_pattern="dd/mm/yyyy", width=10)
        self.entrada_data.grid(row=0, column=1, pady=5, sticky="w")

        tk.Label(painel_esquerda, text="Horário de observação:",
                 font=("Arial", 10, "bold")).grid(row=0, column=2, sticky="w", padx=(10, 0))
        self.spin_hora = tk.Spinbox(painel_esquerda, from_=0, to=23,
                                    width=5, format="%02.0f",
                                    textvariable=self.var_hora)
        self.spin_hora.grid(row=0, column=3, sticky="w")
        self.var_hora.trace_add("write", self.on_var_change)

        self.spin_minuto = tk.Spinbox(painel_esquerda, from_=0, to=59,
                                      width=5, format="%02.0f",
                                      textvariable=self.var_minuto)
        self.spin_minuto.grid(row=0, column=3, sticky="w", padx=(50, 0))
        self.var_minuto.trace_add("write", self.on_var_change)

        tk.Label(painel_esquerda, text="Hora", font=("Arial", 7)).grid(row=1, column=3, sticky="w")
        tk.Label(painel_esquerda, text="Minuto", font=("Arial", 7)).grid(row=1, column=3, padx=(50, 0), sticky="w")

        # Local
        tk.Label(painel_esquerda, text="Local de observação:",
                 font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w")
        self.entry_lat = tk.Entry(painel_esquerda, width=16, textvariable=self.var_latitude)
        self.entry_lat.grid(row=2, column=1, padx=(0, 0), pady=0)

        self.entry_long = tk.Entry(painel_esquerda, width=16, textvariable=self.var_longitude)
        self.entry_long.grid(row=2, column=2, padx=(16, 0), pady=5)

        tk.Label(painel_esquerda, text="Latitude", font=("Arial", 7)).grid(row=3, column=1, padx=24, sticky="n")
        tk.Label(painel_esquerda, text="Longitude", font=("Arial", 7)).grid(row=3, column=2, padx=48, sticky="n")

        tk.Label(painel_esquerda, text="Fuso horário:", font=("Arial", 10, "bold")).grid(row=4, column=0, sticky="w", pady=(15, 0))
        self.spin_fuso = tk.Spinbox(painel_esquerda, from_=-12, to=14, width=5, format="%02.0f",
                                    textvariable=self.var_fuso)
        self.spin_fuso.grid(row=4, column=1, pady=(15, 0), sticky="w")
        self.var_fuso.trace_add("write", self.on_var_change)

        # Resultados
        tk.Label(painel_direita, text="Estrela:", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w")
        tk.Label(painel_direita, textvariable=self.dados_observacao['nome']).grid(row=0, column=1, sticky="w")

        tk.Label(painel_direita, text="Altura:", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w")
        tk.Label(painel_direita, textvariable=self.dados_observacao['altura']).grid(row=1, column=1, sticky="w")

        tk.Label(painel_direita, text="Azimute:", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w")
        tk.Label(painel_direita, textvariable=self.dados_observacao['azimute']).grid(row=2, column=1, sticky="w")

    # Funções
    def carregar_dados(self):
        stars_arr = stars.get_stars_arr()

        for item in self.tree.get_children():
            self.tree.delete(item)

        for star in stars_arr:
            self.tree.insert("", tk.END, values=(star.name, star.identifier, star.constellation,
                                                 f"{star.distance} ly", star.Amagnitude, star.Vmagnitude,
                                                 f"{star.ra[0]}h {star.ra[1]}m {star.ra[2]}s",
                                                 f"{star.dec[0]}° {star.dec[1]}' {star.dec[2]}''"))
        return stars_arr

    def get_selected_star_index(self):
        selecionado = self.tree.selection()
        index = self.tree.index(selecionado[0])
        
        return index

    def on_tree_item_select(self, event):
        selecionado = self.tree.selection()

        if not selecionado:
            return
        index = self.get_selected_star_index()
        self.obter_Ah(index)
    
    def on_var_change(self, *args):
        index = self.get_selected_star_index()
        self.obter_Ah(index)

    def obter_Ah(self, index):
        datetimeObservacao = datetime.datetime.combine(
            self.entrada_data.get_date(),
            datetime.time(hour=self.var_hora.get(), minute=self.var_minuto.get())
        )

        latitudeObservacao = float(self.var_latitude.get())
        longitudeObservacao = float(self.var_longitude.get())
        fusoObservacao = self.var_fuso.get()

        estrela = self.stars_arr[index]

        ra_deg = convertion.horario_to_decimal(estrela.ra)
        dec_deg = convertion.sexagesimal_to_decimal(estrela.dec)

        TS_Local = temposideral.get_local_TS(latitudeObservacao, fusoObservacao, datetimeObservacao)
        TS_Local = TS_Local * 15

        ra = m.radians(ra_deg)
        dec = m.radians(dec_deg)
        TS = m.radians(TS_Local)
        phi = m.radians(longitudeObservacao)

        Ah = convertion.radec_to_Ah(ra, dec, TS, phi)

        Ah_sexagesimal = [
            convertion.decimal_to_sexagesimal(m.degrees(Ah[0])),
            convertion.decimal_to_sexagesimal(m.degrees(Ah[1]))
        ]

        Ah_formatado = [
            f"{Ah_sexagesimal[0][0]}° {Ah_sexagesimal[0][1]}' {Ah_sexagesimal[0][2]:.2f}\"",
            f"{Ah_sexagesimal[1][0]}° {Ah_sexagesimal[1][1]}' {Ah_sexagesimal[1][2]:.2f}\""
        ]

        self.var_nome_estrela.set(estrela.name)
        self.var_altura.set(Ah_formatado[0])
        self.var_azimute.set(Ah_formatado[1])