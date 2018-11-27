#Caculate factorial
a = int(input("Enter a number? "))
f = 1

for i in range(a):
    f = i * (i+1)

print(f)