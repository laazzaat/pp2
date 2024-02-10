def histogram(listik):
    for x in range(len(listik)):
        print("*" * listik[x])

listik = list(map(int, input("Enter the data: ").split()))
histogram(listik)