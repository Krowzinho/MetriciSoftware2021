from writer import Writer
from reader import Reader
import random

class Apartament:
    def __init__(self,**kwargs):
        self.id_ap = random.randint(0,1000)
        self.capacitate = kwargs["capacitate"]
        self.nr_paturi = kwargs["nr_paturi"]
        self.pret_ap = kwargs["pret_ap"]
        self.disponibilitate_ap = kwargs["disponibilitate_ap"]
        self.suprafata_ap = kwargs["suprafata_ap"]

    def set_disponibilitate(self, valoare):
        self.disponibilitate_ap = valoare

