import random 

choice = random.choice( ['up', 'down', 'left', 'right'] )
print("Welcome to the labyrinth Travel Game!")
print("You can choose directions: 'up', 'down', 'left', 'right'")
print("Type 'exit' to leave the game.")
i = 3
while i > 0:
    guess = input("Choose directions to go:")
    i = i - 1
    if choice == guess:
        print("You found the exit! Congratulations!",choice)
        break
    if guess == "exit":
        print("Exit the labyrinth Travel Game!  ")
        break
    elif choice != guess:
        print(f"You have {i} move left",)
        if i == 0:
            print("You could not find the exit within the allowed moves.")
    


    







