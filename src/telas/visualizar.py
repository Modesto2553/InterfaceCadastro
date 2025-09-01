import tkinter as tk
from tkinter import ttk
import pandas as pd
import json
import requests

class FrameVisualizar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.canvas = tk.Canvas(bg="black", width=711, height=707, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.grid(row=0, column=0)

        self.background_img = tk.PhotoImage(file=f"interfaceEstoque/arquivos/pagina_visualizar.png")
        self.background = self.canvas.create_image(355.5, 353.5, image=self.background_img)

        self.img_adicionar = tk.PhotoImage(file=f"interfaceEstoque/arquivos/img_adicionar.png")
        self.btn_adicionar = tk.Button(image=self.img_adicionar, borderwidth=0, highlightthickness=0, command=master.mostrar_frame_adicionar,
                                  relief="flat", anchor="nw")
        self.btn_adicionar.place(x=25, y=300, width=124, height=43)

        self.img_visualizar = tk.PhotoImage(file=f"interfaceEstoque/arquivos/img_Visualizar.png")
        self.btn_visualizar = tk.Button(image=self.img_visualizar, borderwidth=0, highlightthickness=0, command=master.mostrar_frame_visualizar,
                                   relief="flat", anchor="nw")
        self.btn_visualizar.place(x=45, y=350, width=124, height=43)

        self.img_atualizar = tk.PhotoImage(file=f"interfaceEstoque/arquivos/img_atualizar.png")
        self.btn_atualizar = tk.Button(image=self.img_atualizar, borderwidth=0, highlightthickness=0, command=master.mostrar_frame_atualizar,
                                  relief="flat", anchor="nw")
        self.btn_atualizar.place(x=25, y=400, width=124, height=43)

        self.img_deletar = tk.PhotoImage(file=f"interfaceEstoque/arquivos/img_deletar.png")
        self.btn_deletar = tk.Button(image=self.img_deletar, borderwidth=0, highlightthickness=0, command=master.mostrar_frame_deletar,
                                relief="flat", anchor="nw")
        self.btn_deletar.place(x=25, y=450, width=124, height=43)

        self.id_processo = tk.Entry()
        self.id_processo.place(x=210, y=250, width=200, height=25)

        self.visualizar = tk.Text(width=50, height=15)
        self.visualizar.place(x=210, y=300)

        self.img_visualizar_individual = tk.PhotoImage(file=f"interfaceEstoque/arquivos/Visualizar_individual.png")
        self.btn_visualizar_individual = tk.Button(image=self.img_visualizar_individual, borderwidth=0, highlightthickness=0,
                                              command=self.btn_clicked2, relief="flat", anchor="nw")
        self.btn_visualizar_individual.place(x=420, y=230, width=124, height=43)

        self.img_visualizar_tudo = tk.PhotoImage(file=f"interfaceEstoque/arquivos/Visualizar_tudo.png")
        self.btn_visualizar_tudo = tk.Button(image=self.img_visualizar_tudo, borderwidth=0, highlightthickness=0,
                                        command=self.btn_clicked, relief="flat", anchor="nw")
        self.btn_visualizar_tudo.place(x=543, y=230, width=124, height=43)

    def btn_clicked(self):
        self.link = 'SEU BANCO DE DADOS'
        self.visualizar.delete("1.0", tk.END)
        self.requisicao = requests.get(f'{self.link}/Vendas/.json')
        self.json = self.requisicao.json()
        self.vet = []
        print(f'Assim - > {self.json}')
        for self.dado in self.json:
            print(f'Dado {self.json[self.dado]}')
            self.lista = (f"{self.json[self.dado]['Numero_processo']} |", f"{self.json[self.dado]['Cliente']} |", self.json[self.dado]['Data'])
            self.vet.append(self.lista)
        self.valores = self.vet
        self.colunas = ['Numero processo |', 'Cliente |', 'Data']

        self.tabela_clientes = pd.DataFrame.from_records(self.valores, columns=self.colunas)
        self.visualizar.insert('1.0', self.tabela_clientes.to_string(index=False))

    def btn_clicked2(self):
        self.link = 'SEU BANCO DE DADOS'
        self.visualizar.delete("1.0", tk.END)
        self.id = self.id_processo.get()
        if len(self.id) > 0:
            self.requisicao = requests.get(f'{self.link}/Vendas/.json')
            self.json = self.requisicao.json()
            self.vet = []
            for self.dado in self.json:
                if str(self.json[self.dado]['Numero_processo']) == str(self.id):
                    self.lista = (f"{self.json[self.dado]['Numero_processo']} |", f"{self.json[self.dado]['Cliente']} |", self.json[self.dado]['Data'])
                    self.vet.append(self.lista)
            self.valores = self.vet
            if len(self.valores) > 0:
                self.colunas = ['Numero processo |', 'Cliente |', 'Data']

                self.tabela_clientes = pd.DataFrame.from_records(self.valores, columns=self.colunas)
                self.visualizar.insert('1.0', self.tabela_clientes.to_string(index=False))
            else:
                self.visualizar.insert('1.0', 'ID não encontrada')
        else:
            self.visualizar.insert('1.0', 'Digite um ID')

