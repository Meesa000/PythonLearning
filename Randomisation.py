import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

moves = ["Rock", "Paper", "Scissors"] # List of moves
images = [rock, paper, scissors]
computer_turn = random.choice(moves) # Computer move, random choice from the moves list
player_turn = int(input("Enter rock, paper or scissors: ")) # User input for move


print(f"You chose {player_turn}") # Print what player and computer chose
print(images[player_turn])
print(f"The computer chose {computer_turn}")
print(images[computer_turn])

if player_turn == computer_turn.lower():
    print("It's a tie!")

if player_turn == "rock": # If player chooses rock conditionals
    if computer_turn == "Paper":
        print("The computer won!")
    elif computer_turn == "Scissors":
        print("You won!")

if player_turn == "paper": # If player chooses paper conditionals
    if computer_turn == "Scissors":
        print("The computer won!")
    elif computer_turn == "Rock":
        print("You won!")

if player_turn == "scissors": # If player chooses scissors conditionals
    if computer_turn == "Rock":
        print("The computer won!")
    elif computer_turn == "Paper":
        print("You won!")






#player turn = input enter rock paper or scissors
#if statements for rules
#rock wins vs scissors
#scissors wins vs paper
#paper wins vs rock

#i.e if player turn is rock print(rock)
#if computer turn == paper, player loses
#if computer turn == scissors, pc loses