import tkinter
from tkinter import *
from persoana import Persoana

class Grafica:
    def __init__(self, lista_persoane):
        # Inits
        self.root = None
        self.btn_adaugare = None
        self.lista_persoane = lista_persoane

        # GUI Inits
        self.creaza_grafica()
        list_box = ListBox(self.root, self.lista_persoane)
        ButonAdaugare(self.root, list_box)
        ButonStergere(self.root, list_box)
        self.porneste_grafica()

    def creaza_grafica(self):
        self.root = Tk()
        self.root.title("GUI MSIC")
        self.root.geometry("720x480")

    def porneste_grafica(self):
        self.root.mainloop()


class ButonAdaugare:
    def __init__(self, root, list_box):
        self.root = root
        self.btn_adaugare = None
        self.fereastra_adaugare = None
        self.listbox = list_box

        # GUI INITS
        self.creaza_buton_adaugare()

    def creaza_buton_adaugare(self):
        self.btn_adaugare = Button(self.root, text="Adauga persoana", command=self.buton_adaugare_apasat)
        self.btn_adaugare.grid(column=0, row=0)

    def buton_adaugare_apasat(self):
        self.creaza_fereastra_adaugare()

    def creaza_fereastra_adaugare(self):
        self.fereastra_adaugare = Toplevel(self.root)
        self.fereastra_adaugare.geometry("400x300")
        self.fereastra_adaugare.title("Fereastra adaugare persoana")

        self.nume_input = Text(self.fereastra_adaugare, width = 20, height = 1)
        self.nume_input.grid (row=0, column = 1)
        self.prenume_input = Text(self.fereastra_adaugare, width = 20, height = 1)
        self.prenume_input.grid(row=1, column=1)
        self.cnp_input = Text(self.fereastra_adaugare, width = 20, height = 1)
        self.cnp_input.grid(row=2, column=1)
        self.buget_input = Text(self.fereastra_adaugare, width = 20, height = 1)
        self.buget_input.grid(row=3, column=1)

        label_nume = Label(self.fereastra_adaugare, text="Nume: ")
        label_nume.grid(row=0, column=0)
        label_prenume = Label(self.fereastra_adaugare, text="Prenume: ")
        label_prenume.grid(row=1, column=0)
        label_cnp = Label(self.fereastra_adaugare, text="CNP: ")
        label_cnp.grid(row=2, column=0)
        label_buget = Label(self.fereastra_adaugare, text="Buget: ")
        label_buget.grid(row=3, column=0)

        buton_adaugare_persoana = Button(self.fereastra_adaugare, text="Adauga persoana", command=self.adauga_persoana)
        buton_adaugare_persoana.grid(row=4, column=0)

    def adauga_persoana(self):
        in_nume = self.nume_input.get("1.0", END)
        in_prenume = self.prenume_input.get("1.0", END)
        in_cnp = self.cnp_input.get("1.0", END)
        in_buget = self.buget_input.get("1.0", END)

        self.listbox.adauga_persoana(Persoana(nume=in_nume.strip(), prenume=in_prenume.strip(), cnp=in_cnp.strip(), buget=in_buget.strip(), certificat_verde=True))
        self.fereastra_adaugare.destroy()



class ButonStergere:
    def __init__(self, root, list_box):
        self.root = root
        self.btn_stergere = None
        self.list_box = list_box

        # GUI INITS
        self.creaza_buton_stergere()

    def creaza_buton_stergere(self):
        self.btn_stergere = Button(self.root, text="Sterge persoana", command=self.buton_stergere_apasat)
        self.btn_stergere.grid(column=0, row=1)

    def buton_stergere_apasat(self):
        self.list_box.sterge_persoana(self.list_box.return_nume_activ())
        self.list_box.goleste_text_edit()


class ListBox:
    def __init__(self, root, lista_persoane):
        self.root = root
        self.list_box = None
        self.lista_persoane = lista_persoane

        self.creaza_list_box()
        self.creaza_text_info()

    def creaza_list_box(self):
        self.list_box = Listbox(self.root)
        self.list_box.grid(row=2, column=0)

        for pos_cnt, persoana in enumerate(self.lista_persoane):
            self.list_box.insert(pos_cnt, persoana.get_nume())

        self.list_box.bind('<<ListboxSelect>>', self.item_apasat)

    def item_apasat(self, event):
        persoana_selectata = self.list_box.get(self.list_box.curselection())
        for persoana in self.lista_persoane:
            if persoana.get_nume() == persoana_selectata:
                self.seteaza_text(persoana.get_info())

    def return_nume_activ(self):
        return  self.list_box.get(self.list_box.curselection())

    def creaza_text_info(self):
        self.text_box = Text(self.root, height=10, width=70)
        self.text_box.grid(row=2, column=1)

    def seteaza_text(self, text):
        self.text_box.delete("1.0","end")
        self.text_box.insert(tkinter.END, text)

    def adauga_persoana(self, persoana):
        self.lista_persoane.append(persoana)
        self.list_box.delete(0, tkinter.END)
        self.creaza_list_box()

    def sterge_persoana(self, nume):
        for persoana in self.lista_persoane:
            if persoana.get_nume() == nume:
                self.lista_persoane.remove(persoana)

        self.list_box.delete(0, tkinter.END)
        self.creaza_list_box()

    def goleste_text_edit(self):
        self.text_box.delete("1.0","end")

