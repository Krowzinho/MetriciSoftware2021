from writer import Writer
import random

class Camera:
    def __init__(self,**kwargs):
        self.suprafata = kwargs["suprafata"]
        self.pret = kwargs["pret"]
        self.disponibilitate =  kwargs["disponibilitate"]
        self.certificat_verde =  kwargs["certificat_verde"]
        self.id = random.randint(0,1000)
    #functie modifica_camera, parcurg fisierul hotelului si cand gasesc inf despre camera mea le actualizez in obiect si acolo
    #functie get si set pentru fiecare atribut, set pret, set suprafata etc.