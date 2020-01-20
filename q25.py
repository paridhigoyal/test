class Student:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
    def display(self):
        print()
        print("Name: %s \n Age: %d"%(self.name, self.age))
std1=Student("Pari",21)
std2=Student("Varsha",22)
std1.display()
std2.display()

