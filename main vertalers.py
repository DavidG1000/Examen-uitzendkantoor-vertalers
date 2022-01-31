# https://github.com/DavidG1000/Examen-uitzendkantoor-vertalers.git
# ######  Examen David Gregoor ########

"""Opdracht: Een uitzendkantoor voor vertalers/tolken heeft 2 vestigen: Limburg, Antwerpen. Voor elke
vestiging is een dictoinary met als naam de vertalers_provincie. Op de volgende pagina vind je de
vertalers en hun talen"""

import module_vertalers
import sys  # nodig voor de break
from tabulate import tabulate

# Hoofd deel 1 : kies uit welke provincie
def keuze_lijst():
    print()
    print("1. Lijst vertalers Limburg")
    print("2. Lijst vertalers Antwerpen")
    print("3. Toon lijst alle vertalers")

# Functie druk alle vertalers af
def alle_vertalers(dictio):
    headers = ["Naam", "Provincie","Moedertaal","Talen","Beschikbaar"]
    dictio = [[name, *inner.values()] for name, inner in dictio.items()]
    print("")
    print(tabulate(dictio, headers=headers, tablefmt="grid"))
    print("")
    main()


def Merge(dict1, dict2):
    return(dict2.update(dict1))


# Hoofd. deel 2 druk het keuze menu af
def keuze_menu():
    print("1.Tonen alle vertalers")
    print("2.Tonen beschikbare vertalers")
    print("3.Tonen beschikbare vertalers op taalkeuze")
    print("4.Vertaler toevoegen")
    print("5.Vertaler verwijderen")
    print("6.Voeg taal toe aan vertaler")
    print("7.Reserveer vertaler")


# 1a.Druk items af
def tonen(dictio):
    for naam, vertaler_info in dictio.items():
        print("\nNaam :", naam)
        for key in vertaler_info:
            print(key + ":", vertaler_info[key])
    main()

# 1b. Druk uitgebreid af
def uitgebr_tonen(dictio):
    headers = ["Naam", "Provincie", "Moedertaal", "Talen","Beschikbaar"]
    dictio = [[name, *inner.values()] for name, inner in dictio.items()]
    print("")
    print(tabulate(dictio, headers=headers, tablefmt="grid"))
    print("")
    main()

# 2.Toon beschikbare vertalers
def beschikb_vertalers(dictio):
    teller = 0
    for naam, vertaler_info in dictio.items():
        if dictio[naam]["Beschikbaar"] == "Ja":
            teller = 1
            print("\nNaam :", naam)
            for key in vertaler_info:
                print(key + ":", vertaler_info[key])
    if teller == 0: print("Geen enkele vertaler is beschikbaar")
    main()

# 3.Toon beschikbare vertalers op taal
def beschikb_vertalers_op_taal(dictio):
    teller = 0
    taal_keuze=input("Op welke taal wil u filteren ? ")

    for naam, vertaler_info in dictio.items():
        if taal_keuze in vertaler_info["Talen"]:
            if dictio[naam]["Beschikbaar"] == "Ja":
                teller = 1
                print("\nNaam :", naam)
                for key in vertaler_info:
                    print(key + ":", vertaler_info[key])
    if teller == 0: print("Geen enkele vertaler is beschikbaar")
    main()

# 4.Voeg nieuwe vertaler toe
def toevoegen(dictio):
    naam = input("Geef de naam van de vertaler in :")
    moedertaal = input("Geef de moedertaal van " + naam + " in: ")
    dictio[naam] = {"Moedertaal": moedertaal}
    for namen in dictio.items():
        print(namen)
    print("Naam: " + naam + " is toegevoegd.")
    main()

# 5.verwijderd een item uit de lijst
def verwijder(dictio):
    for namen in dictio.items():
        print(namen)
    naam = input("Geef de naam die je wenst te verwijderen: ")
    if naam in dictio.keys():
        bevestiging = input("Bent u zeker dat u vertaler " + naam + " wil verwijderen j/n ?")
        if bevestiging == "j":
            dictio.pop(naam)
            print("Vertaler " + naam + " is weg uit de lijst")
    else:
        print("Wagennr. " + naam + " is niet in de lijst")

    main()

# 6. Voeg taal toe aan vertaler
def aanpassen(dictio):
    for namen in dictio.items():
        print(namen)
    aan_te_passen_key = input("Aan welke naam wil u talen toevoegen: ")
    if aan_te_passen_key in dictio:
        keuze_taal = input('Welke taal wil je toevoegen: ')
        if keuze_taal not in dictio[aan_te_passen_key]:
            dictio[aan_te_passen_key]["Talen"].append(keuze_taal)
            for namen in dictio.items():
                print(namen)
            print("Taal is toegevoegd")
        else:
            print(aan_te_passen_key + " kent deze taal al")

    else:
        print("Naam staat niet in de lijst")
    main()

# 7. Reserveer vertaler
def reserveer_vertaler(dictio):
    for naam in dictio.items():
        print(naam)
    keuze = ""
    while not keuze == 0:
        keuze = input("Geef de vertaler die u wil reserveren of '0' om te stoppen ? ")
        if not keuze == 0:
            if dictio[keuze]["Beschikbaar"] == "Ja":
                print("Deze persoon is niet beschikbaar.")
            else:
                dictio[keuze]["Beschikbaar"] = "Nee"
                print("\nVertaler :", keuze, " is nu gereserveerd.")

    main()


# hoofdprogramma
def main():
    keuze_lijst()
    lijst_kiezen = input("Maak een keuze welke provincie of 'stop' om te stoppen (1-2) : ")
    print()

    if lijst_kiezen == "1":
        dictio = module_vertalers.vertalers_limburg
    elif lijst_kiezen == "2":
        dictio = module_vertalers.vertalers_antwerpen
    elif lijst_kiezen == "3":
        dictio = module_vertalers.vertalers_limburg # alleen de lijst van limburg. Samenvoegen is niet gelukt met update
        alle_vertalers(dictio)
    elif lijst_kiezen == "stop": sys.exit()

    keuze_menu()
    keuze = input("Maak een keuze 1-7 : ")
    if (keuze == "1"):
        uitgebr_tonen(dictio)
    elif (keuze == "2"):
        beschikb_vertalers(dictio)
    elif (keuze == "3"):
        beschikb_vertalers_op_taal(dictio)
    elif (keuze == "4"):
        toevoegen(dictio)
    elif (keuze == "5"):
        verwijder(dictio)
    elif (keuze == "6"):
        aanpassen(dictio)
    elif (keuze == "7"):
        reserveer_vertaler(dictio)

main()




