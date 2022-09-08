import random

def win():
    print()
    print("You win!")
def draw():
    print()
    print("It's a draw!")
def lose():
    print()
    print("You lose!")

moves=("Rock" , "Paper" , "Scissors")

x=random.choice(moves)

a=moves[0]
b=moves[1]
c=moves[2]

print()
print("Welcome")
print()
print("Press q for -> 'rock', w for 'paper' , e for 'scissors'")
print()

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
print()