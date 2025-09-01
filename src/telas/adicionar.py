import tkinter as tk
import json
import requests

class FrameAdicionar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.canvas = tk.Canvas(bg="black", width=711, height=707, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.grid(row=0, column=0)

        self.background_img = tk.PhotoImage(file=f"arquivos/Adicionar.png")
        self.background = self.canvas.create_image(355.5, 353.5, image=self.background_img)


        self.img_adicionar = tk.PhotoImage(file=f"interfaceEstoque/arquivos/img_adicionar.png")
        self.btn_adicionar = tk.Button(image=self.img_adicionar, borderwidth=0, highlightthickness=0, command=master.mostrar_frame_adicionar, relief="flat", anchor="nw")
        self.btn_adicionar.place(x=45, y=300, width=124, height=43)

        self.img_visualizar = tk.PhotoImage(file=f"interfaceEstoque/arquivos/img_Visualizar.png")
        self.btn_visualizar = tk.Button(image=self.img_visualizar, borderwidth=0, highlightthickness=0, command=master.mostrar_frame_visualizar,
                                   relief="flat", anchor="nw")
        self.btn_visualizar.place(x=25, y=350, width=124, height=43)

        self.img_atualizar = tk.PhotoImage(file=f"interfaceEstoque/arquivos/img_atualizar.png")
        self.btn_atualizar = tk.Button(image=self.img_atualizar, borderwidth=0, highlightthickness=0, command=master.mostrar_frame_atualizar,
                                  relief="flat", anchor="nw")
        self.btn_atualizar.place(x=25, y=400, width=124, height=43)

        self.img_deletar = tk.PhotoImage(file=f"interfaceEstoque/arquivos/img_deletar.png")
        self.btn_deletar = tk.Button(image=self.img_deletar, borderwidth=0, highlightthickness=0, command=master.mostrar_frame_deletar,
                                relief="flat", anchor="nw")
        self.btn_deletar.place(x=25, y=450, width=124, height=43)

        self.id_processo = tk.Entry()
        self.id_processo.place(x=240, y=300, width=200, height=25)

        self.nome = tk.Entry()
        self.nome.place(x=240, y=373, width=200, height=25)

        self.data = tk.Entry()
        self.data.place(x=240, y=450, width=200, height=25)

        self.adicionar = tk.PhotoImage(file=f'interfaceEstoque/arquivos/botao_adicionar.png')
        self.botao_adicionar = tk.Button(image=self.adicionar, borderwidth=0, highlightthickness=0, command=self.create, relief="flat", anchor="nw")
        self.botao_adicionar.place(x=270, y=500, width=124, height=43)


    def create(self):
        try:
            self.link = 'SEU BANCO DE DADOS'
            self.dados = {'Cliente': self.nome.get(), 'Numero_processo': self.id_processo.get(), 'Data': self.data.get()}
            self.requisicao = requests.post(f'{self.link}/Vendas/.json', data=json.dumps(self.dados))

            self.mensagem = tk.Text(width=22, height=1)
            self.mensagem.place(x=270, y=600)
            self.mensagem.delete("1.0", tk.END)
            self.mensagem.insert('1.0', 'Adicionado com sucesso')
        except Exception:
            self.mensagem = tk.Text(width=17, height=1)
            self.mensagem.place(x=270, y=600)
            self.mensagem.delete("1.0", tk.END)
            self.mensagem.insert('1.0', 'Erro ao adicionar, tente novamente mais tarde')
