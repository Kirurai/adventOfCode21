from utils.Reader import Reader
import os

# First Problem
def reducirPorDias( listaPeces ):
    fishByDay = [0]*9 # Siendo que hay días de 0 a 8 de gestación
    for i in listaPeces:
        fishByDay[i] += 1
    return  fishByDay



def pasarDia( pecesPorDia ):
    aux = [0]*9
    for i in range(len(pecesPorDia)):
        if i == 6:
            aux[i] = pecesPorDia[i - len(pecesPorDia) +1] + pecesPorDia[0]
        else:
            aux[i] = pecesPorDia[i - len(pecesPorDia) +1]
    return aux


def contarPeces( pecesPorDia ):
    acc = 0
    for i in pecesPorDia:
        acc += i
    return acc


with Reader( 'Dataset.txt', os.path.dirname( __file__ ) ) as file:
    qOfDays = 80 #Constante de la consigna
    listaPeces = [ int(i) for i in file.readline().split(",") ]

    pecesPorDia = reducirPorDias(listaPeces)
    for i in range(qOfDays):
        pecesPorDia = pasarDia(pecesPorDia)

    print(f'After {qOfDays} days will by {contarPeces( pecesPorDia )} lanternfish')


with Reader( 'Dataset.txt', os.path.dirname( __file__ ) ) as file:
    qOfDays = 256 #Constante de la consigna
    listaPeces = [ int(i) for i in file.readline().split(",") ]

    pecesPorDia = reducirPorDias(listaPeces)
    for i in range(qOfDays):
        pecesPorDia = pasarDia(pecesPorDia)

    print(f'After {qOfDays} days will by {contarPeces( pecesPorDia )} lanternfish')
