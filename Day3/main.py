from utils.Reader import Reader
import os

def split(word):
    arr = []
    for char in word:
        if char == "0" or char == "1":
            arr.append(int(char))

    return arr

def _sum(arr = [], number=""):
    for i in range(len(arr)):
        arr[i] += int(number[i])
    return arr

def reduceFromBinary(arr = []):
    res = 0
    if len(arr):
        res = int("".join(repr(str(n)) for n in arr).replace("'", ""), 2)
    return res


gamma = []
epsilon = []

# First Problem
with Reader( 'Dataset.txt', os.path.dirname( __file__ ) ) as file:
    count = split(file.readline())
    size = 0
    for line in file:
        count = _sum(count, line)
        size += 1

    for number in count:
        gamma.append( 0 if number < size/2 else 1)
        epsilon.append( 1 if number < size/2 else 0 )

    print(f'The consumption of the submarine is {reduceFromBinary(gamma)*reduceFromBinary(epsilon)}')


# Second Problem
def searchMostAppeared( original, _index = 0 ):
    arrOfZeros= []
    arrOfOnes= []
    for _number in original:
        ( arrOfZeros if _number[_index] == "0" else arrOfOnes ).append(_number)
    return arrOfOnes if len(arrOfOnes) >= len(arrOfZeros) else arrOfZeros

def searchLessAppeared( original, _index = 0 ):
    arrOfZeros= []
    arrOfOnes= []
    for _number in original:
        ( arrOfZeros if _number[_index] == "0" else arrOfOnes ).append(_number)
    return arrOfOnes if len(arrOfOnes) < len(arrOfZeros) else arrOfZeros


with Reader( 'Dataset.txt', os.path.dirname( __file__ ) ) as file:
    oxygen = []
    co2 = []
    index = 0
    for line in file:
        line = line.replace("\n", "")

        if  line[0] == str(gamma[ 0 ]) :
            oxygen.append( line )
        else:
            co2.append( line )

    while len(oxygen) > 1 or len(co2) > 1:
        index += 1
        if len(oxygen) > 1:
            oxygen = searchMostAppeared(oxygen, index)

        if len( co2 ) > 1:
            co2 = searchLessAppeared(co2, index)

    print(f'The consumption of the submarine is { reduceFromBinary(oxygen)*reduceFromBinary(co2) }')

