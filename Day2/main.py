from utils.Reader import Reader
import os

def splitCommand( cmd="" ):
    arr = cmd.split(" ")
    arr[1] = int(arr[1])
    return arr

# First Problem
with Reader( 'Dataset.txt', os.path.dirname( __file__ ) ) as file:
    position = {"up": 0,
                "down": 0,
                "forward": 0}
    for line in file:
        command = splitCommand(line)
        position[command[0]] += command[1]

    print(f'Horizontally the submarine moves { position["forward"] } at { position["down"] - position["up"] } ')
    print(f'If you multiply both values obtain you\'ll { position["forward"] * (position["down"] - position["up"]) } ')
    print()


# Second Problem
with Reader( 'Dataset.txt', os.path.dirname( __file__ ) ) as file:
    position = {"forward": 0,
                "aim": { "up" : 0,
                         "down": 0 },
                "deep": 0}
    for line in file:
        command = splitCommand(line)
        if command[0] =="forward":
            position[command[0]] += command[1]
            position["deep"] += ( position["aim"]["down"] - position["aim"]["up"]  ) * command[1]
        else:
            position['aim'][command[0]] += command[1]


    print(f'Horizontally the submarine moves { position["forward"] } at { position["deep"] } ')
    print(f'If you multiply both values obtain you\'ll { position["forward"] * position["deep"] } ')
    print()