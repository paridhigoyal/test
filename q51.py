class American:
   def Nationality(self):
       return"Parent class"
class NewYork(American):
    def Nationality(self):
        return"Child Class"
d=NewYork().Nationality()
print(d)
