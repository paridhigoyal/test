class num:

    def getstring(self,s):
       self.s=s
    def printstring(self):
        print(self.s.upper())
n=num()
s =''
s = input("enter some input: ")
n.getstring(s)
n.printstring()
