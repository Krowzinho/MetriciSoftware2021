from hotel import Hotel
from camera import Camera
from manager_camere import camera_manager
from apartament import Apartament
from manager_apartament import apartament_manager
from persoana import Persoana

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

    ap1 = Apartament(capacitate="2", nr_paturi="1", pret_ap="190", disponibilitate_ap=True,
                     suprafata_ap="35")
    ap2 = Apartament(capacitate="4", nr_paturi="2", pret_ap="150", disponibilitate_ap=True,
                     suprafata_ap="40")
    ap3 = Apartament(capacitate="5", nr_paturi="2", pret_ap="200", disponibilitate_ap=True,
                     suprafata_ap="42")
    ap4 = Apartament(capacitate="6", nr_paturi="3", pret_ap="250", disponibilitate_ap=True,
                     suprafata_ap="45")

    pers1 = Persoana(nume="Ion",prenume="Popescu",cnp="1981112160025", certificat_verde=True)
    pers2 = Persoana(nume="Ion2",prenume="Popescu2",cnp="1980112160025", certificat_verde=True)
    pers3 = Persoana(nume="Ion3",prenume="Popescu3",cnp="1981112160025", certificat_verde=True)
    pers4 = Persoana(nume="Ion4",prenume="Popescu4",cnp="1981112160025", certificat_verde=True)
    pers5 = Persoana(nume="Ion5",prenume="Popescu5",cnp="198112160025", certificat_verde=True)
    pers6 = Persoana(nume="Ion6",prenume="Popescu6",cnp="198511160025", certificat_verde=True)

    camere_hotel_h2 = camera_manager([c1, c2, c3, c4])
    camere_hotel_h3 = camera_manager([c5, c6, c7, c8, c9])

    h2.adaugare_camere(camere_hotel_h2)
    h3.adaugare_camere(camere_hotel_h3)

    apartament_hotel_h2 = apartament_manager([ap1,ap2])
    apartament_hotel_h3 = apartament_manager([ap3,ap4])

    h2.adaugare_ap(apartament_hotel_h2)
    h3.adaugare_ap(apartament_hotel_h3)

    if pers1.inchiriere_apartament(h2,200)!=-1:
        h2.apartament_inchiriat(pers1.inchiriere_apartament(h2,200))

