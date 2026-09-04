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