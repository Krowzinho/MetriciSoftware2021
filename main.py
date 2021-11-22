from hotel import Hotel
from camera import Camera
from manager_camere import camera_manager

if __name__ == '__main__':
    #h1 = Hotel ("Royal Bay Resort - All Inclusive","Bulgaria","3","3","Radoi","0727213717")
    h2 = Hotel("B", "Bulgaria", "3", "3", "Radoi", "0727213717")
    h3 = Hotel("C", "Bulgaria", "3", "3", "Radoi", "0727213717")

    c1 = Camera(suprafata="50", pret="500", disponibilitate=True,certificat_verde=True)
    c2 = Camera(suprafata="51", pret="551", disponibilitate=False, certificat_verde=True)
    c3 = Camera(suprafata="52", pret="552", disponibilitate=True, certificat_verde=False)
    c4 = Camera(suprafata="51", pret="551", disponibilitate=False, certificat_verde=True)
    c5 = Camera(suprafata="52", pret="552", disponibilitate=True, certificat_verde=False)
    c6 = Camera(suprafata="51", pret="551", disponibilitate=False, certificat_verde=True)
    c7 = Camera(suprafata="52", pret="552", disponibilitate=True, certificat_verde=False)
    c8 = Camera(suprafata="51", pret="551", disponibilitate=False, certificat_verde=True)
    c9 = Camera(suprafata="52", pret="552", disponibilitate=True, certificat_verde=False)

    camere_hotel_h2 = camera_manager([c1, c2, c3, c4])
    camere_hotel_h3 = camera_manager([c5, c6, c7, c8, c9])
    h2.adaugare_camere(camere_hotel_h2)
    h3.adaugare_camere(camere_hotel_h3)


