# 2.1:
print("Hello, my name is Truong and these are my sheep sizes ")
sizes = [5, 7, 300, 90, 24, 50, 75]
print(sizes)

# 2.2:
a = max(sizes)
print("My biggest sheep has size ", a, " let's shear it")

# 2.3:
print("After shearing here is my flock")
b = sizes.index(a)
sizes[b] = 8
print(sizes)

# 2.4:
for i in range(len(sizes)-1):
    sizes[i] = sizes[i] + 50
print("One month has passed, now here is my flock")
print(sizes)
