telefonbok = []
person1 = {
    "navn": "Oskar",
    "nummer": "20349567"
}
person2 = {
    "navn": "Peter",
    "nummer": "54483920"
}
telefonbok.append(person1)
telefonbok.append(person2)

def vis_alle():
    for person in telefonbok:
        print(f"{person["navn"]}: {person["nummer"]}")

def legg_til():
    nyttnavn = input("Skriv nytt navn: ")
    nyttnummer = input("Skriv inn nummer: ")
    nyttordbok = {
        "navn": nyttnavn,
        "nummer": nyttnummer
    }
    telefonbok.append(nyttordbok)
    print(f"{nyttnavn} ble lag til i telefonboka.")

def søk():
    funnet = False
    søknavn = input("Skriv inn navn du vil søke opp: ")
    søknavn.lower()
    funnetnummer = ""
    for person in telefonbok:
        if person["navn"] == søknavn:
            funnet = True
            funnetnummer = person["nummer"]
    if funnet:
        print(f"{søknavn}: {funnetnummer}")
    else:
        print(f"{søknavn} har ikke blitt funnet.")

while True:
    print("1. Vis alle")
    print("2. Legg til ny")
    print("3. Søk")
    print("4. Avslutt")
    svar = input("Hva vil du gjøre?")
    svar.lower()
    if svar == "1" or svar == "vis":
        vis_alle()
    elif svar == "2" or svar == "legg":
        legg_til()
    elif svar == "3" or svar == "søk":
        søk()
    elif svar == "4" or svar == "stopp":
        print("Programmet avsluttes.")
        break
    else:
        print("ERROR: Feil kommando.")
