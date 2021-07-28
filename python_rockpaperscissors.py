import random
def linebreak():
    print("--------------------------------------")

def intro():
    print("--------------------------------------")
    print('Welcome to Rock Paper Scissors!')
    print("--------------------------------------")
    print("Main Menu")
    print("--------------------------------------")
    print("Enter \"help\" for instructions")
    input("Press enter to play")


def rock():
    rock = ['rock', '0', '2']
    return rock

def paper():
    paper = ['paper', '1', '11']
    return paper

def scissors():
    scissors = ['scissors', '2', '21']
    return scissors

def getinfo(component, i):
    value = (component[i])
    return value

intro()
linebreak()
linebreak()

first_choice = input('Rock, paper or scissors? Type in one of the following and hit enter.\n')
first_choice = first_choice.lower()
get_number = random.choice([0, 1, 2])
components = ['rock', 'paper', 'scissors']
computer_turn = components[get_number]

func_to_run = globals()[first_choice]
func2_to_run = globals()[computer_turn]
value = getinfo(func_to_run(),2)
value2 = getinfo(func2_to_run(),2)
total = int(value) - int(value2)

if total == 0:
    result = "Tie!"
elif total == -19 or total == 9 or total == 10:
    result = "You Lose!"
elif total == -10 or total == 19 or total == -9:
    result = "You Win!"
else:
    result = "Error"

print(f'You picked {first_choice}. The computer picked {computer_turn}.\n{result}')
