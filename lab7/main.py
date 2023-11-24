def dzielniki(liczba):
    wynik = []
    for i in range(1, int(liczba / 2 + 1)):
        if liczba % i == 0:
            wynik.append(i)
    wynik.append(liczba)
    return wynik


def dzielnik_mojPomysl(liczba):
    wynik = []
    for i in range(1, liczba + 1):
        if liczba % i == 0:
            wynik += [i]
    return wynik


def suma(lista):
    wynik = 0
    for i in lista:
        wynik += i
    return wynik


def czy_liczba_jest_doskonala(liczba):
    dziel = dzielniki(liczba)
    suma_dziel = suma(dziel)
    return suma_dziel == liczba


def zad_1b(liczba):
    wynik = []
