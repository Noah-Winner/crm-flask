import json
try:
    with open("kunden.json", "r") as datei:
        kunden = json.load(datei)
except:
    kunden = []

def linien_einfach():
    print("-" * 40)

def linien_doppelt():
    print("=" * 40)

def kunde_hinzufügen():
    name = input("Name: ")
    email = input("Email: ")
    telefon = input("Telefonnummer: ")
    kunde = {
        "name": name,
        "email": email,
        "telefon": telefon
        }
    kunden.append(kunde)
    with open("kunden.json", "w") as datei:
        json.dump(kunden, datei)
        linien_einfach()
    print("Kunde erfolgreich hinzugefügt.")

def kunde_suchen():
    name = input("Name: ")
    gefunden = False
    for kunde in kunden:
        if kunde["name"] == name:
            linien_einfach()
            print(f"Name: {kunde['name']}")
            print(f"Email: {kunde['email']}")
            print(f"Telefonnummer: {kunde['telefon']}")
            linien_einfach()
            gefunden = True
            break
    if gefunden == False:
        print("Dieser Kunde existiert nicht.")
        print("Möglicherweise enthält der Name einen Rechtschreibungsfehler.") 

def kunde_anzeigen():
    gefunden = False
    for kunde in kunden:
        linien_einfach()
        print(f"Name: {kunde['name']}")
        print(f"Email: {kunde['email']}")
        print(f"Telefonnummer: {kunde['telefon']}")
        linien_einfach()
        gefunden = True
    if gefunden == False:
        print("Es sind noch keine Kunden gespeichert.")

def kunde_loeschen():
    name = input("Name: ")
    gefunden = False
    for kunde in kunden:
        if kunde["name"] == name:
            kunden.remove(kunde)
            with open("kunden.json", "w") as datei:
                json.dump(kunden, datei)
            gefunden = True
            print("Der Kunde wurde erfolgreich gelöscht.")
            break
    if gefunden == False:
        linien_einfach()
        print("Dieser Kunde existiert nicht.")

def kunde_bearbeiten():
    name = input("Name: ")
    gefunden = False
    for kunde in kunden:
        if kunde["name"] == name:
            print(f"Name: {kunde['name']}")
            print(f"Email: {kunde['email']}")
            print(f"Telefonnummer: {kunde['telefon']}")
            neuer_name = input("Neuer Name: ")
            neue_email = input("Neue Email: ")
            neues_telefon = input("Neue Telefonnummer: ")
            kunde["name"] = neuer_name
            kunde["email"] = neue_email
            kunde["telefon"] = neues_telefon
            with open("kunden.json", "w") as datei:
                json.dump(kunden, datei)
            gefunden = True
            linien_einfach()
            print("Der Kunde wurde erfolgreich bearbeitet.")
            break
    if gefunden == False:
        linien_einfach()
        print("Dieser Kunde existiert nicht.")


while True:
    linien_doppelt()
    print("         Kundenmanagementsystem")
    linien_doppelt()
    print("1 - Kunde hinzufügen")
    print("2 - Kunde suchen")
    print("3 - Kunden anzeigen")
    print("4 - Kunde löschen")
    print("5 - Kunde bearbeiten")
    print("6 - Beenden")
    linien_einfach()
    auswahl = input("Auswahl: ")

    if auswahl == "1":
        kunde_hinzufügen()

    elif auswahl == "2":
        kunde_suchen()
     

    elif auswahl == "3":
        kunde_anzeigen()

    elif auswahl == "4":
        kunde_loeschen()

    elif auswahl == "5":
        kunde_bearbeiten()

    elif auswahl == "6":
        break