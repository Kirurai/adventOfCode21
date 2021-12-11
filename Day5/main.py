from utils.Reader import Reader
import os


def isVerticalLine( xComponentStart, xComponentEnd ):
    return  xComponentStart == xComponentEnd

def isHorizontalLine( yComponentStart, yComponentEnd ):
    return  yComponentStart == yComponentEnd

def isDiagonalLine( xComponentStart, yComponentStart, xComponentEnd, yComponentEnd ):
    return  (abs( xComponentStart - yComponentStart ) == abs( xComponentEnd - yComponentEnd )) or \
            ( xComponentStart + yComponentStart  ==  xComponentEnd + yComponentEnd )

def bringLargerNumber( original, possibleLargers = [] ):
    larger = original
    for i in possibleLargers:
        larger = i if larger < i else larger
    return  larger

def bringDataAsInt( line ):
    return [ int(i) for i in line.replace("\n", "").replace(" -> ", ",").split(",") ]

def vectorUnitario( first, second ):
    return int((second - first)/abs(second - first))

def countOverlaps( overlapMatrix ):
    acc = 0
    for i in overlapMatrix:
        for j in i:
            if j > 1:
                acc += 1
    return acc

# First Problem
def solveFirstProblem( startPoints, endPoints, overlapMatrix ):
    for start, end in zip(startPoints, endPoints):
        if isVerticalLine(start[0], end[0]):
            for i in range(abs(start[1] - end[1]) + 1):
                overlapMatrix[ start[0] ][ start[1] + i*vectorUnitario( start[1], end[1] ) ] += 1
        if isHorizontalLine(start[1], end[1]):
            for i in range(abs(start[0] - end[0]) + 1):
                overlapMatrix[ start[0] + i*vectorUnitario( start[0], end[0] ) ][start[1] ] += 1
        if isDiagonalLine( start[0], start[1], end[0], end[1]):
            for i in range(abs(start[0] - end[0]) + 1):
                overlapMatrix[ start[0] + i*vectorUnitario( start[0], end[0] ) ][start[1] + i*vectorUnitario( start[1], end[1] ) ] += 1
    print(f'Are {countOverlaps( overlapMatrix )} that have at least 2 lines overlap' )

with Reader( 'Dataset.txt', os.path.dirname( __file__ ) ) as file:
    startPoints = []
    endPoints = []
    maxNumber = 0
    overlapMatrix = []
    for line in file:
        xInicio, yInicio, xFinal, yFinal = bringDataAsInt(line)
        if isVerticalLine( xInicio, xFinal) or isHorizontalLine( yInicio, yFinal):
            maxNumber = bringLargerNumber( maxNumber, [ xInicio, yInicio, xFinal, yFinal ])
            startPoints.append( [xInicio, yInicio] )
            endPoints.append( [xFinal, yFinal] )

    for i in range(maxNumber + 1):
        overlapMatrix.append([0]*(maxNumber +1))

    solveFirstProblem(startPoints, endPoints, overlapMatrix)



# Second Second
def solveSecondProblem( startPoints, endPoints, overlapMatrix ):
    for start, end in zip(startPoints, endPoints):
        if isVerticalLine(start[0], end[0]):
            for i in range(abs(start[1] - end[1]) + 1):
                overlapMatrix[ start[0] ][ start[1] + i*vectorUnitario( start[1], end[1] ) ] += 1
        if isHorizontalLine(start[1], end[1]):
            for i in range(abs(start[0] - end[0]) + 1):
                overlapMatrix[ start[0] + i*vectorUnitario( start[0], end[0] ) ][start[1] ] += 1
        if isDiagonalLine( start[0], start[1], end[0], end[1]):
            for i in range(abs(start[0] - end[0]) + 1):
                overlapMatrix[ start[0] + i*vectorUnitario( start[0], end[0] ) ][start[1] + i*vectorUnitario( start[1], end[1] ) ] += 1
    print(f'Are {countOverlaps( overlapMatrix )} that have at least 2 lines overlap' )


with Reader( 'Dataset.txt', os.path.dirname( __file__ ) ) as file:
    startPoints = []
    endPoints = []
    maxNumber = 0
    overlapMatrix = []
    for line in file:
        # Por los ejemplo de la web, parece que los puntos son primero ordenada y luego abscisa
        yInicio, xInicio, yFinal, xFinal = bringDataAsInt(line)
        if isVerticalLine( xInicio, xFinal) or isHorizontalLine( yInicio, yFinal) or isDiagonalLine(xInicio, yInicio, xFinal, yFinal):
            maxNumber = bringLargerNumber( maxNumber, [ xInicio, yInicio, xFinal, yFinal ])
            startPoints.append( [xInicio, yInicio] )
            endPoints.append( [xFinal, yFinal] )

    for i in range(maxNumber + 1):
        overlapMatrix.append([0]*(maxNumber +1))

    solveSecondProblem(startPoints, endPoints, overlapMatrix)


