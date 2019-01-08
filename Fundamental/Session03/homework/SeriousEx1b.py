#Repeats a block of code as long as the user indicates they want it to

print("Type exit to escape")

loop = True
while loop:
    n = input("Your input: ")
    if n == "exit":
        loop = False