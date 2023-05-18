# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def get_username_and_greet(name):
    print("Welcome!")
    print(f"Hello {username}, Lets play a game!")

username = input("Please add your name: ")

get_username_and_greet(username)
user = input("Do you want to play game?(yes/no) ")   

secret_number = 6
guess_num = 0
guess_limit = 3
if user == "yes":
    print("Game started")
    while guess_num < guess_limit:
        try:
            guess = int(input("Guess a number: "))
            guess_num += 1
        except ValueError:
            print("Invalid, you are asked to enter a number")
        

        if guess == secret_number:
            print(f"Hey {username} You won!")
            break
    else:
        print(f"{username} You Failed!")
elif user == 'no':
    print("You said no.")
else:
    print("Sorry I do not undrestand that.\nYou need to write yes if you want to play and no if you do not want to play.")
        




