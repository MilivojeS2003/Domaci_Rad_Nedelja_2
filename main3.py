# 41. Napisati program koji za unijetu listu L i vrijednost max vraća broj elemenata koji su
# manji od max iz te liste. Napomena: lista sadrži samo cijele brojeve
# Input: a = [1,2,3], max = 3; Output: 2
# Input: a = [-1, 0, 5], max = -2; Output: 0

# a = [1,23,5,3,5,6,7-12]
# max = int(input("Unesite max: "))
# brojac = 0

# for item in a:
#   if item < max:
#     brojac += 1

# print(brojac)


# 42. Dat je niz koji sadrži cijene proizvoda u jednom marketu. Market je za ovu nedelju odluči
# da spusti cijene svim proizvodima. Kolika će zarada marketa od tih proizvoda biti manja
# u odnosu na originalnu cijenu.

# niz_cijena = [12,13,19,83,10,1,3]
# popust = int(input("Unesite popust: "))
# popust = popust/100
# niz_nove_cijene = []

# for item in niz_cijena:
#   item *= popust
#   niz_nove_cijene.append(item)

# razlika_u_ceni = sum(niz_cijena) - sum(niz_nove_cijene)
# print(razlika_u_ceni)


# 43. Data je lista ocjena na predmetu likovno za sve učenike jednog odjeljenja osnovne
# škole. Ispostavilo se da nema učenika koji imaju ocjenu 1 i 2. Prebrojati koliko učenika
# ima ostale ocjene (za svaku ocjenu pojedinačno).

# niz_ocjena = [3,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,3,3,3,4,4,4]
# ocjena_3 = 0
# ocjena_4 = 0
# ocjena_5 = 0
# for item in niz_ocjena:
#   if item == 3:
#     ocjena_3 += 1
#   elif item == 4:
#     ocjena_4 += 1
#   elif item == 5:
#     ocjena_5 += 1

# print(f"Ocjena 3 ima {ocjena_3}, ocjena 4 ima {ocjena_4}, ocjena 5 ima {ocjena_5}")


# 44. Data je lista koja sadrži broj posjeta za poslednjih deset fudbalskih utakmica. Napisati
# program koji štampa koliko je bilo najviše posjeta u jednom danu.

# broj_posjeta = [10000,20000,3000,400,0,12300,12000]

# broj_posjeta.sort()
# duzina = len(broj_posjeta)
# max = broj_posjeta[duzina-1]
# print(max)

# 45. Kreirati program koji prikazuje koliko ima zaposlenih koji imaju veće plate od prosječne
# plata. Npr. ako su plate = [500, 600, 700] rezultat je 1 jer je samo plata od 700 EUR
# iznad prosječne plate

# plate = [200,100,1000,300,2000,550]
# prosjek = sum(plate) / len(plate)
# brojac = 0
# for item in plate:
#   if item > prosjek:
#     brojac += 1

# print(brojac)


# 46. Kreirati program koji nalazi platu zaposlenog koji ima drugo najveće primanje. Npr. ako
# je plate = [540,690, 900] rezultat je 690. Napomena: lista ima bar 2 elementa

# plate = [200,100,1000,300,2000,550]
# plate.sort()
# duzina = len(plate)
# drugi_najveci = plate[duzina - 2]
# print(drugi_najveci)


# 47. Korisnik unosi tri broja. Naći minimum i maksimum među unijetim brojevima i rezultat
# prikazati korisniku.

# a = int(input("Unesite broj 1: "))
# b = int(input("Unesite broj 2: "))
# c = int(input("Unesite broj 3: "))

# niz = [a,b,c]
# niz.sort()
# print(f"najveci el. niza je {niz[2]}, a najmanji {niz[0]}")


# 48. Napisati program koji račun X**n koristeći petlju (bez ugrađenog Python operatora za
# stepenovanje)

# x = int(input("Unesite broj x: "))
# n = int(input("Unesite stepen n: "))
# proz = 1
# for i in range(1,n+1):
#   proz *= x

# print(proz)

# 49. Napisati program koji skraćuje string do unijete dužine. Na kraj stringa dodati ... Ako je
# unijeza dužina veća od same dužine stringa, na kraju stringa dodati samo ...
# Primjer 1:
# string: “abcde”, duzina: 2, štampa se “ab...”
# Primjer 2:
# string: “abcde”, duzina: 10, štampa se “abcde...”

# x = int(input("Duzina niza: "))
# string = input("Unesite string: ")
# string = string[:x]
# string +="..."
# print(string)

# 50. Napisati program koji iz zadatog stringa izdvaja samo samoglasnike i vraća taj novi
# string.

# string = input("Unesite string: ")
# new_string = ""
# for item in string:
#   if item in "aeiou":
#     new_string += item
# print(new_string)

# 51. Lozinka je jaka ako je njena dužina najmanje 8 simbola, i sadrži mala slova, velika slova
# i cifre. Napisati program koji provjerava da li je lozinka jaka. Ulaz: Unosi se jedna riječ,
# dužine ne veće od 100, koja sadrži mala i velika slova i cifre. Izlaz: Štampati YES ili NO.

# mala_slova = 0
# velika_slova = 0
# cifre_slova = 0

# string = input("Unesite string: ")

# for item in string:
#   if item.islower():
#     mala_slova = 1
#   elif item.isupper():
#     velika_slova = 1
#   elif item in "0123456789":
#     cifre_slova = 1

# if mala_slova == 1 and velika_slova == 1 and cifre_slova == 1:
#   print("YES")
# else:
#   print("NO")


# 52. Napisati program koji na osnovu varijabli a, pre, sub i num dodaje prefiks pre, i sufiks suf
# stringu a num puta i vraća novi prošireni string.
# Input 1: a = ‘test’, pre = ‘pr’, suf = ‘su’, num = 2;
# Output 1: ‘prprtestsusu’

# string = input("Unesite string: ")
# prefiks = input("Unesite prefiks: ")
# sufiks = input("Unesite sufiks: ")
# ponavljanja = int(input("Unesite broj ponavljanja: "))
# new_string = ""
# i=0
# while i != ponavljanja:
#   new_string += prefiks
#   i += 1

# new_string += string
# i=0

# while i != ponavljanja:
#   new_string += sufiks
#   i += 1

# print(new_string)

# 53. Fudbal – Petar je posmatrao fudbalsku utakmicu i na papiru zapisivao rezultat sa
# semafora poslije svakog gola. Npr. mogući zapis je: 1:0, 1:1, 1:2, 2:2, 2:3. Zatim je Petar
# sabrao sve zapisane brojeve: 1+0+1+1+1+2+2+2+2+3=15. Na osnovu datog zbira,
# napišite program koji određuje koliko je golova bilo na utakmici. Ulaz: U jednom redu dat
# je cio broj N – Petrov zbir (1 ≤ N ≤1000). Izlaz: Štampati jedan cio broj – broj golova.




# 54. Dat je string sastavljen od karaktera 0 i 1. Karakter 0 predstavlja slobodno polje, a 1
# predstavlja zauzeto polje. Vaš zadatak je da za zadatu poziciju u stringu provjerite da li
# su susjedna polja slobodna (lijevo i desno). Napomena: za prvo polje gledate same
# desno polje, za poslednje polje samo lijevo polje, a za ostala i lijevo i desno polje. Npr.
# ako je string 01010, a zadata pozicija 2 (indeksiranje kreće od nule), treba štampati 0 jer
# nema slobodnih polja.

# string = input("unesite string: ")
# pozicija = int(input("unesite poziciju: "))
# duzina = len(string)

# if pozicija == 0 and string[0] == '1' and string[1] == '0':
#   print("1")
# elif pozicija == duzina-1 and string[duzina-1] == '1' and string[duzina-2] == '0':
#   print("1")
# elif string[pozicija] == '1' and string[pozicija-1] == '0' and string[pozicija + 1]:
#   print("1")
# else:
#   print("0")

# 55. Napisati program koji za 2 data prirodna broja h i o koji redom predstavljaju broj
# molekula vodonika (H) i kiseonika (O), vraća koliko se najviše molekula vode (H2O)
# može dobiti od datih molekula. Npr., ako je h=4, o=3 odgovor je 2.

# h = int(input("Unesite broj molekula vodonika: "))
# o = int(input("Unesite broj molekula kiseonika: "))

# moguci_zbir = h // 2
# print(h,o)
# if h < 1 or o < 1:
#   print(0)
# elif o <= moguci_zbir:
#   print(o)
# else:
#   print(moguci_zbir)


# 56. Napisati program kojim za unijeti string provjeravate koliko ima jednocifrenih negativnih
# brojeva. String se sastoji od negativnih i pozitivnih brojeva i oznaka za negativne (-) i
# pozitivne (+). Primjer: +23-2-32+4-22-4 izlaz je 2.

# string = input("Unesite string: ")

# brojac = 0

# i = 0
# while i < len(string):
#     if string[i] == '-':
#         if i+1 < len(string) and string[i+1].isdigit():
#             if i+2 >= len(string) or not string[i+2].isdigit():
#                 brojac += 1
#             else:
#                 while i+1 < len(string) and string[i+1].isdigit():
#                     i += 1
#     i += 1


# print(brojac)

# 57. Narcissistic Number je broj čija suma cifara (tog broja) stepenova sa njegovim brojem
# cifara daje isti taj broj.
# Primjer 1: 153 (3 cifre)
# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# Primjer 2: 1634 (4 cifre):
# 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
# Vaš program treba da štampa “Da” ili “Ne” u zavisnosti od toga da li je broj Narcissistic ili
# nije. Input je uvijek validan broj.

# broj = input("Unesite broj: ")
# stepen = len(broj)
# broj = int(broj)
# broj1 = broj
# sum=0
# while broj != 0:
#   cifra = broj % 10
#   sum += cifra**stepen
#   broj //= 10

# if sum == broj1:
#   print("DA")
# else:
#   print("NE")

# 58. Napisati program koji od zadatog stringa kreira novi string koji se sastoji bez cifara.
# Primjer: “Hi Mr. Rober53. How are you today? Today is 08.10.2019”), vraća “Hi Mr.
# Rober. How are you today? Today is ..” kao string.
# Pomoć: da provjerite da li je karakter slovo koristiti isalpha metod, a da li je cifre koristite
# isdigit.

# string = input("Unesite string: ")
# duzina = len(string)
# niz = []
# i=0

# while i < duzina:
#   if string[i] not in "0123456789":
#     niz.append(string[i])
#   i+=1

# print(niz)
# string1 = ''.join(niz)
# print(string1)


# 59. Napisati program koji za unijeti string s (karakteri stringa cifre od 0 do 9) enkriptuje na
# sledeći način: ako je karakter paran broj pretvara se u 0, a ako je karakter neparan broj
# pretvara se u 1. Npr. za s = ‘15023’ rezultat je 11001. Pomoć: Inicijalna vrijednost za
# dodatni string je “”, a onda se pomoću operatora + nadodaje 0 ili 1 u zavisnosti u
# ispunjenosti uslova

# string = input("Unesite string: ")
# resenje = ""
# for item in string:
#   if item in "02468":
#     resenje += "0"
#   else:
#     resenje += "1"

# print(resenje)


# 60. Napisati program koji na osnovu dvije varijable start i end koji predstavljaju početak i kraj
# segmenta [start, end] (uključujući start i end) kvadrira sve elemente iz tog segmenta koji
# su djeljivi sa 3 ali ne sa 6, a onda ih sumira. Štampati sumu.

# start = int(input("Unesite pocetak segmenta: "))
# end = int(input("Unesite kraj segmenta: "))
# sum = 0
# for i in range(start+1,end):
#   if i % 3 == 0 and i % 6 != 0:
#     sum += i**2
#   print(i)

# print(sum)

# 61. Napisati program koji vraća velika slova iz zadatog unijetog teksta kao jedan novi string.
# Ulaz: “Prva recenica. Ovo je druga recenica. Na kraju treca.”
# Izlaz: PON

# string = input("Unesite string")
# karjni_string = ""

# for item in string:
#   if item.isupper():
#     karjni_string += item

# print(karjni_string)

#62. Napisati program koji za unijeti string a prebrojava koliko ima heksadecimalnih brojeva.
# Broj je heksadecimalni ako ima prefiks 0x. Svaki broj je razdvojena razmakom (space)
# Ulaz 1: a = “12 0x1A 0001 121 0x2”; Izlaz 1: 2
# Ulaz 2: a = “12 001 31”; Izlaz 2: 0

# string = input("Unesite string: ")
# brojac = 0
# i=0
# duzina = len(string)

# while i != duzina:
#   if string[i] == "0" and string[i+1] == "x":
#     brojac += 1
#   i += 1

# print(brojac)

# 63. Za dati string koji sadrži praznine (blankove), odrediti najdužu riječ u stringu

# string = input("Unesite string: ")

# najduzi_string = ""
# trenutni_string = ""

# for item in string:
#     if item != " ":
#         trenutni_string += item
#     else:
#         if len(trenutni_string) > len(najduzi_string):
#             najduzi_string = trenutni_string
#         trenutni_string = ""

# # Provjeravamo dužinu posljednje riječi u stringu
# if len(trenutni_string) > len(najduzi_string):
#     najduzi_string = trenutni_string

# print(najduzi_string)

# 64. Napisati program koji računa zbir najmanje i najveće cifre unesenog broja

# broj = int(input("Unesite broj: "))
# min = broj%10
# max = broj%10
# broj //= 10

# while broj != 0:
#   cifra = broj % 10
#   if cifra < min:
#     min = cifra
#   elif cifra > max:
#     max = cifra
#   broj //= 10

# print(min , max)

# 65. Na terasi dužine d metara treba rasporediti n stubića širine s centimetara tako da
# rastojanje između stubića, kao i između stubića i zida bude isto.
# Ulaz: Tri reda standardnog ulaza sadrže tri broja:
# • d - realan broj koji predstavlja dužinu terase u m
# • n - broj stubića
# • s - realan broj koji predstavlja širinu stubića u cm
# Izlaz: Rastojanje između stubića u centimetrima, zaokruženo na dve decimale.
# Napomena: Neka je r nepoznato rastojanje između stubića. Tada n stubića pokriva n ·
# s cm. Između n stubića postoji n − 1 razmak, jedan razmak je između lijevog zida i prvog
# stubića i jedan razmak je između poslednjeg stubića i desnog zida. Dužina terase u
# centimetrima je d · 100 cm.
# Dakle, važi uslov n · s cm + (n + 1) · r cm = d · 100 cm
# Samo ostaje da r izracunamo i to je to.

# d = float(input("Unesite duzinu terase: "))
# n = int(input("Unesite broj stubica: "))
# s = float(input("Unesite sirinu stubica: "))

# d *= 100

# r = (d - (n*s)) / n - 1

# print(round(r,2))

# 66. Data je lista koja se sastoji od cijelih brojeva. Provjeriti da li u listi ima više dvocifrenih ili
# trocifrenih brojeva.

# lista = [100,200,10,23,2000,123,422]
# broj_dvocifrenih = 0
# broj_trocifrenih = 0

# for item in lista:
#   if item>9 and item<100:
#     broj_dvocifrenih += 1
#   elif item>99 and item<1000:
#     broj_trocifrenih += 1

# print(broj_dvocifrenih,broj_trocifrenih)

# 67. Napisati program koji provjerava koliko se određeni broj ponavlja u listi (taj broj unosi
# korisnik).

# niz = [1,2,4,5,6,6,31,6,3,4,]

# broj = int(input("Unesite broj: "))
# brojac = 0
# for item in niz:
#   if item == broj:
#     brojac+=1

# print(brojac)

# 68. Napisati program koji uvećava zarade koje su veće od prosječne zarade (prosjek liste)
# za X eura.

# plate = [200,330,330,400,500,100,300]
# x = int(input("Unesite x: "))

# prosjek = sum(plate) / len(plate)
# i=0
# while i != len(plate):
#   if plate[i] > prosjek:
#     plate[i] += x

#   i+=1

# print(plate)

# 69. Napisati program koji umanjujete zarade koje su veće od prosječne za 10 %, a zarade
# manje od prosječne uvećava za 10 %. Prikazati koliko zarada će biti iznad prosjeka
# nakon uvećanja/umanjenja.

# plate = [200,330,330,400,500,100,300]

# prosjek = sum(plate) / len(plate)
# i=0
# while i != len(plate):
#   if plate[i] > prosjek:
#     plate[i] -= plate[i] * 0.1
#   elif plate[i] < prosjek:
#     plate[i] += plate[i] * 0.1
#   i+=1

# print(plate)

# 70. Napisati program koji vraća zbir kvadrata elemenata liste koji su djeljivi sa 3.
# lista = [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20]

# sum = 0

# for item in lista:
#   if item % 3 == 0:
#     sum += item**2

# print(sum)

from math import sqrt
# 71. Kreirati program koji analizira zadatu listu brojeva i određuje koliko među njima postoji
# onih brojeva koji nakon primjene kvadratnog korijena zadržavaju svojstvo da budu cijeli
# brojevi. Program treba da prikaže ukupan broj takvih brojeva u listi.

# lista = [1,2,3,4,5,6,7,8,9,11]
# brojac=0
# for item in lista:
#   broj = sqrt(item)
#   if broj.is_integer():
#     # moglo je i sa isinstance(broj,int)
#     brojac += 1
#     print(broj)

# print(brojac)

# 72. Lista se sastoji od ocjena studenata na predmetu Ekonomija i razvoj. Koliko studenata je
# dobilo veću ocjenu od prosječne ocjene (ocjena 5 ne utiče na prosjek).
# ocjene = [10,5,6,7,5,6,8,7,8,8,9,10,10]
# brojac = 0
# sum = 0
# for item in ocjene:
#   if item > 5:
#     brojac += 1
#     sum += item
# prosjek = sum / brojac

# veci_od_prosjek = 0

# for item in ocjene:
#   if item > prosjek:
#     veci_od_prosjek += 1

# print(veci_od_prosjek)

# 73. Za RPG igru, napravi program koji simulira inventar igrača. Inventar može biti lista tkz.
# itema, odnosno predmeta (npr. mač, šešir, rukavice,...). Vaš zadatak je da na osnovu
# pozicije u inventaru otkrijete koji je to predmet (za pristup koristiti indeks liste)

# invertot = ["casa","sesir","rukavice","mac","sablja"]
# pozicija = int(input("Unesite poziciju u inventaru:"))
# if pozicija < len(invertot):
#   print(invertot[pozicija])
# else:
#   print("Nema predmeta na ovoj poziciji")


# 74. Napisati program koji za zadatu listu plata zaposlenih u jednoj IT kompaniji (plate se
# unose u eurima) računa prosječnu vrijednost plata u dolarima ako je poznato da je 1e =
# 1.1$.

# plate = [200,330,330,400,500,100,300]

# prosjek = sum(plate) / len(plate)

# prosjek_dolara = prosjek * 1.1

# print(round(prosjek,2) ,round(prosjek_dolara,2))

# 75. Napisati program koji izračunava ukupni gubitak banke za godinu dana od kamate na
# štednju. Korisnik unosi listu početnih iznosa štednje klijenata. Takođe, korisnik unosi
# fiksnu kamatnu stopu na štednju (za sve korisnike ista). Program izračunava i ispisuje
# ukupni gubitak banke od kamate nakon datog perioda.
# stednja_klijenata = [100,200,300,400,500,600,700,800,900]

# kamatna_stopa = float(input("Unesite fiksnu kamatnu stopu na štednju (u postocima): "))
# kamatna_stopa /= 100

# ukupni_gubitak = sum(iznos * kamatna_stopa for iznos in stednja_klijenata)

# print(ukupni_gubitak)

# 76. Napraviti program koji mijenja svako pojavljivanje određenog elementa u listi sa drugim
# elementom. Na primjer, zamjena svih 2 sa -2. Npr. lista [1, 2, 3, 2, 4, 2] u [1, -2, 3, -2, 4,
# -2]
# lista = [1,2,3,2,4,2]
# promjenjen_el = int(input("Unesite element koji zelite promjeniti: "))
# novi_el = int(input("Unesite novi element: "))
# i=0

# while i != len(lista):
#   if lista[i] == promjenjen_el:
#     lista[i] = novi_el
#   i+=1  
# print(lista)

# 77. Kreirati program koji provjerava da li je lista brojeva sortirana u rastućem poretku.
# Program treba da vrati True ako je lista sortirana, inače False.

# lista = [1,2,3,2,4,2]
# i=0
# sortiran = True
# while i != len(lista):
#   if lista[i] > lista[i+1]:
#     sortiran = False
#     break
#   i+=1

# print(sortiran)

# 78. Neka je data lista artikala u jednoj prodavnici. Pronaći vrijednost drugog najskupljeg
# proizvoda u prodavnici.

# lista = [1,2,3,2,4,2]

# lista.sort()
# print(lista[-2])

# 79. Napisati program koji za unijetu listu elemenata (cijeli brojevi, bez nule) vraća broj
# elemenata koji imaju suprotnu vrijednost. Broju x, suprotan broj je -x. Smatrati da se broj
# pojavljuje jednom i da nekad ima svoju suprotnu vrijednost, a nekad nema (ne može
# imati više od jedne suprotne vrijednosti, niti se ponavljati)

# lista = [1, 2, 3, -1, -2, -3, 4, 5, 6]
# broj_suprotnih = 0
# vidjeni_brojevi = {}

# for broj in lista:
#     if broj != 0:  
#         if -broj in vidjeni_brojevi and vidjeni_brojevi[-broj] > 0:
#             broj_suprotnih += 1
#             vidjeni_brojevi[-broj] -= 1
#         else:
#             vidjeni_brojevi[broj] = vidjeni_brojevi.get(broj, 0) + 1

# print(broj_suprotnih)

# 80. U igri gdje lik skače po platformama, dužina svakog skoka sačuvana je kao broj u listi.
# Napravi program koja nalazi razliku između najdužeg i najkraćeg skoka.

# lista = [1,2,4,5,2,5,1,1]

# min = min(lista)
# max = max(lista)
# razlika = max - min
# print(razlika)
