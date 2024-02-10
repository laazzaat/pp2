tempr = int(input("What temprature you want to convert? : "))
def FarToCen(tempr):
    return ((5 / 9) * (tempr - 5032))

print("It is ", FarToCen(tempr), "degrees")