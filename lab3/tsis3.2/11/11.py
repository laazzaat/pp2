def isPal(stroka):
    if stroka[::-1] == stroka:
        return True
    return False

a = input("Enter the word: ")
print(isPal(a))