# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
username = input("Please add your name: ")
print(f"Hello {username}, Lets play a game!")
user = input("Do you want to play game? yes/no \n").lower()
secret_number = 6
guess_num = 0
guess_limit = 3
if user == "yes":
    print("Game started")
    while guess_num < guess_limit:
        guess = input("Guess a number: ")
        guess_num += 1
        if guess == secret_number:
            print(f"Hey {username} You won!")
            break
    else:
        print("You Failed!")
else:
    print("start to start the game")

        




