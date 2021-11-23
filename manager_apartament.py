
class apartament_manager:
    def __init__(self, lista_apartamente):
        self.lista_apartamente = lista_apartamente

    def printare_apartamente(self):
        output = ""
        for apartament in self.lista_apartamente:
            output += "Apartamentul are o suprafata de {} si costa {} lei\n".format(apartament.suprafata_ap, apartament.pret_ap)
            if apartament.disponibilitate_ap:
                output += "Este Disponibil\n"
            else:
                output += "Nu este disponibil\n"
        return output

    def sortare_ap_dupa_pret(self):
        pass

    def ap_disponibile(self):
        pass

    def ap_fara_certificat(self):
        pass