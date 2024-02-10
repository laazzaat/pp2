from itertools import permutations

def Perms(stroka):
    perms = permutations(stroka)

    for perm in perms:
        print("".join(perm))

stroka = input("Enter a string: ")
print("Permutations of the string:")
Perms(stroka)