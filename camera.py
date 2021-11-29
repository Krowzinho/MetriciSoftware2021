from writer import Writer
import random

class Camera:
    def __init__(self,**kwargs):
        self.suprafata = kwargs["suprafata"]
        self.pret = kwargs["pret"]
        self.disponibilitate =  kwargs["disponibilitate"]
        self.certificat_verde =  kwargs["certificat_verde"]
        self.id = random.randint(0,1000)

    def get_suprafata(self):
        return self.suprafata

    def set_suprafata(self, new_suprafata):
        self.suprafata = new_suprafata

    def get_pret(self):
        return self.pret

    def set_pret(self, new_pret):
        self.pret = new_pret

    def get_disponibilitate(self):
        return self.disponibilitate

    def set_disponibilitate(self, new_disponibilitate):
        self.disponibilitate = new_disponibilitate

    def get_certificat_verde(self):
        return self.certificat_verde

    def set_certificat_verde(self, new_certificat_verde):
        self.certificat_verde = new_certificat_verde

    def get_id(self):
        return self.id
    #functie modifica_camera, parcurg fisierul hotelului si cand gasesc inf despre camera mea le actualizez in obiect si acolo
    #functie get si set pentru fiecare atribut, set pret, set suprafata etc.