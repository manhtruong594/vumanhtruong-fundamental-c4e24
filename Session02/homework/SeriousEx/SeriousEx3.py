# Print without moving to a new line

import sys

sys.stdout.flush()

print("Hello", end="")
print(", my name", end="")
print(" is B-max", end="")

