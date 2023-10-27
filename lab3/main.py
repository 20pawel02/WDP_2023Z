'''
na wejsciowke:
- to co na pierwszej wejsciowce
- wszystko to co ponizej
- zdefiniowanie funkcji
'''


def zad1():
    imie = input("podaj swoje imie: ")
    wiek = int(input("podaj swoj wiek (w latach): "))
    print(f'Twoje imie to: {imie}\nTwoj wiek to: {wiek} lat')


def zad2():
    print('wdp ' + 'jest ' + 'najlepsze')
    print(3 * 'tak jest\n')


def zad3():
    fraza = 'wdp ' + 'jest ' + 'najlepsze'
    print(fraza[0])
    print(fraza[:3])
    print(fraza[3:])
    print(fraza[3:2])
    print(fraza[-1])
    print(fraza[:-3])
    print(fraza[-3:])


def suma(lista):
    wynik = 0
    for i in lista:
        wynik += i
    return wynik
