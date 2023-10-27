def zad1_1():
    f1 = float(input("Podaj liczbe zmiennoprzecinkowa: "))
    if f1 < 0:
        f1 *= -1
    return f1


# print(zad1_1())


# -------------------------------------------------------------------------
# liczba = float(input("Podaj liczbe zmiennoprzecinkowa: "))
def absNew(liczba):
    if liczba < 0:
        liczba *= -1
    return liczba


# print(absNew(liczba))


# -------------------------------------------------------------------------
# liczba = int(input("Podaj liczbe: "))
def sgn(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    return 0


# print(sgn(liczba))

# -------------------------------------------------------------------------
# f1 = float(input("Podaj liczbe zmiennoprzecinkowa: "))
# f2 = float(input("Podaj liczbe zmiennoprzecinkowa: "))
def zad3(f1, f2):
    if f2 > 0:
        wynik = f1 / f2
        return wynik
    else:
        return -1


# print(zad3(f1, f2))

# -------------------------------------------------------------------------
def zad4(a, b):
    if a == 0:
        print("funkcja jest stala")
        return 0
    else:
        print("pierwiastek funkcji to: ")
        return (-(b / a))


# print(zad4(1, 3))

# -------------------------------------------------------------------------
def zad5a(n):
    return 0


# -------------------------------------------------------------------------
def zad5b(n):
    return 0


# -------------------------------------------------------------------------
import random


def generuj(len, min, max):
    wynik = []
    for i in range(len):
        liczba = random.randint(min, max)
        wynik.append(liczba)
    return wynik

# print(generuj(10, 1, 15))
# -------------------------------------------------------------------------
