# take snake water gun input
# computer choose snake water gun
# 
import random
gameMap = {
        "SNAKE": 0,
        "WATER": 1,
        "GUN": 2,
        "EXIT": 3
    }

def play(userInput):
    # logic goes here
    computerInput = random.choice(["SNAKE","WATER","GUN"]);
    print(f"computer plays {computerInput}")
    winMatrix = [["DRAW","WIN","LOOSE"],["LOOSE","DRAW","WIN"],
                 ["WIN","LOOSE","DRAW"]]
    result = winMatrix[userInput][gameMap[computerInput]]

    return result



if __name__ == "__main__":
    print("--SNAKE - WATER - GUN ---")
    print("1. SNAKE")
    print("2. WATER")
    print("3. GUN")

    cont = 1
    while(cont):
        userInput = input("What would you like to use SNAKE/WATER/GUN/Exit: ")
        userInput = userInput.upper()
        if gameMap[userInput] == 3:
            cont = 0
        else:
            result = play(gameMap[userInput])
            print(f"You {result}")
    
    print("Good Bye !!!")
