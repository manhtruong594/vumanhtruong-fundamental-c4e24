# Implement guess my number game

n = int(input("My number is: "))

loop = True
while loop:
    a = int(input("Your number is: "))
    if a < n:
        print("Too small :(")
    elif a>n :
        print("Too large :'(")
    else :
        print("Bingo")
        loop = False