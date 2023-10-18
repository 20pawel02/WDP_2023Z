def zad_1a():
    print(sum(range(2, 102, 2)))


def zad_1b():
    print(sum(i ** 2 for i in range(1, 101)))


def zad_1c():
    print(sum(2 ** i for i in range(1, 64)))


def zad_1d(a, b):
    if a > b:
        print(0)
    else:
        wynik = 0
        for i in range(a, b + 1):
            if i % 2 != 0:
                wynik += i
        print(wynik)


def zad_2a(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    print(suma)


def zad_2b(n):
    iloczyn = 1
    for i in range(1, n + 1):
        iloczyn *= i
    print(iloczyn)


def zad_2c(n):
    suma = 0
    for i in range(1, n + 1):
        if i < 0:
            i = i * -1
        suma += i
    print(suma)


def zad_2d(n):
    suma = 0
    for i in range(1, n + 1):
        if i < 0:
            i = i * -1
        suma += i ** (1 / 2)
    print(suma)


def zad_2e(n):
    suma = 0
    for i in range(1, n + 1):
        if i < 0:
            i = i * -1
        suma *= i
    print(suma)


def zad_2f(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i ** 2
    print(suma)


def zad_2g(n):
    suma = 0
    iloczyn = 1
    for i in range(1, n + 1):
        suma += i
        iloczyn *= i
    print("suma:", suma)
    print("iloczyn:", iloczyn)


def zad_3(var_1, var_2):
    var_1 = eval(input("podaj ilosc elementow w ciagu"))
   