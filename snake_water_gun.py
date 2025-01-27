SNAKE, WATER, GUN GAME
'''
1 for snake
-1 for water
0 for gun
'''

import random

def snake_water_game():
    print("Welcome to my Snake, Water, gun Game!")
    print("Rules:")
    print("1. Snake beats Water")
    print("2. Water beats Gun")
    print("3. Gun beats Snake")
    print("Type 's' for Snake, 'w' for Water, 'g' for Gun, or 'exit' to quit.\n")

    # Mapping
    youDict={"s":1,"w":-1,"g":0}
    reverseDict={1:"Snake",-1:"Water",0:"Gun"}

    while True:
        # Computer's choice
        computer = random.choice([1,-1,0])

        # Player's input
        youstr = input("Your turn (s/w/g):").lower()

        if(youstr=="exit"):
            print("Game Exited. Thanks for playing lil bro!")
            break
        if youstr not in youDict:
            print("Invalid Choice! Please enter 's' 'w',or 'g'")
            continue
        # Convert input to its corresponding number
        you = youDict[youstr]
        
        # Display choices
        print(f"\n You chose: {reverseDict[you]}")
        print(f"\n Computer chose: {reverseDict[computer]}")

        # Determine result
        if(computer==you):
            print("It's a Draw!")
        else:
            if(computer==-1 and you ==1) or (computer==0 and you ==-1) or (computer==1 and you ==0):
                print("You Win!")
            else:
                print("You lose!(kal ana)")
        
        print("") #blank line for spacing between rounds
        
#run the game
snake_water_game()
