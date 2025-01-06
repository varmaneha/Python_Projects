print("Welome to the treasure island!\nYour mission is to find a treasure!")
choice1 = input('You are at cross road. Where do you want to go ?\n Type "Left" or "Right". ').lower()

if choice1 == "left":
    choice2 = input('You have come to a lake. There is an island in the middle of the lake.' 
                     'Type "wait" for a boat or "swim" to across ' ).lower()
    if choice2 == "wait":
        choice3 = input('You have arrived at the island unharmed.'
              'There is a house with 3 doors. '
              'One "red" one "yellow" and one "blue"'
              'Which color do you choose ').lower()
        if choice3 == "red":
            print("Its a room full of fire. Game Over!")
        elif choice3 == "yellow":
            print("You found the treasure, You win!")
        elif choice3 == "blue":
            print("You enter a room full of beast. Game Over!")
        else:
            print("You chose a door that doesnt exist. game Over!")            
    else:
        print("You have got attacked by an angry trout. Game Over")       
else:
    print("You fell into a hole. game over")
        
    
    
    
    