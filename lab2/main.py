def zad_1a():
    print(sum(range(2, 102, 2)))

def zad_1b():
    print(sum(i**2 for i in range(1, 101)))

def zad_1c():
    print(sum(2**i for i in range(1, 64)))

def zad_1d(a, b):
    if a > b:
        print(0)
    else:
        wynik = 0
        for i in range(a, b+1):
            if i % 2 != 0:
                wynik += i
        print(wynik)
zad_1d(1,5)