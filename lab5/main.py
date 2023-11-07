def czy_nalezy(lista, element):
    for i in lista:
        if i == element:
            return True
        else:
            return False


# print(czy_nalezy([1,2,3,4,5,6,7], 8))

def czy_zawiera(lista1, lista2):
    for i in lista1:
        for j in lista2:
            if i == j:
                return True
            else:
                return False


# print(czy_zawiera([1,2,3,4], [3]))

def zad_1a():
    lista = []
    for i in range(1, 11):
        lista.append(i)
    print(lista)


def zad_1b():
    lista = []
    for i in range(0, 22, 2):
        lista.append(i)
    print(lista)


def zad_1c():
    lista = []
    for i in range(1, 11):
        lista.append(i ** 2)
    print(lista)


def zad_1d():
    lista = []
    for i in range(0, 11):
        lista.append(0)
    print(lista)


def zad_1e():
    lista = []
    for i in range(1, 11):
        if i % 2 == 0:
            lista.append(1)
        else:
            lista.append(0)
    print(lista)


def zad_1f():
    lista = []
    for i in range(2):
        for j in range(5):
            lista.append(j)
    print(lista)


def zad_2a():
    lista = []
    i = 1
    while i <= 10:
        lista.append(i)
        i += 1
    print(lista)

def zad_2b():
    lista = []
    i = 0
    while i <= 20:
        lista.append(i)
        i += 2
    print(lista)

def zad_2c():
    lista = []
    i = 1
    while i <= 10:
        lista.append(i ** 2)
        i += 1
    print(lista)

def zad_2d():
    lista = []
    i = 0
    while i <= 10:
        lista.append(0)
        i += 1
    print(lista)

def zad_2e():
    lista = []
    i = 1
    while i <= 10:
        if i % 2 == 0:
            lista.append(1)
        else:
            lista.append(0)
        i += 1
    print(lista)

def zad_2f():
    lista = []
    i = 0
    while i < 2:
        j = 0
        while j < 5:
            lista.append(j)
            j += 1
        i += 1
    print(lista)


def ile_ujemnych(lista):
    count = 0
    for i in lista:
        if i < 0:
            count += 1
    return count

#print(ile_ujemnych([-1, -2, 3, -4, -5, 6]))

def iloczyn(var):
    count = 1
    for i in range(1, 7):
        if i % var == 0:
            count *= i
    return count

#print(iloczyn(2))

