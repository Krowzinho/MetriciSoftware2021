class Persoana:
    def __init__(self, **kwargs):
        self.nume = kwargs["nume"]
        self.prenume = kwargs ["prenume"]
        self.cnp = kwargs ["cnp"]
        self.certificat_verde = kwargs ["certificat_verde"]
        self.buget = kwargs["buget"]
        self.checkin = False
        self.checkout = False
        self.locatie = None

    def get_nume(self):
        return self.nume

    def get_certificat_verde(self):
        return self.certificat_verde

    def get_buget(self):
        return self.buget

    def get_checkin(self):
        return self.checkin

    def get_info(self):
        return f'{self.prenume} {self.nume} cu CNP-ul {self.cnp} are un buget de {self.buget} lei.'

    def inchiriere_apartament(self, hotel, pret_ap):
        #if self.get_checkin():
         #   return -1

        for apartament in hotel.apartamente.lista_apartamente:
            if apartament.disponibilitate_ap and int(apartament.pret_ap)<pret_ap:
                self.checkin = True
                self.locatie = apartament.get_id()
                return apartament.get_id()
        return -1


    def inchiriere_camera(self, hotel, pret_camera):
        #if self.get_checkin():
        #   return -1

        for camera in hotel.camere.lista_camere:
            if camera.get_disponibilitate() and int(camera.get_pret()) < pret_camera:
                self.checkin = True
                self.locatie = camera.get_id()
                return camera.get_id()
        return -1

    def check_out(self):
        return self.locatie

