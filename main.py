# 1. U tajanstvenom svijetu postoji portal koji se otvara samo kada mu se date paran broj.
# Kao mladi čarobnjak na svom prvom zadatku, dobio si čarobni štapić koji može
# generisati brojeve. Vaš zadatak je da kreirate algoritam koji će provjeriti da li je broj koji
# je čarobni štapić generisao paran. Ako jeste, algoritam treba da ispiše: "Portal se
# otvara!" Ako nije, algoritam treba da ispiše: "Portal ostaje zatvoren."

#import random
# broj se moze uzeti kaom input
#broj = int(input("Unesite broj: "))
# broj = random.randint(1,100)
# if broj % 2 == 0:
#   print(broj)
#   print("Portal se otvara!")
# else:
#   print(broj)
#   print("Portal ostaje zatvoren.")


# 2. U selu poznatom po svojim jabukama, održava se godišnje takmičenje u berbi jabuka
# između i najbliži pobjedi su Petar i Miloš. Petar tvrdi da je ubrao p jabuka, dok Miloš tvrdi
# da je ubrao m jabuka. Vaš zadatak je da kreirate algoritam koji će provjeriti da li je Petar
# uspio da ubere više jabuka nego Miloš i shodno tome ispiše poruku o pobjedniku.
# Pretpostaviti da ne mogu ubrati isti broj jabuka.

# p = int(input("Unesite broj jabuka koje je ubrao Petar"))
# m = int(input("Unesite broj jabuka koje je ubrao Miloš"))

# if p > m:
#   print("Petar je pobjedik")
# else:
#   print("Milos je pobjednik")



# 3. Zamislimo da pravimo program koji treba da odluči da li student može da pristupi ispitu.
# Postoje dva uslova: student mora imati više od 75% prisustva na predavanjima i mora
# imati predate sve seminarske radove. Oba uslova moraju biti zadovoljena da bi student
# mogao pristupiti ispitu. Algoritam treba da štampa odgovarajuću poruku. Dodatak:
# prisustvo se unosi u procentima, a dio za seminarske radove na sledeci nacin -> 0
# predstavlja da bar jedan seminarski rad nike uradjen, a 1 da su svi seminarski radovi
# uradjeni.

# prisustvo = int(input("Unesite broj procenata prisustva: "))
# broj_seminarskih = int(input("Unesite broj seminarskih radova: "))

# if prisustvo >= 75 and broj_seminarskih == 1:
#   print("student ima pravo prisustva")
# else:
#   print("student nema pravo prisustva"")


# 4. Kućni red zabranjuje pravljenje buke prije 6 časova, između 13 i 17 časova i nakon 22
# časa. Napiši program koji radnicima govori da li u nekom datom trenutku mogu da
# izvode bučnije radove.

# vrijeme = int(input("Unesite vrijeme: "))
# if (vrijeme > 6 and vrijeme < 13) or (vrijeme > 17 and vrijeme < 22):
#   print("Mozete da izvodite bucnije radove")
# else:
#   print("Ne mozete da izvodite bucnije radove")

# 7. Takmičari su radili testove iz matematike i programiranja. Za svaki predmet dobili su
# određeni broj poena (cio broj od 0 do 50). Takmičari se rangiraju po ukupnom broju
# poena iz oba predmeta. Ako dva takmičara imaju isti broj poena, pobjednik je onaj koji
# ima više poena iz programiranja. Potrebno je napisati program koji određuje pobjednika
# takmičenja.

# takmicari = ["Vasilije","Andrija","Mirko"]
# bodovi_programiranje = [30,29,12]
# bodovi_matematika = [50,23,15]

# najveci = bodovi_programiranje[0] + bodovi_matematika[0]
# pozicija = 0

# for i in range(1,len(bodovi_programiranje)):
#   if bodovi_programiranje[i] + bodovi_matematika[i] > najveci:
#     najveci = bodovi_programiranje[i] + bodovi_matematika[i]
#     pozicija = i

# print(f"Takmicar {takmicari[pozicija]} je pobjednik sa {najveci} poena")

# 8. Napisati program kojim se na osnovu datog prosjeka učenika prikazuje uspjeh učenika.
# Odličan uspjeh ima učenik čiji je prosjek veći ili jednak 4.5. Vrlodobar uspeh postiže
# učenik čiji je prosek veći ili jednak 3.5, a manji od 4.5, dobar uspeh se postiže za prosek
# koji je veći ili jednak 2.5 a manji od 3.5, dovoljan uspeh za prosek veći ili jednak 2, a
# manji od 2.5. Ako učenik ima neku jedinicu unijeće se prosjek 1, a uspeh mu je
# nedovoljan.

# prosjek = float(input("Unesite prosjek: "))

# if prosjek >= 4.5:
#   print("Odlican")
# elif prosjek >= 3.5:
#   print("Vrlodobar")
# elif prosjek >= 2.5:
#   print("Dobar")
# elif prosjek >= 2:
#   print("Dovoljan")
# elif prosjek == 1:
#   print("Nedovoljan")
# else:
#   print("Projeske nije u rasponu od 1 do 5")


# 9. Kupili ste zavjesu pravouganog oblika. Provjerite da li će zavjesa prekriti prozor koji je
# takođe pravouganog oblika. Za zavjesu i prozor poznata je gornja lijeva i donja desna
# koordinata.

# #koordinate prozora
# gornja_lijeva_x_prozora = 4
# gornja_lijeva_y_prozora = 2
# donja_desna_x_prozora = 1
# donja_desna_y_prozora = 3

# #koordinate zavjese
# gornja_lijeva_x_zavjesa = 5
# gornja_lijeva_y_zavjesa = 1
# donja_desna_x_zavjesa = 6
# donja_desna_y_zavjesa = 4

# if (gornja_lijeva_x_prozora < gornja_lijeva_x_zavjesa) and (donja_desna_x_prozora < donja_desna_x_zavjesa) and (gornja_lijeva_y_prozora < gornja_lijeva_y_zavjesa) and (donja_desna_y_prozora < donja_desna_y_zavjesa):
#   print("Zavjesa prekriva prozor")
# else:
#   print("Zavjesa ne prekriva prozor")

# 11. Vaš zadatak je da napišete program kojim ćete provjeriti da li se mrav kreće po ivici
# stola. Geometrijski, mrav se predstavlja kao tačka, a za sto su poznate tjemena desne
# gornje i lijeve donje ivice stola. Radi jednostavnosti smatrati da je sto pravouganik, ne
# kvadar.


# x_mrava = int(input("Unesite x koordinatu mrava:"))
# y_mrava = int(input("Unesite y koordinatu mrava:"))

# x_lijeva_donja_ivica = 4
# y_lijeva_donja_ivica = 2
# x_desna_gornja_ivica = 4
# y_desna_gornja_ivica = 0

# if (x_mrava >= x_lijeva_donja_ivica) and (x_mrava <= x_desna_gornja_ivica) and (y_mrava == y_lijeva_donja_ivica or y_mrava == y_desna_gornja_ivica):
# #mrav seta po gornjoj ili donjoj ivici stola
#   print("na ivici je")
# elif (y_mrava >= y_lijeva_donja_ivica) and (y_mrava <= y_desna_gornja_ivica) and (x_mrava == x_lijeva_donja_ivica or x_mrava == x):
# #mrav seta po levoj ili desnoj ivici stola
#   print("na ivici je")
# else:
#   print("nije na ivici")



# 10. Vaš zadatak je da napišete program kojim provjerate da li je strelica pogodila pikado
# tablu. Za pikado tablu je poznat je njegov poluprečnik i koordinate centra, a za strelice
# koordinate cilja.
#Ovaj zadatak cemo uradit pomocu matematike forumule za udaljenos dvije tacke u ravni

#importovacemo math radi lakseg zapisivanja formule
# import math

# def provjeri_pogodak(pikado_centar_x, pikado_centar_y, pikado_poluprecnik, strelica_x, strelica_y):
#     # d = sqrt((x2 - x1)^2 + (y2 - y1)^2) nije bitan redosled uzimanja koordina
#     udaljenost = math.sqrt((strelica_x - pikado_centar_x)**2 + (strelica_y - pikado_centar_y)**2)
#     if udaljenost <= pikado_poluprecnik:
#         return True
#     else:
#         return False

# # Unesite koordinate centra pikado table i poluprečnik
# pikado_centar_x = int(input("Unesite x koordinatu centra pikado table: "))
# pikado_centar_y = int(input("Unesite y koordinatu centra pikado table: "))
# pikado_poluprecnik = int(input("Unesite poluprečnik pikado table: "))

# # Unesite koordinate strelice
# strelica_x = int(input("Unesite x koordinatu strelice: "))
# strelica_y = int(input("Unesite y koordinatu strelice: "))

# # Provjeri da li je strelica pogodila pikado tablu
# if provjeri_pogodak(pikado_centar_x, pikado_centar_y, pikado_poluprecnik, strelica_x, strelica_y):
#     print("Strelica je pogodila pikado tablu!")
# else:
#     print("Strelica nije pogodila pikado tablu.")


# 12. Napisati program koji obrađuje dvocifreni broj na sledeći način:
# a. Ako je prva cifra veća od druge štampati razliku prve i druge cifre
# b. Ako je prva cifra manja od druge štampati zbir te dvije cifre
# c. Ako su cifre iste štampati njihov proizvod

# x = 33
# cifra_2 = x % 10
# cifra_1 = (x // 10) % 10

# #print(cifra_1 , cifra_2)
# if cifra_1 > cifra_2:
#   print(cifra_1 - cifra_2)
# elif cifra_1 < cifra_2:
#   print(cifra_1 + cifra_2)
# else:
#   print(cifra_1 * cifra_2)



# 13. Za dva stola kružnog oblika poznat je njihov poluprečnik. Napisati kod kojim se štampa
# obim stola sa većom površinom.

# import math
# r1=9
# r2 = 5
# povrsina1 = (r1)**2 * math.pi
# povrsina2 = (r2)**2 * math.pi

# if povrsina1 > povrsina2:
#   print(2*r1*math.pi)
# else:
#   print(2*r2*math.pi)

# 14. Date su cijene tri proizvoda. Naći par proizvoda čija cijena u zbiru daje najmanju
# vrijednost.


# cijena1 = 200
# cijena2 = 100
# cijena3 = 89

# niz = [cijena1, cijena2, cijena3]

# niz.sort()
# print(niz[0]+niz[1])

# 15. Napisati kod koji za datu godinu određuje da li je prestupna i štampa odgovarajuću
# poruku.
# godina = int(input("Unesite godinu: "))

# if (godina % 4 == 0 and godina % 100 != 0) or (godina % 400 == 0):
#   print("Godina je prestupna")
# else:
#   print("Godina nije prestupna")  



# 16. Napisati program kojim se provjerava da li se tačka nalazi unutar pravouganika. Za
# pravougaonik su date koordinate gornjeg lijevog i donjeg desnog tjemena.
# x = int(input("Unesite x koordinatu: "))
# y = int(input("Unesite y koordinatu: "))

# #kortinate uglova pravugaonika

# x_gornja_lijeva = 2
# y_gornja_lijeva = 3

# x_donja_desna = 0
# y_donja_desna = 0

# if (x_gornja_lijeva <= x and x <= x_donja_desna) and (y_gornja_lijeva <= y and y <= y_donja_desna):
#   print("Unutra je")
# else:
#   print("Izvan je")



# 17. Napisati program koji provjerava da li se od pravouganika poznatih dimenzija stranica
# mogu napraviti bar dva kvadrata čija je duzina ista kao i dužina pravouganika.

# a = int(input("Unesite duzinu stranice a: "))
# b = int(input("Unesite duzinu stranice b: "))
# manja_stranica = min(a,b)
# povrsina = a*b
# povrsina_kvadrata = manja_stranica**2

# if povrsina_kvadrata * 2 <= povrsina:
#   print("Moze")
# else:
#   print("Ne moze")



# 18. Napisati program kojim se na osnovu temperature vode određuje njeno agregatno
# stanje. Ako je temperatura:
# • viša od 0 C i niža od 100C - agregatno stanje je tečno
# • ne viša od 0 C - agregatno stanje je čvrsto,
# • ne niža od 100 C - agregatno stanje je gasovito.
# Za temperaturu od tačno 0 smatra se da je agregatno stanje čvrsto, a za tačno 100 da je
# gasovito.
# Ulaz: Temperatura - cio broj
# Izlaz: Na standardni izlaz ispisati jednu od sledećih riječi: cvrsto, tecno, gasovito.

# temp = float(input("Unesite temperaturu: "))

# if temp > 0 and temp < 100:
#   print("Tečno")
# elif temp <= 0:
#   print("Crvtsto")
# elif temp >= 100:
#   print("Gasovito")


# 19. U jednoj privatnoj školi uvedeno je pravilo kojim se određuje iznos popusta koji ostvaruju
# učenici prilikom upisa u narednu školsku godinu. Učenici sa odličnim uspehom ostvaruju
# popust od 40% ukupnog iznosa školarine, sa vrlodobrim 20% a sa dobrim 10%. Takođe,
# učenici koji su osvojili nagradu na nekom od državnih takmičenja ostvaruju popust od
# 30% ukupnog iznosa školarine. Ukoliko neki učenik ispunjava dva kriterijuma za popust
# primenjuje se kriterijum po kome je popust veći. Na osnovu punog iznosa školarine,
# prosečne ocene učenika i informacije o nagradama sa takmičenja odrediti iznos koji
# učenik treba da plati pri upisu u narednu školsku godinu.
# Ulaz: U prvoj varijabli nalazi se pun iznos školarine (realan broj), u drugoj prosječna
# ocjena učenika (realan broj od 2.0 do 5.0) a u trećoj 0 ukoliko učenik nema nagradu ili 1
# ukoliko je ima.
# Izlaz: Iznos školarine koju učenik treba da plati (zaokružen na najbliži cio broj) navodi se
# u jednoj linije standardnog izlaza.


# skolarina = int(input("Unesite iznos skolarine: "))
# uspjeh = float(input("Unesite iznos prosjek: "))
# nagrade = int(input("1 ako ima nagradu, 0 ako nema nagradu: "))

# popusta_nagrade = 0.3

# if uspjeh >= 4.5:
#   popust = 0.4
# elif uspjeh >= 3.5:
#   popust = 0.2
# elif uspjeh >= 2.5:
#   popust = 0.1
# else:
#   popust = 0

# if nagrade == 1:
#   ukupna_skolarina = skolarina - (skolarina *  max(popust, popusta_nagrade))
# else:
#   ukupna_skolarina = skolarina - (skolarina *  popust)

# print(round(ukupna_skolarina))


# 20. Napisati program koji računa zbir parnih cifara ukoliko je broj paran, a ukoliko je neparan
# proizvod neparnih cifara četvorocifrenog broja. Broj n unosi korisnik.

# n = int(input("Unesite broj: "))

# def zbir_parnih_cifara(n,parnost):
#   zbir = 0
#   while n != parnost:
#     cifra  = n % 10
#     if(cifra % 2 == 0):
#       zbir += cifra
#     n //= 10
#   print(zbir)

# if n % 2 == 0:
#   zbir_parnih_cifara(n,0)
# else:
#   zbiro_neparnih_cifara(n,1)
