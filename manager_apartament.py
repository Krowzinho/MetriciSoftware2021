
class apartament_manager:
    def __init__(self, lista_apartamente):
        self.lista_apartamente = lista_apartamente

    def printare_apartamente(self):
        output = ""
        for apartament in self.lista_apartamente:
            output += "\nApartamentul are o suprafata de {} mp\u00b2 si costa {} lei.\n".format(apartament.suprafata_ap, apartament.pret_ap)
            if apartament.get_disponibilitate():
                output += "Este disponibil!\n"
            else:
                output += "Nu este disponibil!\n"
        return output

    def sortare_ap_dupa_pret(self):
        pass

    def ap_disponibile(self):
        pass

    def ap_fara_certificat(self):
        pass