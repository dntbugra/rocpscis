def play():
    import random

    def win():
        print("\nKazandın!")
    def draw():
        print("\nBerabere!")
    def lose():
        print("\nKaybettin!")

    moves=("Rock" , "Paper" , "Scissors")

    x=random.choice(moves)

    a=moves[0]
    b=moves[1]
    c=moves[2]

    print("\nHoşgeldin\n")

    # def play():
    print("Taş için 'q' ya , kağıt için 'w' ya , makas için 'e' ye bas\n")

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
