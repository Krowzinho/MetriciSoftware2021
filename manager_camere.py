
class camera_manager:
    def __init__(self, lista_camere):
        self.lista_camere = lista_camere

    def printare_camere(self):
        output = ""
        for camera in self.lista_camere:
            output += "Camera are o suprafata de {} si costa {} lei\n".format(camera.suprafata, camera.pret)
        return output

    def sortare_camere_dupa_pret(self):
        pass

    def camere_disponibile(self):
        pass

    def camere_fara_certificat(self):
        pass