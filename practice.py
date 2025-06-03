ime_korisnika = input("Svoje ime: ")
emil_korisnika = input("Svjo email: ")
sifra_korisnika = input("Svoja sifra: ")

ime_korisnika = ime_korisnika.strip()
broj_razmaka = ime_korisnika.count(" ")
ime_korisnika = ime_korisnika.lower()
ime_korisnika = ime_korisnika.title()

razmak = ime_korisnika.find(" ")
first_name = ime_korisnika[:razmak]
last_name = ime_korisnika[razmak+1:]

lokacija_imena = sifra_korisnika.lower().find(first_name.lower())

if broj_razmaka > 0 :
    print("Ime je potpuno")
else :
    print("Greska - ime je nepotpuno")

duzina_sifre = len(sifra_korisnika)

if duzina_sifre > 8 :
    print("Sifr je OK")
else :
    print("Sifra mora biti duza od 8  karaktera")   












































# print ( 8 / 5);

# # Addition and division
# print(4 + 5)
# print(10 / 2)

# # Subtraction
# print()

# # Multiplication//

# height = 1.79
# weigth = 74.2 # <-
# bmi = weigth / height ** 2
# print(bmi)

# ////

# godine = input("Koliko imas godina: ")
# godine = int(godine)

# if  godine >= 18 :
#     print("Punoljetni ste")
# else :
#     print("Maloljetni ste")

# /////////////////////////////////////////////////////////////////////////////

# broj1 = input("Broj 1: ")
# broj2 = input("Broj 2: ")

# broj1 = int(broj1)
# broj2 = int(broj2)

# rezultat = broj1 + broj2

# print(rezultat)

# /////////////////////////////////////////////////////////////////

# cijeli_broj = 10
# negativan_broj = -5
# decimalniBroj = 3.65
# moje_ime_tekst = "Cysecor"
# moje_ime_tekst2 = 'Cysecor'
# punoljetan = True
# maloljetan = False

# print("Moje ime je:", moje_ime_tekst, "i ovo je cijeli broj:", cijeli_broj)

# # print("Moje ime je: {} i ovo je cijeli broj: {}".format(moje_ime_tekst, cijeli_broj))
# print(f"Moje ime je: {moje_ime_tekst} i ovo je cijeli broj: {cijeli_broj}")
# # ///////////////////