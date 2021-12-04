from utils.Reader import Reader
import os


def _sum( arr ):
    sumOfArray = 0
    for i in arr:
        sumOfArray += i
    return sumOfArray


def newHeights( arr, newInt ):
    arr[ 0 ] = arr[ 1 ]
    arr[ 1 ] = arr[ 2 ]
    arr[ 2 ] = newInt
    return arr


# First Problem
with Reader( 'Dataset.txt', os.path.dirname( __file__ ) ) as file:
    lastOne = int( file.readline() )
    deep = 0

    for line in file:
        x = int( line )
        if x > lastOne:
            deep += 1
        lastOne = x

    print( f"The times that the submarine increments his deep was { deep }" )

# Second Problem
with Reader( 'Dataset.txt', os.path.dirname( __file__ ) ) as file:
    firstWindow = [ 0, int( file.readline() ), int( file.readline() ) ]
    secondWindow = [ firstWindow[1], firstWindow[2], int( file.readline() ) ]
    deep = 0
    for line in file:
        firstWindow = newHeights( firstWindow, secondWindow[ 2 ] )
        secondWindow = newHeights( secondWindow, int( line ) )
        firstSum = _sum( firstWindow )
        secondSum = _sum( secondWindow )
        if secondSum > firstSum:
            deep += 1

    print( f"The times that the submarine increments his deep with the 3 sum of measures was { deep }" )
