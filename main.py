import random

def win():
    print("\nYou win!")
def draw():
    print("\nIt's a draw!")
def lose():
    print("\nYou lose!")

moves=("Rock" , "Paper" , "Scissors")

x=random.choice(moves)

a=moves[0]
b=moves[1]
c=moves[2]

print("\nWelcome\n")

def play():
    print("Press q for -> 'rock', w for 'paper' , e for 'scissors'\n")

    pm=input()

    if x==a:
        if pm=="q":
            draw()
        elif pm=="w":
            win()
        elif pm=="e":
            lose()
    if x==b:
        if pm=="q":
            lose()
        elif pm=="w":
            draw()
        elif pm=="e":
            win()
    if x==c:
        if pm=="q":
            win()
        elif pm=="w":
            lose()
        elif pm=="e":
            draw()
    print("=" * 50 + "\n")

while True:
    play()
