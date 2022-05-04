# def dziwne_dzialanie(liczba1, liczba2):
#     suma=liczba1+liczba2
#     kwadrat=suma**2
#     wynik=kwadrat-1
#     return wynik,kwadrat
#
# for i in range(3):
#     pierwsza=float(input("Podaj pierwszą liczbę: "))
#     druga=float(input("Podaj drugą liczbę: "))
#     wynik, kwadrat=dziwne_dzialanie(pierwsza,druga)
#     print("Wynikiem skomplikowanego działania jest: ", wynik)
#     print("Kwadratem podanych liczb jest: ", kwadrat)

# def rysujProstokat(dlugosc, szerokosc, element=4):
#     for i in range(dlugosc):
#         for j in range(szerokosc):
#             print(element, end='')
#         print()
#
#
# rysujProstokat(4,8)
# rysujProstokat(5,9,'*')

# #NOTE: rekurencja - funkcja gwiazdki uruchamia samą siebie
#
# def gwiazdki(liczbaGwiazdek):
#     if liczbaGwiazdek>0:
#         print("*")
#         gwiazdki(liczbaGwiazdek-1)
#
# gwiazdki(5)

# def mnozenie(listaLiczb):
#     if len(listaLiczb)>0:
#         return listaLiczb[0]*mnozenie(listaLiczb[1:])
#     else:
#         return 1
#
# lista=[1,2,3,4,5]
# wynik=mnozenie(lista)
# print(wynik)


# #NOTE: zad 1
# def ostatni(lista):
#     if len(lista)>1:
#         return ostatni(lista[1:])
#     else:
#         return lista[0]
#
# lista=["a","b","c","d","e","f"]
# wynik=ostatni(lista)
# print(wynik)

# #NOTE: zad 4
# def dlugosc(lista):
#     if not lista==[]:
#         return 1 + dlugosc(lista[1:])
#     else:
#         return 0
#
# lista=["a","b","c","d","e","f"]
# wynik=dlugosc(lista)
# print(wynik)
#
# #NOTE: zad 3
# def maksimum(lista, zapamietana):
#     if len(lista)>1:
#         if lista[0]>zapamietana:
#             zapamietana=lista[0]
#         return maksimum(lista[1:], zapamietana)
#     else:
#         return zapamietana
#
# lista=[1,2,3,4,5,6,7,5,4,3,2,1]
# print(maksimum(lista, lista[0]))
#
# def minimum(lista, zapamietana):
#     if len(lista)>1:
#         if lista[0]<zapamietana:
#             zapamietana=lista[0]
#         return minimum(lista[1:], zapamietana)
#     else:
#         return zapamietana
#
# lista=[1,2,3,4,5,6,7,5,4,3,2,1]
# print(minimum(lista, lista[0]))

# #NOTE: zad 6
# def czy_jest(lista, element):
#     if len(lista)>0:
#         if lista[0]==element:
#             print("Element znajduje się na liście.")
#         else:
#             lista=lista[1:]
#             czy_jest(lista,element)
#     else:
#         print("Elementu nie ma na liście.")
#
# lista=["Ala","ma","kota","a","Basia","ma","psa"]
# print("Jaki element chcesz sprawdzić?")
# element=input()
# wynik=czy_jest(lista,element)

# #NOTE: zad 2
# def ogon(lista,lista2=[]):
#     if len(lista)>1:
#         lista2.append(lista[1])
#         lista=lista[1:]
#         ogon(lista)
#     else:
#         print(lista2)
#
# lista=["ok",2,3,4,5,6,7,8,9]
# ogon(lista)

# #NOTE: zad 5
# ##Napisz funkcje nta(x), która zwraca n-ty element listy (rekurencyjnie)
# def nta(lista,n):
#    if len(lista)>n:
#        if n==0:
#            return lista[0]
#        return nta(lista[1:],n-1)
#
#    else:
#        return "Lista nie ma tylu elementów"
# print("Który element listy wyświetlić?")
# n=int(input())
# print(nta(lista,n))
# #
# #NOTE: zad 7
# def nta(liczba, potega):
#     if int(potega)==0:
#         return 1
#     elif int(potega)>=1:
#         wynik=int(liczba)*nta(int(liczba),int(potega)-1)
#         return wynik
#
# liczba=input("Podaj liczbę: ")
# potega=input("Podaj potęgę: ")
# wynik=nta(liczba,potega)
# print(wynik)

# #NOTE: zad 8
# def silnia(liczba):
#     if liczba==1:
#         return 1
#     elif liczba==0:
#         return 0
#     else:
#         return liczba*silnia(liczba-1)
#
# liczba=int(input("Podaj liczbę: "))
# print(silnia(liczba))

# #NOTE: zad 9
# def suma(liczba1,liczba2):
#     sumowanie=int(liczba1)+int(liczba2)
#     print(sumowanie)
#
# print("Podaj pierwszą liczbę.")
# pierwsza=input()
# print("Podaj drugą liczbę.")
# druga=input()
# suma(pierwsza,druga)

# # #NOTE: zad 10
# def suma(liczba1,liczba2):
#     sumowanie=int(liczba1)+int(liczba2)
#     return sumowanie
#
# print("Podaj pierwszą liczbę.")
# pierwsza=input()
# print("Podaj drugą liczbę.")
# druga=input()
# wynik=suma(pierwsza,druga)
# print(wynik)

# #NOTE: zad 11 kalkulatorek
# def suma(liczba1,liczba2):
#     sumowanie=int(liczba1)+int(liczba2)
#     return sumowanie
#
# def odejmowanie(liczba1,liczba2):
#     roznica=int(liczba1)-int(liczba2)
#     return roznica
#
# def mnozenie(liczba1,liczba2):
#     iloczyn=int(liczba1)*int(liczba2)
#     return iloczyn
#
# def dzielenie(liczba1,liczba2):
#     iloraz=int(liczba1)/int(liczba2)
#     return iloraz
#
# def potegowanie(liczba1,liczba2):
#     potega=int(liczba1)**int(liczba2)
#     return potega
#
# print("Podaj liczbę pierwszą.")
# pierwsza=input()
# print("Podaj liczbę drugą.")
# druga=input()
# print("Jakie działanie chcesz wykonać na tych liczbach?")
# dzialanie=input()
# if dzialanie=="dodawanie":
#     print(suma(pierwsza,druga))
# elif dzialanie=="odejmowanie":
#     print(odejmowanie(pierwsza,druga))
# elif dzialanie=="mnożenie":
#     print(mnozenie(pierwsza,druga))
# elif dzialanie=="dzielenie":
#     print(dzielenie(pierwsza,druga))
# elif dzialanie=="potęgowanie":
#     print(potegowanie(pierwsza,druga))
# else:
#     print("Nie znam takiego działania.")

# #NOTE: zad 12
# def czy_rowne():
#     print("Podaj pierwszą liczbę.")
#     liczba1=int(input())
#     print("Podaj drugą liczbę.")
#     liczba2=int(input())
#     if int(liczba1)==int(liczba2):
#         print("Te liczby są równe.")
#     else:
#         roznica=abs(liczba1-liczba2)
#         print("Te liczby nie są równe. Różnica między nimi wynosi",roznica)
#
# czy_rowne()

# #NOTE: zad 13
# def laczenie_list(lista1,lista2):
#     for i in range(len(lista2)):
#         lista1.append(lista2[i])
#     print(lista1)
#
# lista1=[1,23,4,5,6,78,8,6,4]
# lista2=[234,67,6,54,56,8,88]
# laczenie_list(lista1,lista2)

# #NOTE: zad 14
# def laczenie_list(lista1,lista2):
#     for i in range(len(lista2)):
#         if lista2[i] not in lista1:
#             lista1.append(lista2[i])
#     print(lista1)
#
# lista1=[1,23,4,5,6,78,8,6,4,88,67]
# lista2=[234,67,6,54,56,8,88,6,4]
# laczenie_list(lista1,lista2)

# def fbn(liczba_elementow):
#     if liczba_elementow==0:
#         return 0
#     elif liczba_elementow==1:
#         return 1
#     else:
#         return fbn(liczba_elementow-1)+fbn(liczba_elementow-2)
#
# liczba_elementow=int(input())
# print(fbn(liczba_elementow))

# def odwrocone(lancuch):
#     if lancuch=="":
#         return ""
#     else:
#         return odwrocone(lancuch[1:])+lancuch[0]
#
# lancuch=input()
# print(odwrocone(lancuch))
#
# def czy_palindrom(lancuch):
#     if lancuch=="":
#         return "Tak"
#     else:
#         if lancuch[0]==lancuch[-1]:
#             return czy_palindrom(lancuch[1:-1])
#         else:
#             return "Nie"
#
# slowo=input("Podaj słowo: ")
# print("Czy jest to palindrom?:", czy_palindrom(slowo))


# def suma(liczba):
#     if liczba==0:
#         return liczba
#     else:
#         return liczba+suma(liczba-1)
#
# liczba=int(input("Podaj liczbę: "))
# print(suma(liczba))

#
# def ostatni(lista):
#     if len(lista)==1:
#         return lista[0]
#     else:
#         return ostatni(lista[1:])
#
lista=[34,5,7,5,13444,33,56,3]
# print(ostatni(lista))

# def ogon(lista,lista2=[]):
#     if len(lista)>1:
#         lista2.append(lista[1])
#         ogon(lista[1:])
#     else:
#         print(lista2)
#
# ogon(lista)

# def maksimum(lista, zapamietana=lista[0]):
#     if len(lista)>1:
#         if lista[0]>zapamietana:
#             zapamietana=lista[0]
#         return maksimum(lista[1:], zapamietana)
#     else:
#         return zapamietana
#
# # lista=[1,2,3,4,5,6,7,5,4,3,2,1]
# print(maksimum(lista))
#
# def minimum(lista,zapamietana=lista[0]):
#     if len(lista)>1:
#         if lista[0]<zapamietana:
#             zapamietana=lista[0]
#         return minimum(lista[1:],zapamietana)
#     else:
#         return zapamietana
#
# print(minimum(lista))

# def dlugosc(lista):
#     if not lista==[]:
#         return dlugosc(lista[1:])+1
#     else:
#         return 0
#
# print(dlugosc(lista))

# def nta(lista,liczba):
#     if len(lista)<liczba:
#         return "Nie ma takiego elementu."
#     if liczba==1:
#         return lista[0]
#     else:
#         return nta(lista[1:],liczba-1)
#
# print(nta(lista,1))

# def czy_jest(lista,element):
#     if len(lista)>0:
#         if lista[0]==element:
#             return "TAK"
#         else:
#             return czy_jest(lista[1:],element)
#     else:
#         return "NIE"
#
# print(czy_jest(lista, 35))

# def ntapotega(liczba,potega):
#     if potega==0:
#         return 1
#     else:
#         return ntapotega(liczba,potega-1)*liczba
#
# print(ntapotega(1223,3))

# def silnia(liczba):
#     if liczba==1:
#         return 1
#     elif liczba==0:
#         return 0
#     else:
#         return liczba*silnia(liczba-1)
#
# print(silnia(4))

# def fib(element):
#     if element==1:
#         return 0
#     elif element==2:
#         return 1
#     else:
#         return fib(element-1)+fib(element-2)
#
#
# print(fib(1))


def sumowanie_elementow(lista1,lista2,lista3):
    if len(lista1)==0:
        return lista3
    if len(lista1)>=1:
        lista3.append(lista1[0]+lista2[0])
        return sumowanie_elementow(lista1[1:],lista2[1:],lista3)

lista1=[1,2,3]
lista2=[1,2,3]
lista3=[]
print(sumowanie_elementow(lista1,lista2,lista3))

lista=[1,23,4,4,5,66]
#1
#2
#3

def fun(x,y):
    suma=x+y
    return suma

print("Podaj liczbę pierwszą)
pierwsza=int(input())
print("Podaj liczbę drugą)
druga=int(input())

print(fun(pierwsza,druga))
