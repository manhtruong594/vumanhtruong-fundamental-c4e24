import sys

sys.stdout.flush()

# 20 x 1 stars:
for i in range (20):
    print("* ", end="")
print()

# n stars (n is entered by users)
n = int(input("n= "))
for i in range(n):
    print("* ", end="")
print()

# 9 stars and xs in total
for i in range(4):
    print("x * ", end="")
print("x")
print()

# n stars and xs in total (n is entered by users)
n = int(input("n= "))
a = int(n/2)
for i in range(a):
    print("x * ", end="")
print("x")
print()

# 7 x 3 stars
for j in range(3):
    for i in range(7):
        print("* ", end="")
    print()

# n x m stars (n, m are entered by users)
n = int(input("n= ")) 
m = int(input("m= "))
for i in range(m):
    for j in range(n):
        print("* ", end="")
    print()




