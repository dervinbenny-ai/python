import Graphics
from Graphics import Circle, Rectangle
from Graphics.threeDGraphics import Cuboid, Sphere
from Graphics.Circle import *

rad1=float(input("Enter the radius of the Circle:"))
print("Area of circle is :",Circle.area_circle(rad1))
print("Perimeter of circle is:",Circle.perimeter_circle(rad1))

len1=float(input("Enter the length of the Rectangle:"))
breadth1=float(input("Enter the breadth of the Rectangle:"))
print("Area of Rectangle is:",Rectangle.area_rec(len1,breadth1))
print("Perimeter of rectangle is:",Rectangle.perimeter_rec(len1, breadth1))

len2=float(input("Enter the length of the Cuboid:"))
breadth2=float(input("Enter the breadth of the Cuboid:"))
height=float(input("Enter the height of the Cuboid:"))
print("Area of cuboid is:",Cuboid.area_cuboid(len2,breadth2,height))
print("Perimeter of cuboid is:",Cuboid.perimeter_cuboid(len2,breadth2,height))

rad2=float(input("Enter the radius of the Sphere:"))
print("Area of sphere is :",Sphere.area_sphere(rad2))
print("Perimeter of sphere is:",Sphere.perimeter_sphere(rad2))