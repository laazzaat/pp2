from math import pi
def SphVolume(x):
    return 4/3 * pi * (x ** 3)

r = int(input("Enter radius: "))
print(SphVolume(r))