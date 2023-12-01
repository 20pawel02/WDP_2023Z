def czy_nalezy(lista, element):
    for i in lista:
        if element in lista:
            return True
    return False


def dzielniki(liczba):
    lista = []
    for i in range(1, liczba + 1):
        if liczba % i == 0:
            lista += [i]
    return lista


def czesc_wspolna(lista1, lista2):
    wynik = []
    for i in lista1:
        for j in lista2:
            if i == j:
                wynik += [i]
    return wynik


def suma(liczba):
    wynik = 0
    for i in range(1, liczba + 1):
        if liczba % i == 0:
            wynik += i
    return wynik


def czestosc(lista):  # moj pomysl (chatu >:3)
    wynik = {}
    for i in lista:
        i = i.lower();
        if i in wynik:
            wynik[i] += 1
        else:
            wynik[i] = 1
    return wynik

# print(czestosc("Perhaps"))
