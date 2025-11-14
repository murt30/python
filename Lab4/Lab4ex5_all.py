import math

choice = int(input("Enter a choice (1,2,3): "))

if choice==1:
    radius=float(input("Enter the radius of the circle: "))
    print("Area of a circle with radius %.2f"%radius," is %.3f"%(pow(radius,2)*math.pi))
elif choice==2:
    radius=float(input("Enter the radius of the cylinder: "))
    height=float(input("Enter the height of the cylinder: "))
    print("volume of a cylinder with radius %.2f"%radius," is %.3f"%(pow(radius,2)*height*math.pi))
else:
    radius=float(input("Enter the radius of the sphere: "))
    print("Volume of a sphere with radius %.2f"%radius," is %.3f"%((4/3)*pow(radius,3)*math.pi))
