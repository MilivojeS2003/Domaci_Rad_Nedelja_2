# 81. Napisati program koji analizira promjene cijena akcija. Program treba da učita niz cijena akcija za određeni period, a zatim izračuna i ispiše najveći pad i najveći porast cijena za susjedne vrijednosti.

# cijena_akcija = 360
# cijene = [100,200,300,400,500,600,700,800,900]

# max_pad = 0
# max_porast = 0

# for item in cijene:
#   if item > cijena_akcija:
#     pad = item - cijena_akcija
#     if pad > max_porast:
#       max_porast = pad
#   elif item <cijene_akcija:
#     pad = cijena_akcija - item
#     if pa > max_pad:
#       max_pad = pad

# print(max_pad,max_porast)

# 82. Pretpostavite da imate listu koja predstavlja broj slobodnih sjedišta u svakom redu u
# pozorištu. Na primjer, ako pozorište ima 5 redova, lista može izgledati ovako: [10, 8, 15,
# 12, 7], gdje svaki broj predstavlja broj slobodnih sjedišta u tom redu (listu unosi korisnik).
# Napisati program koji pronalazi najbolji red za grupu od n osoba koje mogu sjesti
# zajedno (n unosi korisnik). Smatrati da je najbolji onaj red u kome ostane najviše
# slobodnih mjesta nakon što se smjesti n osoba.
  
# lista = [10, 8, 15, 12, 7]

# n = int(input("Unesite broj osoba: "))

# max = 0

# for item in lista:
#   if item > max:
#     max = item

# if max < n:
#   print("nema dovoljno slobodnih mjesta za jedan red")
# else:
#   red = lista.index(max)
#   print(f"najbolji red ima {red} slobodnih mjesta") #ako se redovi racunaju od 0, ako ne treba dodati +1
#   lista[red] -= n

# print(lista)

# 83. Nakon napornog perioda studiranja odlučili ste da odete na kratko putovanje. Na sajtu
# putovanja.me postavljene su razne destinacije sa cijenama. Izbor je velik ali vaš budžet
# je ograničen. Odlučili ste da potrošite gotovo sav novac kojim raspolažete na ovo
# putovanje, pa ste odabrali onu destinaciju koja je najskuplja ali u skladu sa
# mogućnostima. Cijene destinacija se čuvaju u listi. Koliko budžeta vam ostaje na
# raspolaganju nakon uloženog novca.

# budzet = 1000
# cijene_destinacija = [300, 500, 700, 1000, 200]

# najskuplja_destinacija = max(cijene_destinacija)
# novi_budzet = budzet - najskuplja_destinacija

# print(novi_budzet)

# 84. Pretpostavite da imate restoran sa različitim stolovima različitih kapaciteta (npr. [4, 6, 2,
# 8, 5] mjesta po stolu). Večeras imate najavu da ćete imati više gostiju nego slobodnih
# mjesta u restoranu (unosite broj gostiju). Napišite program kojim računate koliko stolova
# je potrebno dodatno nabaviti ako se zna da uz svaki novi sto dolaze 4 stolice.

# broj_stolica = [4,6,2,8,5]
# broj_gostiju = int(input("Unesite broj gostiju: "))
# ukupno = sum(broj_stolica)
# if broj_gostiju > ukupno:
#   visak_gostiju = broj_gostiju - ukupno
#   visak_stolova = visak_gostiju / 4
#   if visak_stolova.is_integer():
#     print(f"Potrebno je dodati {visak_stolova} stolova")
#   else:
#     visa_stola = (visak_gostiju // 4)+1
#     print(f"Potrebno je dodati {visa_stola} stolova")

# 85. Napisati program koji za listu koja pokazuje broj slobodnih sjedišta u svakom redu
# bioskopa određuje koliko redova je potrebno rezervisati za grupu od n posjetilaca.
# Idealno je zauzeti što manje redova.

#   slobodna_sjedista = [20, 15, 25, 30, 10]
#   n = 50

#   slobodna_sjedista.sort() 

#   broj_redova = 0
#   ukupno_sjedista = 0

#   for sjedista_u_redu in slobodna_sjedista:
#       if ukupno_sjedista < n:
#           ukupno_sjedista += sjedista_u_redu
#           broj_redova += 1
#       else:
#           break

#   print("Potrebno je rezervisati", broj_redova, "redova za grupu od", n, "posjetilaca.")

# 86. Napisati program absolute_of_even_sum koji ima jedan parametar, niz cijelih brojeva,
# a koja računa apsolutnu sumu svih negativnih parnih elemenata za unijeti niz. Štampati
# sumu.
# Input: [-2, 7, -5, 3, 1, -4] Output: 6 (|-2| + |-4|)

# def absolute_of_even_sum(niz):
#   suma = 0
#   for broj in niz:
#       if broj < 0 and broj % 2 == 0:
#           suma += abs(broj)
#   return suma


# niz = [-2, 7, -5, 3, 1, -4]
# print(absolute_of_even_sum(niz))

# 87. Napisati program presjek (a, b) koji za unijete liste a i b vraća listu zajedničkih elementa
# liste a i liste b. Elementi liste a i liste b su brojevi ili stringovi.
# Input 1: a = [1,2, ’a’], b = [‘a’, 2] Output 1: [2, ‘a’]
# Input 2: a = [2, 3, 4], b = [1, 1, 7] Output 2: []

# def presjek(a,b):
#   lista = []
#   for item in a:
#     if item in b:
#       lista.append(item)
#   return lista

# a = [1,2,3]
# b = [4, 2]
# print(presjek(a,b))

# 88. Napisati program br_elemenata(a, max) koji za unijetu listu a vraća broj elemenata koji
# su manji od max iz te liste. Napomena: lista sadrži samo cijele brojeve.
# Input 1: a = [1,2,3], max = 3 Output 1: 2
# Input 2: a = [2, 3, 4], max = 7 Output 2: 3
# Input 3: a = [-1, 0, 5], max = -2 Output 3: 0

# def br_elemenata(a,max):
#   broj = 0
#   for item in a:
#     if item < max:
#       broj += 1
#   return broj

# a = [1,2,3]
# print(br_elemenata(a,3))

# 89. Napisati program br_elemenata(a) koji za unijetu listu elemenata (cijeli brojevi, bez nule)
# a vraća broj elemenata koji imaju suprotnu vrijednost. Broju x, suprotan broj je -x.
# Smatrati da se broj pojavljuje jednom i da nekad ima svoju suprotnu vrijednost, a nekad
# nema. Input 1: [1, 2, -1, 3, -3] Output: 2 Input 2: [20, 10, -10, 100] Output: 1

# def br_elemenata(a):
#   broj = 0
#   for item in a:
#     if item != 0:
#       if -item in a:
#         broj +=1
#   if broj > 0:
#     return broj/2
#   else:
#     return 0

# a = [1,2,-1,3,-3]
# print(br_elemenata(a))

# 90. Napisati program update_list(a, x) koji za unijetu listu elemenata (cijeli brojevi) a uvećava
# svaki parni element za vrijednost x. Parametar x je prirodan broj.
# Input 1: [1, 2, -1, 3, -4], 3 Output: [1, 5, -1, 3, -1]
# Input 2: [21, 10, -10, 100], 5 Output: [21, 15, -5, 105]

# def update_list(a,x):
#   for i in range(0,len(a)):
#     if a[i] % 2 == 0:
#       a[i] += x
#   return a

# a = [1,2,-1,3,-4]
# print(update_list(a,3))

# 91. Napisati program second_max(a) koji nalazi drugi najveći element liste a. Npr. ako je a =
# [1, 22, 33] rezultat je 22. Napomena: lista ima bar 2 elem

# def second_mac(a):
#   a.sort()
#   return a[-2]

# a = [1,22,33]
# print(second_mac(a))

# 92. Napisati program koji omogućava korisniku da unese n proizvoda (n parametar funkcije).
# Svaki proizvod se predstavlja sa kao dictionary oblika: {naziv, opis, cijena, broj_artikala}.
# Funkcija treba da vrati listu proizvoda. Nakon toga, napisati funkciju koja ima dva
# parametra i to proizvodi, search_term, a koja vraća sve proizvode čiji naziv počinje sa
# vrijednošću parametra search_term.
# proizvodi_test = [
#     {"naziv": "Laptop", "opis": "Prijenosno računalo", "cijena": 1500, "broj_artikala": 10},
#     {"naziv": "Monitor", "opis": "Računalni monitor", "cijena": 300, "broj_artikala": 20},
#     {"naziv": "Miš", "opis": "Bežični miš", "cijena": 30, "broj_artikala": 50},
#     {"naziv": "Tipkovnica", "opis": "Računalna tipkovnica", "cijena": 50, "broj_artikala": 30},
#     {"naziv": "Slušalice", "opis": "Bežične slušalice", "cijena": 80, "broj_artikala": 25}
# ]
# lista = []
# n = int(input("Unesite broj proizvoda: "))
# i=0
# while i < n:
#   naziv = input("Unesite naziv proizvoda: ")
#   opis = input("Unesite opis proizvoda: ")
#   cijena = int(input("Unesite cijenu proizvoda: "))
#   broj_artikala = int(input("Unesite broj artikala: "))
#   proizvod = {"naziv":naziv, "opis":opis, "cijena":cijena, "broj_artikala": broj_artikala}
#   lista.append(proizvod)
#   i+=1
# print(proizvodi_test[0]["naziv"])

# def proizvodi(proizvodi, search_term):
#   svi_nadjeni = []
#   for proizvod in proizvodi:
#     if proizvod["naziv"].startswith(search_term):
#       svi_nadjeni.append(proizvod)
#   return svi_nadjeni

# print(proizvodi(proizvodi_test, "Laptop"))


# 93. Napisati program koji kao parametar prima listu igrica oblika (ime:String, izdavac:String,
# godina_izlaska:Integer, ocjena:Float), a vraća igrice čija je ocjena veca od ocjene x
# (unosi korisnik sa input), a cije je izdavac y (unosi korisnik sa input). Koristiti list
# comprehension pristup.


# lista_proizvoda = [
#     {"ime": "The Great Gatsby", "izdavac": "Scribner", "godina_izlaska": 1925, "ocjena": 4.2},
#     {"ime": "To Kill a Mockingbird", "izdavac": "J. B. Lippincott & Co.", "godina_izlaska": 1960, "ocjena": 4.5},
#     {"ime": "1984", "izdavac": "Secker & Warburg", "godina_izlaska": 1949, "ocjena": 4.6},
#     {"ime": "The Catcher in the Rye", "izdavac": "Little, Brown and Company", "godina_izlaska": 1951, "ocjena": 4.1}
# ]

# def cijena(lista,x,y):
#   new_list = []
#   for item in lista:
#     if item["ocjena"] >= x and item["izdavac"] == y:
#       print(item["ime"])


# cijena(lista_proizvoda, 4.5, "J. B. Lippincott & Co.")
# cijena(lista_proizvoda, 4.5, "Secker & Warburg")

# 94. Napisati program koji za unijeti string i slovo vraća sve riječi čija je dužina paran broj, a
# ne sadrže zadato slovo (koje korisnik unosi). Primjer: get_ewfbyr(“words with even
# number of letters without character d”, “d”) Output: [“with”, “even”, “number”, “of”]
# string = "words with even number of letters without character d"
# slovo = "d"
# def get_ewfbyr(string,slovo):
#   novi_string = ""
#   lista = []
#   for item in string:
#     if item != " ":
#       novi_string += item
#     else:
#       if len(novi_string) % 2 == 0 and slovo not in novi_string:
#         lista.append(novi_string)
#       novi_string = ""
#   print(lista)
# get_ewfbyr(string,slovo)

# 95. Napisati program longest_increasing koji ima jedan parametar i to input_list (predstavlja
# listu cijelih brojeva), a nalazi najdužu neopadajuću podlistu pozitivnih cijelih brojeva
# (brojevi veći od 0) i vraća tu podlistu
# Primjer:
# Input: [1, 2, 3, -1, 0, 5, 6, 7, 10, 10, 1]
# Output: [5, 6, 7, 10, 10]

# def longest_increasing(input_list):
#   najduza_lista = []
#   trenutna_lista = []

#   for i in range(len(input_list) - 1):  
#       if input_list[i] < input_list[i + 1]:
#           trenutna_lista.append(input_list[i])
#       else:
#           trenutna_lista.append(input_list[i])  
#           if len(najduza_lista) < len(trenutna_lista):
#               najduza_lista = trenutna_lista[:]  
#           trenutna_lista = []

#   trenutna_lista.append(input_list[-1])  
#   if len(najduza_lista) < len(trenutna_lista):
#       najduza_lista = trenutna_lista[:] 

#   return najduza_lista


# a = [1, 2, 3, -1, 0, 5, 6, 7, 10, 10, 1]
# print(longest_increasing(a))

# 96. Napisati program koji ima dva parametra string i number gdje prvi parametar predstavlja
# ulazni string, dok number predstavlja broj na osnovu koga se radi razbijanje stringa na
# podstringove. Funkcija treba da vrati niz/listu podstringova zadate dužine. Ako poslednji
# podstring ne sadrži dovoljno karaktera dopuniti ga sa *. Napomena: space se takođe
# računa kao karakter.
# Primjer 1:
# split_string(“danas polažemo test”, 5) -> [“danas”, “ pola”, “žemo ”, “test*”]
# Primjer 2:
# split_string(“kurs web program.”, 6) -> [“kurs w”, “eb pro”, “gram.*”]
# Primjer 3:
# split_string(“da”, 7) -> [“da*****”]

# def split_string(string, number):
#   num_substrings = len(string) // number
#   if len(string) % number != 0:
#       num_substrings += 1

#   substrings = []
#   for i in range(num_substrings):
#       start_index = i * number
#       end_index = min((i + 1) * number, len(string)) 
#       substring = string[start_index:end_index]
#       if len(substring) < number:  
#           substring += "*" * (number - len(substring))
#       substrings.append(substring)

#   return substrings


# print(split_string("danas polazemo test", 5))
