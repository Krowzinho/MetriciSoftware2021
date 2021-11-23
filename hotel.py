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
        self.file_writer.write("Hotelul {} are urmatoarele camere {}\n".format(self.nume, self.camere.printare_camere()))

    def adaugare_ap(self, manager_ap):
        self.apartamente = manager_ap
        self.file_writer.write("Hotelul {} are urmatoarele apartamente {}\n".format(self.nume, self.apartamente.printare_apartamente()))

    def apartament_inchiriat(self, id):
        for apartament in self.apartamente.lista_apartamente:
            if id == apartament.id_ap:
                apartament.set_disponibilitate(False)
        print(self.apartamente.printare_apartamente())