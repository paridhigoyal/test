class Rectangle:
    def area_rectangle(self,length,breadth):
        area=length*breadth
        return area
length,breadth=float(input()),float(input())
print(Rectangle().area_rectangle(length,breadth))
