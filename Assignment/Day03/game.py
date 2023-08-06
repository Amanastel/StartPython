import random

def display_welcome_message():
    print("Welcome to Rock, Paper, Scissors game!")
    print("Enter your choice: rock, paper, or scissors")

def get_user_choice():
    user_choice = input().lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
        user_choice = input().lower()
    return user_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"
    
userWins = 0
computerWins = 0
draws = 0

while True:
    display_welcome_message()
    user_choice = get_user_choice()

    # Randomly select computer's choice
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print("Computer chose:", computer_choice)

    winner = determine_winner(user_choice, computer_choice)

    if winner == "draw":
        print("It's a draw!")
        draws += 1
    elif winner == "user":
        print("You win!")
        userWins += 1
    else:
        print("Computer wins!")
        computerWins += 1

    print(f"Score - You: {userWins} | Computer: {computerWins} | Draws: {draws}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break   