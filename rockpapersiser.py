import random
print("Welcome to Rock, Paper, Scissors!")
choices = ['rock', 'paper', 'scissors']
count=0
t=0
while True:
    user = input("Enter Rock, Paper, or Scissors (or 'quit' to exit): ").lower()
    if user == 'quit':
        print("Thanks for playing!")
        if t>count:
            print(f"Your score:{count} ")
            print(f"Computer score:{t} ")
            print("You are Winner!")
        elif t<count:
            print(f"Your score:{count} ")
            print(f"Computer score:{t} ")
            print("You are Losser!")
        else:
            print("Macth Draw")
        break
    if user not in choices:
        print("Invalid input. Try again.")
        continue

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a draw!")
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        print("You win! 🎉")
        count+=1
    else:
        print("Computer wins! 😅")
        t+=1
