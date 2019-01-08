prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

total = 0

for st in prices:
    print(st)
    print("_ price: ", prices[st])
    print("_ stock: ", stock[st])
    a = prices[st] * stock[st]
    total += a
print("Total: ", total)
