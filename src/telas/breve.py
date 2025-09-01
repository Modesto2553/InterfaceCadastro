import tkinter as tk

class FrameBreve(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.canvas = tk.Canvas(bg="black", width=711, height=707, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.grid(row=0, column=0)

        self.background_img = tk.PhotoImage(file=f"interfaceEstoquearquivos/breve.png")
        self.background = self.canvas.create_image(355.5, 353.5, image=self.background_img)


        self.img_adicionar = tk.PhotoImage(file=f"interfaceEstoquearquivos/img_adicionar.png")
        self.btn_adicionar = tk.Button(image=self.img_adicionar, borderwidth=0, highlightthickness=0, command=master.mostrar_frame_adicionar, relief="flat", anchor="nw")
        self.btn_adicionar.place(x=25, y=300, width=124, height=43)

        self.img_visualizar = tk.PhotoImage(file=f"interfaceEstoquearquivos/img_Visualizar.png")
        self.btn_visualizar = tk.Button(image=self.img_visualizar, borderwidth=0, highlightthickness=0, command=master.mostrar_frame_visualizar,
                                   relief="flat", anchor="nw")
        self.btn_visualizar.place(x=25, y=350, width=124, height=43)

        self.img_atualizar = tk.PhotoImage(file=f"interfaceEstoquearquivos/img_atualizar.png")
        self.btn_atualizar = tk.Button(image=self.img_atualizar, borderwidth=0, highlightthickness=0, command=master.mostrar_frame_atualizar,
                                  relief="flat", anchor="nw")
        self.btn_atualizar.place(x=25, y=400, width=124, height=43)

        self.img_deletar = tk.PhotoImage(file=f"interfaceEstoquearquivos/img_deletar.png")
        self.btn_deletar = tk.Button(image=self.img_deletar, borderwidth=0, highlightthickness=0, command=master.mostrar_frame_deletar,
                                relief="flat", anchor="nw")
        self.btn_deletar.place(x=25, y=450, width=124, height=43)

