from hotel import Hotel
from camera import Camera
from manager_camere import camera_manager
from apartament import Apartament
from manager_apartament import apartament_manager
from persoana import Persoana
from printer import PDF_Printer
from grafica import Grafica

if __name__ == '__main__':
    #Lista hoteluri
    h1 = Hotel ("Royal Bay Resort-All Inclusive"," Bulgaria [tara]"," 3 [camere] "," 3 [apartamente] "," Borislav [nume manager]"," +359 700 18 411 [nr telefon]")
    h2 = Hotel("Hotel Rusu", " Romania [tara]", " 6 [camere]", " 3 [apartamente]", " Radoi [nume manager]", " +40 724 233 820 [nr telefon]")
    h3 = Hotel("Anassa Blue Boutique Hotel", " Thasos [tara]", " 8 [camere] ", " 2 [apartamente] ", " Giannis [nume manager]", " +30 2593 022844 [nr telefon]")

    #Lista camere
    c1 = Camera(suprafata="50", pret="600", disponibilitate=True, certificat_verde=True)
    c2 = Camera(suprafata="51", pret="561", disponibilitate=False, certificat_verde=True)
    c3 = Camera(suprafata="52", pret="572", disponibilitate=True, certificat_verde=False)
    c4 = Camera(suprafata="51", pret="581", disponibilitate=True, certificat_verde=True)
    c5 = Camera(suprafata="52", pret="592", disponibilitate=True, certificat_verde=False)
    c6 = Camera(suprafata="51", pret="651", disponibilitate=True, certificat_verde=True)
    c7 = Camera(suprafata="52", pret="752", disponibilitate=True, certificat_verde=False)
    c8 = Camera(suprafata="51", pret="851", disponibilitate=True, certificat_verde=True)
    c9 = Camera(suprafata="52", pret="852", disponibilitate=True, certificat_verde=False)

    #Lista apartamente
    ap1 = Apartament(capacitate="2", nr_paturi="1", pret_ap="190", disponibilitate_ap=True,
                     suprafata_ap="35")
    ap2 = Apartament(capacitate="4", nr_paturi="2", pret_ap="150", disponibilitate_ap=False,
                     suprafata_ap="40")
    ap3 = Apartament(capacitate="5", nr_paturi="2", pret_ap="200", disponibilitate_ap=True,
                     suprafata_ap="42")
    ap4 = Apartament(capacitate="6", nr_paturi="3", pret_ap="250", disponibilitate_ap=True,
                     suprafata_ap="45")

    #Lista persoane
    pers1 = Persoana(nume="Lucan",prenume="Florin",cnp="198112160025", certificat_verde=True, buget=800)
    pers2 = Persoana(nume="Mateescu",prenume="Roxana",cnp="296011160013", certificat_verde=True, buget=400)
    pers3 = Persoana(nume="Popescu",prenume="Mihai",cnp="1700715160016", certificat_verde=True, buget=122)
    pers4 = Persoana(nume="Antonio",prenume="Gabriel",cnp="1881101160020", certificat_verde=False, buget=305)
    pers5 = Persoana(nume="Andronache",prenume="Elena",cnp="2010315160035", certificat_verde=True, buget=230)
    pers6 = Persoana(nume="Dumitrascu",prenume="Alexandra",cnp="2990511160021", certificat_verde=True, buget=523)

    #Lista camerelor pentru fiecare hotel
    camere_hotel_h1 = camera_manager([c1, c2, c3])
    camere_hotel_h2 = camera_manager([c1, c2, c3, c4, c5, c6])
    camere_hotel_h3 = camera_manager([c1, c2, c3, c5, c6, c7, c8, c9])

    #Adaugare camere pentru fiecare hotel
    h1.adaugare_camere(camere_hotel_h1)
    h2.adaugare_camere(camere_hotel_h2)
    h3.adaugare_camere(camere_hotel_h3)

    #Lista apartamentelor pentru fiecare hotel
    apartament_hotel_h1 = apartament_manager([ap1, ap3, ap4])
    apartament_hotel_h2 = apartament_manager([ap1, ap2, ap3])
    apartament_hotel_h3 = apartament_manager([ap2, ap4])

    #Adaugare apartament pentru fiecare hotel
    h1.adaugare_ap(apartament_hotel_h1)
    h2.adaugare_ap(apartament_hotel_h2)
    h3.adaugare_ap(apartament_hotel_h3)

    #Conditie inchiriere apartament in functie de parametru dat
    if pers1.inchiriere_apartament(h2, 200) != -1:
        h2.apartament_inchiriat(pers1.inchiriere_apartament(h2, 200))

    #Inchiriere camera
    if pers1.inchiriere_camera(h2, pers1.get_buget()) != -1 and h2.verificare_certificat(pers1, pers1.inchiriere_camera(h2, pers1.get_buget())):
        h2.camera_inchiriata(pers1.inchiriere_camera(h2, pers1.get_buget()))
    else:
        print("Nu se pot inchiria camere in acest hotel!")

    #Fac checkout dintr-o camera
    h2.camera_eliberata(pers1.check_out())

    printer = PDF_Printer()

    printer.scrie_PDF("NUME:")
    printer.scrie_PDF("PRENUME:")
    printer.scrie_PDF("CNP:")
    printer.scrie_PDF("CERTIFICAT VERDE:")
    printer.scrie_PDF("PRET APARTAMENT/CAMERA INCHIRIATA:")

    printer.printeaza_PDF()


    lista_persoane = [pers1, pers2, pers3, pers4, pers5, pers6]
    lista_hoteluri = [h1, h2, h3]
    manager_camere = camera_manager([c1, c2, c3, c4, c5, c6, c7, c8, c9])
    manager_apartament = apartament_manager([ap1, ap2, ap3, ap4])

    graphics = Grafica(lista_persoane)