import tkinter as tk
from telas.adicionar import FrameAdicionar
from telas.visualizar import FrameVisualizar
from telas.breve import FrameBreve

class Aplicacao(tk.Tk):
    def __init__(self):
        super().__init__()
        self.mostrar_frame_adicionar()

    def mostrar_frame_adicionar(self):
        print("Adicionar")
        self.frame1 = FrameAdicionar(self)
        self.frame1.grid(row=0, column=0)

    def mostrar_frame_visualizar(self):
        print("Visualizar")
        self.frame2 = FrameVisualizar(self)
        self.frame2.grid(row=0, column=0)

    def mostrar_frame_atualizar(self):
        self.frame3 = FrameBreve(self)
        self.frame3.grid(row=0, column=0)

    def mostrar_frame_deletar(self):
        self.frame4 = FrameBreve(self)
        self.frame4.grid(row=0, column=0)


if __name__ == "__main__":
    app = Aplicacao()
    app.mainloop()

