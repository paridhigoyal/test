class Circle:
    def area_circle(self,radius):
        area=3.141* radius*radius
        return area
radius=float(input())
print(Circle().area_circle(radius))

