ime_korisnika = input("Svoje ime: ")
email_korisnika = input("Svoj email: ")
sifra_korisnika = input("Svoja sifra: ")

ime_korisnika = ime_korisnika.strip()
broj_razmaka = ime_korisnika.count(" ")
ime_korisnika = ime_korisnika.lower()
ime_korisnika = ime_korisnika.title()

razmak = ime_korisnika.find(" ")
first_name = ime_korisnika[:razmak]
last_name = ime_korisnika[razmak+1:]

lokacija_imena = sifra_korisnika.lower().find(first_name.lower())
# print(lokacija_imena)
if broj_razmaka > 0 :
    print("Ime je potpuno")
else :
    print("Greska - ime je nepotpuno")

duzina_sifre = len(sifra_korisnika)

if duzina_sifre > 8 :
    print("Sifra je OK")
else :
    print("Nije ok")

# ////