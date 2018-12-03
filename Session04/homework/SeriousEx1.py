items = ["T-Shirt", "Sweater"]
print("Here is my items: ", sep=" ")
print(*items, sep=", ")

loop = True
while loop:
    cmd = input("Welcome to our shop, what do u want (C, R, U, D or exit)? ").upper()
    if cmd == "R":
        print("Our items: ", *items, sep=", ")
    elif cmd == "C":
        new = input("Enter new item: ")
        items.append(new)
        print("Our items: ", *items, sep=", ")
    elif cmd == "U":
        while True:
            position_update = int(input("Update position? "))
            if 0 > position_update or position_update > len(items):
                print("No items in this position, try again!")
            else:
                update = input("Update to new item: ")
                items[position_update - 1] = update
                print("Our items: ", *items, sep=", ")
                break
    elif cmd == "D":
        while True:
            position_del = int(input("Delete position? "))
            if 0 > position_del or position_del > len(items):
                print("No items in this position, try again!")
            else:
                items.pop(position_del)
                print("Our items: ", *items, sep=", ")
                break
    elif cmd == "exit":
        loop = False
    else:
        print("Only chose C, R, U, D or exit!! Try again!")