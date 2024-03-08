#a + b > c, a + c > b, i b + c > a
# 5. Napisati program kojim se proverava da li se može napraviti bašta u obliku trougla sa
# datim dužinama stranica.

# unese_stranicu_a = int(input("Unesite duzinu stranice a: "))
# unese_stranicu_b = int(input("Unesite duzinu stranice b: "))
# unese_stranicu_c = int(input("Unesite duzinu stranice c: "))

# if (a+b>c) and (a+c>b) and (b+c>a):
#   print("Moze da se napravi trougao")
# else:
#   print("Ne moze da se napravi trougao")

# 6. Vaš zadatak je da napravite program kojim provjeravate da li se pčela kreće po žici. Žica
# se može predstaviti pravom y = 2 * x + 5, dok se pčela predstavlja tačkom (x, y).


# koordinata_x = int(input("Unesite kordinatu x: "))
# koordinata_y = int(input("Unesite kordinatu y: "))

# izraz = 2 * koordinata_x + 5

# if izraz == koordinata_y:
#   print("Pcela je krecela po zici")
# else:
#   print("Pcela nije krecela po zici")


# 21. Napisati program koji za zadato x računa y i to na sledeći način:
# from math import sqrt
# x = int(input("Unesite x: "))

# if x <= -7:
#   y = -2*x + 7/2
# elif x > -7 and x < 1:
#   y = (x**2 - 3*x + 5) / (x**2 + 2)
# elif x >=1 and x <= 8:
#   y  = sqrt(x**2 + 2*x + 2) + sqrt(abs(1.5*x - 4/7))
# elif x > 8:
#   y = abs(3/x**2 - 11*x)

# print(y)


# 22. Za unijetu tačku sa koordinata (x,y) provjeriti kom kvadratnu pripada u koordinatnom
# sistemu.

# x = int(input("Unesite x: "))
# y = int(input("Unesite y: "))

# if x > 0 and y > 0:
#   print("I kvadrant")
# elif x < 0 and y > 0:
#   print("II kvadrant")
# elif x < 0 and y < 0:
#   print("III kvadrant")
# elif x>0 and y<0:
#   print("IV kvadrant")
# elif x == 0 and y != 0:
#   print("Tačka se nalazi na Y osi.")
# elif y == 0 and x != 0:
#   print("Tačka se nalazi na X osi.")
# else:
#   print("Tačka se nalazi u ishodištu.")


# 24. Ako tekst ima više od 30 karaktera skratiti ga tako da ostane tačno 30 karaktera, a na
# kraj skraćenog teksta dodati …

# tekst = input("Unesite tekst: ")

# while len(tekst) > 30:
#   tekst = tekst[:-1]

# print(tekst + "...")

# 25. Napisati program kojim se uklanja prvi i poslednji karakter teksta i štampa novi tekst.

# tekst = input("Unesite tekst: ")
# print(tekst[1:len(tekst)-1])

# 26. Napisati program koji provjerava da li je korsnik unio binarni, oktalni, dekadni ili
# heksadecimalni broj. Binarni broj ima prefiks 0b, oktalni 0o, heksadecimalni 0x, a
# dekadni nema prefiks.

# broj = input("Unesite broj: ")

# if broj.startswith("0b"):
#   print("Binarni")
# elif broj.startswith("0o"):
#   print("Oktalni")
# elif broj.startswith("0x"):
#   print("Heksadecimalni")
# else:
#   print("Dekadni")

# 27. Napisati program kojim provjeravati da li String sadrži bar jedan samoglasnik.
# string = input("Unesite string: ")

# for item in string:
#   if item in "aeiou":
#     print("Sadrzi samoglasnik")
#     break

# 28. Napisati program koji provjerava da li se string završava sa target stringom.
# Primjer 1: string:“Abcd”, target: “cd”, štampa se “Da”
# Primjer 2: string: “www.google.com”, target: “me”, štampa se “Ne”

# string = input("Unesite string: ")
# target = input("Unesite target: ")

# duzina = len(target)
# i = len(string) - duzina

# if string[i:len(string)] == target:
#   print("Da")
# else:
#   print("Ne")


# 29. Napisati program koji provjerava da li je uneseni string binarni broj (ima samo 0 ili 1).

# broj = input("Unesite broj: ")
# ind=0
# for item in broj:
#   if item != '0' and item != '1':
#     ind = 1

# if ind == 1:
#   print("Nije binarni broj")
# else:
#   print("Binarni broj")


# 30. Napisati program koji računa zbir parnih i proizvod neparnih brojeva od 1 do n. Broj n
# unosi korisnik.
# a. Štampati taj zbir i proizvod.
# b. Štampati koliko ima parnih, a koliko neparnih brojeva iz tog segmenta.

# n = int(input("Unesite broj:"))
# zbir=0
# proizvod=1
# parni = 0
# neparni = 0
# for item in range(1,n+1):
#   if item % 2 == 0:
#     zbir += item
#     parni += 1
#   else:
#     proizvod *= item
#     neparni += 1

# print(f"Zbir je {zbir}, a proizvod je {proizvod}")
# print(f"Parnih ima {parni}, a neparnih ima {neparni}")


# 31. Napisati program sa dva ulaza (korisnik unosi) start i end koji predstavljaju početak i kraj
# segmenta [start, end] (uključujući start i end), a koja kvadrira sve elemente iz tog
# segmenta koji su djeljivi sa 2 ali ne sa 4, a onda ih sumira. Štampati sumu.

# start = int(input("Unesite start: "))
# end = int(input("Unesite end: "))

# for item in range(start,end+1):
#   if item % 2 == 0 and item % 4 != 0:
#     item = item**2
#   print(item)


# 32. Napisati program koji za unijete vrijednosti a, b, djelilac vraća sumu i broj elemenata
# djeljivih sa djelilac iz segmenta (a, b) (a i b ne pripadaju intervalu)

# a = int(input("Unesite a: "))
# b = int(input("Unesite b: "))
# djelilac = int(input("Unesite djelilac: "))
# suma = 0
# brojac = 0
# for item in range(a+1,b):
#   if item % djelilac == 0:
#     suma += item
#     brojac += 1

# print(f"Suma je {suma}, a broj elemenata je {brojac}")

# 33. Napisati program koji sabira sve cifre unijetog broja.

# broj = int(input("unesite broj:"))
# sum = 0
# while broj != 0:
#   sum += broj % 10
#   broj //= 10

# print(sum)

# 34. Napisati program koji iz teksta izvlači cifre i računa njihov proizvod.

# string = input("Unesite string: ")
# proz = 1
# for item in string:
#   if item in "0123456789":
#     proz *= int(item)

# print(proz)

# 35. Napisati program koji vraća broj cifara u stringu i kreira od njih integer. Primjer: “Hi Mr.
# Rober53. How are you today? Today is 08.10.2019”, štampa 5308102019 i to kao
# integer. Pomoć: da provjerite da li je karakter broj koristiti isdigit metod.

# string = input("Unesite string: ")
# niz = []
# for item in string:
#   if item in "0123456789":
#     niz.append(item)

# for item in niz:
#   print(item, end="")
# # print(niz)

# Kreirati program koji unijeti string s (karakteri stringa alfabetski karakteri, mala slova)
# enkriptuje na sledeći način: ako je karakter suglasnik pretvara ga u 0, a ako je karakter
# samoglasnik pretvara ga u 1. Npr. za s = ‘abaae’ rezultat je 10111.


# 36. Kreirati program koji unijeti string s (karakteri stringa alfabetski karakteri, mala slova)
# enkriptuje na sledeći način: ako je karakter suglasnik pretvara ga u 0, a ako je karakter
# samoglasnik pretvara ga u 1. Npr. za s = ‘abaae’ rezultat je 10111.

# string = input("Unesite string: ")

# for item in string:
#   if item in "aeiou":
#     print(1, end="")
#   else:
#     print(0,end="")

# 37. Igrač nasumično bira listicu na kojoj se nalazi tekst sastavljen od karaktera 1, 0 i *.
# Karakter 1 nosi 1 poen, 0 nosi 0 poena, dok * nosi -1 poen. Napisati program koji
# provjerava da li je igrač u plusu.

# from random import randint
# #Uzeo sam da je duzina listica 10 karaktera
# duzina = 10 
# lista = []
# pomocna_lista = ['1','0','*']
# sum = 0
# for i in range(duzina):
#   rand_broj = randint(0,2)
#   if rand_broj == 0:
#     sum += 1
#   elif rand_broj == 1:
#     sum += 0
#   else:
#     sum -= 1

# if sum > 0:
#   print("Uzeo si plus")
# else:
#   print("Nisi u plusu")

# 38. Napisati program koji za unijeti string s (provjeriti da li je karakter cifra) enkriptuje na
# sledeći način: ako je karakter paran broj pretvara se u 0, a ako je karakter neparan broj
# pretvara se u 1. Npr. za s = ‘15023’ rezultat je 11001.


# string = input("Unesite string: ")

# for item in string:
#   if item in "02468":
#     print(0,end="")
#   else:
#     print(1,end="")

# 39. Narcissistic Number je broj čija suma cifara (tog broja) stepenova sa njegovim brojem
# cifara daje isti taj broj.
# Primjer 1: 153 (3 cifre)
# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

# broj = input("Unesite broj: ")
# stepen = len(broj)
# broj = int(broj)

# sum=0
# while broj != 0:
#   cifra = broj % 10
#   sum += cifra**stepen
#   broj //= 10

# print(sum)

# 40. Napisati program koji na osnovu niza cijelih brojeva računa apsolutnu sumu svih
# negativnih parnih elemenata za unijeti niz. Štampati sumu.
# Primjer:
# Input: [-2, 7, -5, 3, 1, -4]
# Output: 6 (|-2| + |-4|)

# niz = [-2, 7, -5, 3, 1, -4]
# sum = 0
# for item in niz:
#   if item < 0 and item % 2 == 0:
#     item *= -1
#     sum += item

# print(sum)