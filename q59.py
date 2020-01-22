class Person:
    def getGender(self,gender):
        self.gender=gender

class Male(Person):
    def getGender(self,gender):
        return"Male"


class Female(Person):
    def getGender(self,gender):
        return "Female"
gender=input()
if gender=="female"or gender=="Female":
  g=Female().getGender(gender)
  print(g)
else:
    g=Male().getGender(gender)
    print(g)
