def czy_nalezy(lista, element):
    for i in lista:
        if element in lista:
            return True
    return False


def czy_zawiera(lista1, lista2):
    for elem in lista2:
        if not czy_nalezy(lista1, elem):
            return False
    return True


def reverse(napis):
    wynik = ""
    l = len(napis)
    for elem in range(l):
        wynik += napis[l - elem  - 1]


def palindrome(napis):
    for elem in napis:
        if reverse(napis):
            return False
    return True

print(palindrome("kajaa"))