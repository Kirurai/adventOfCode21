from utils.Reader import Reader
import os


def sumOfAllUnmarkedNumbers( _matrix ):
    _acc = 0
    for _line in _matrix:
        for _number in _line:
            if not _line[_number]:
                _acc += int(_number)
    return _acc

def checkNumberExistence( _matrix, _number ):
    for _line in _matrix:
        if _number in _line.keys():
            _line[_number] = True
    return _matrix

def trasposeMatrix( _matrix ):
    arr = [{}, {}, {},  {}, {}]
    arrIndex = 0
    for i in range(len(_matrix)):
        for key in _matrix[i]:
            arr[arrIndex][key] = _matrix[i][key]
            arrIndex += 1
        arrIndex = 0
    return arr

def isWinnerLine( _line ):
    return False not in _line.values()

def hasWinnerColumn( _matrix ):
    for _line in _matrix:
        if isWinnerLine(_line):
            return True
    return False

def hasWinnerRow( _matrix ):
    for _line in trasposeMatrix(_matrix):
        if isWinnerLine(_line):
            return True
    return False

def checkForWin( _matrix ):
    return hasWinnerColumn( _matrix ) or hasWinnerRow( _matrix )

# First Problem
def won( _matrix, _lastNumber ):
    _lastNumber = int(_lastNumber)
    _acc = sumOfAllUnmarkedNumbers(_matrix)
    print(f'The value of the sum of all unmarked numbers multiply for first bingo card by the winner number is {_acc*_lastNumber}')

def firstProblem( _numerosSorteados, _cartonesBingo ):
    for _number in _numerosSorteados:
        for _matrix in _cartonesBingo:
            _matrix = checkNumberExistence( _matrix, _number )
            if checkForWin( _matrix ):
                won( _matrix, _number )
                return

# First Problem
with Reader( 'Dataset.txt', os.path.dirname( __file__ ) ) as file:
    numerosSorteados = (file.readline()).replace("\n", "").split(",")
    cartonesBingo = []
    for line in file:
        if line == "\n":
            cartonesBingo.append([])
        else:
            cartonesBingo[-1].append( line.replace("\n", "").replace("  ", " ").strip().split(" ") )
            cartonesBingo[-1][-1] = { i: False for i in cartonesBingo[-1][-1] }

    firstProblem(numerosSorteados, cartonesBingo)

# Second Problem
def lose( _matrix, _lastNumber ):
    _lastNumber = int( _lastNumber )
    _acc = sumOfAllUnmarkedNumbers(_matrix)
    print( f'The value of the sum of all unmarked numbers multiply for first bingo card by the winner number is {_acc * _lastNumber}' )


def cleanCards( _cartonesBingo ):
    indexToDelete = []
    for i in range(len(_cartonesBingo)):
        if _cartonesBingo[i] == {}:
            indexToDelete.append(i)
    for index in indexToDelete:
        _cartonesBingo.pop(-len(_cartonesBingo) + index)
    return _cartonesBingo


def secondProblem( _numerosSorteados, _cartonesBingo ):
    _cartonesResueltos = 0

    for _number in _numerosSorteados:
        for i in range( len( _cartonesBingo ) ):
            if _cartonesBingo[ i ] == True: # No reducible porque puede dar True por otros valores
                continue
            _cartonesBingo[ i ] = checkNumberExistence( _cartonesBingo[ i ], _number )
            if checkForWin( _cartonesBingo[ i ] ):
                _cartonesResueltos += 1
                if _cartonesResueltos == 100:
                    lose( _cartonesBingo[ i ], _number )
                    return

                cartonesBingo[ i ] = True
    _cartonesBingo = cleanCards(_cartonesBingo)


with Reader( 'Dataset.txt', os.path.dirname( __file__ ) ) as file:
    numerosSorteados = (file.readline()).replace("\n", "").split(",")
    cartonesBingo = []
    solved = False
    for line in file:
        if line == "\n":
            cartonesBingo.append([])
        else:
            cartonesBingo[-1].append( line.replace("\n", "").replace("  ", " ").strip().split(" ") )
            cartonesBingo[-1][-1] = { i: False for i in cartonesBingo[-1][-1] }

    secondProblem(numerosSorteados, cartonesBingo)





