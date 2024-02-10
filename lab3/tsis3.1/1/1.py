class Str:
    def getStr(self):
        self.string = input()

    def printStr(self):
        print(self.string.upper())

privet = Str()
privet.getStr()
privet.printStr()