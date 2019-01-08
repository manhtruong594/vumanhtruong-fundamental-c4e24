def is_inside(a,b):
    if b[0] <= a[0] <= (b[0] + b[2]) and b[1] <= a[1] <= (b[1] + b[3]):
        return True
    else:
        return False

print(is_inside([150, 30],[140, 60, 50, 100]))