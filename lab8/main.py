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


# print(dzielniki(6))

def czesc_wspolna(lista1, lista2):
    wynik = []
    for i in lista1:
        for j in lista2:
            if i == j:
                wynik += [i]
    return wynik


# print(czesc_wspolna([1, 3, 8, 3, 2], [1, 5, 8, 2]))

def suma(liczba):
    wynik = 0
    for i in range(1, liczba + 1):
        if liczba % i == 0:
            wynik += i
    return wynik


# print(suma(6))

def czy_wzglednie_pierwsza(liczba1, liczba2):
    d1 = dzielniki(liczba1)
    d2 = dzielniki(liczba2)
    iloczyn = czesc_wspolna(d1, d2)
    return len(iloczyn) == 1 and iloczyn[0] == 1

# print(czy_wzglednie_pierwsza(1, 2))


def unikalnosc(lista):
    wynik_lista = []
    for i in lista:
        if not czy_nalezy(wynik_lista, i):
            wynik_lista.append(i)
    return wynik_lista

print(unikalnosc([2,1,3,7,2,1,4,4,5]))