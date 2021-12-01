from writer import Writer
from reader import Reader

class Hotel:
    def __init__(self,nume,locatie,nr_camere,nr_apartamente,manager,telefon):
        self.nume = nume
        self.locatie = locatie
        self.nr_camere = nr_camere
        self.nr_apartamente = nr_apartamente
        self.manager = manager
        self.telefon = telefon
        self.file_writer = Writer(self.nume)
        data_hotel = "{},{},{},{},{},{}".format(self.nume, self.locatie, self.nr_camere, self.nr_apartamente,
                                                self.manager, self.telefon)

        self.file_writer.write(data_hotel)

        #reader = Reader(self.nume)
        self.camere = None
        self.apartamente = None

    def adaugare_camere(self, manager_camere):
        self.camere = manager_camere
        self.file_writer.write("Hotelul [{}] are urmatoarele camere: {}\n".format(self.nume, self.camere.printare_camere()))

    def adaugare_ap(self, manager_ap):
        self.apartamente = manager_ap
        self.file_writer.write("Hotelul [{}] are urmatoarele apartamente: {}\n".format(self.nume, self.apartamente.printare_apartamente()))

    def apartament_inchiriat(self, id):
        for apartament in self.apartamente.lista_apartamente:
            if id == apartament.id_ap:
                apartament.set_disponibilitate(False)
        print(self.apartamente.printare_apartamente())

    def camera_inchiriata(self, id):
        for camera in self.camere.lista_camere:
            if id == camera.get_id():
                camera.set_disponibilitate(False)
        print(self.camere.printare_camere())

    def verificare_certificat(self, persoana, id):
        if persoana.get_certificat_verde():
            return True

        for camera in self.camere.lista_camere:
            if camera.get_id() == id:
                if persoana.get_certificat_verde() == camera.get_certificat_verde() and camera.get_disponibilitate():
                    return True

        for apartament in self.apartamente.lista_apartamente:
            if apartament.get_id() == id:
                if persoana.get_certificat_verde() == apartament.get_certificat_verde() and apartament.get_disponibilitate():
                    return True

        return False

    def camere_fara_certificat(self):
        return [camera for camera in self.camere.lista_camere if camera.get_certificat_verde() == False]

    def apartamente_fara_certificat(self):
        return [ap for ap in self.apartamente.lista_apartamente if ap.get_certificat_verde() == False]

    def camera_eliberata(self, id):
        for camera in self.camere.lista_camere:
            if camera.get_id() == id:
                camera.set_disponibilitate(True)
        print(self.camere.printare_camere())

    def apartament_eliberat(self, id):
        for apartament in self.apartamente.lista_apartamente:
            if apartament.get_id() == id:
                apartament.set_disponibilitate(True)