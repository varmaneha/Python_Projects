import random
print("Welcome to the Rock, Paper and Scissor Game ")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper = '''____
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissor = '''
______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissor]
user_input = int(input("Choose 0 for Rock, 1 for Paper and 2 for Scissor\n"))
print(game_images[user_input])

computer_input = random.randint(0,2)
print(game_images[computer_input])

if user_input >= 3 or user_input < 0:
    print("You enter an invalid number, You lose!")
elif user_input == 0 and computer_input == 2:
    print("You win!")
elif computer_input == 0 and user_input == 2:
    print("You lose!")
elif computer_input > user_input:
    print("You lose!")
elif user_input > computer_input:
    print("You win")
elif computer_input == user_input:
    print("Its a draw!")

