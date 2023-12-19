#  =======User Input and Control Flow======

        # Vamos a crear un juego, piedra papel o tijeras.
        
# value = input("Please enter a value:\n")

# print(value)
import sys
import random
from enum import Enum# vamos a importar "enums" que son los ennumeradores.

class RPS(Enum): # Aqui creamos una clase con el nomnbre de "RPS" y con "Enum" el cual lo importamos desde enum.
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    # Esto basicamente son las clases que creamos y les dimos un nombre, estan en mayusculas porque "no se pueden cambiar"
    

print("")

playerchoice = input("Enter...\n1 for Rock.\n2 for Paper.\n3 for Scissors.\n\n") # ahora vamos a implementar el "control flow" y "operadores logicos"

player = int(playerchoice) # se tiene que poner una variable nueva con el "int" para que el "playerchoice" se pueda leer como un "int"

if player < 1 or player > 3: # truco nuevo, copie el "player" con "ctrl + c" y luego seleccione el "playerchoice" de abajo con "ctrl + d" para seleccionar los 2 "playerchoice" y luego precionar " ctrl + v" para pegar el "player"
    exit.sys("You must enter 1, 2, or 3.") # el "exit.sys" es para terminar el proceso de arriba.
    
computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("Yuo chose " + str(RPS(player)).replace('RPS.', '') + "." )
print("Python chose " + str(RPS(computer)).replace('RPS.', '') + "." )
print("")

if player == 1 and computer == 3:
    print("🎉 You Win!")
elif player == 2 and computer == 1:
    print("🎉 You Win!")
elif player == 3 and computer == 2:
    print("🎉 You Win!")
elif player == computer:
    print("😲 Tie Game")
else:
    print("🐍 Python Wins!")