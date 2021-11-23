class Persoana:
    def __init__(self, **kwargs):
        self.nume = kwargs["nume"]
        self.prenume = kwargs ["prenume"]
        self.cnp = kwargs ["cnp"]
        self.certificat_verde = kwargs ["certificat_verde"]
        self.checkin = False
        self.checkout = False
        self.locatie = None

    def inchiriere_apartament(self, hotel, pret_ap):
        for apartament in hotel.apartamente.lista_apartamente:
            if apartament.disponibilitate_ap and int(apartament.pret_ap)<pret_ap:
                self.checkin = True
                self.locatie = apartament.id_ap
                return apartament.id_ap
        return -1

