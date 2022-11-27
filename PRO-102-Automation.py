# I am automating the process of calculating volume of some simple 3-D Shapes
valid = False

def Cube(side):
    # Volume of Cube is cube of the side
    return ("Volume of Cube is " + str(round(pow(side,3),2)) + " unit. cu.")
    
def Cuboid(l,b,h):
    # Volume of Cuboid is the product of all three sides
    return ("Volume of Cuboid is " + str(round(l*b*h,2)) + " unit. cu.")

def Cone(r,h):
    # Volume of Cone is the product of Pie,square of radius and height whole divided by 3
    return ("Volume of Cone is " + str(round(((1/3)*(22/7)*(pow(r,2))*(h)),2)) + " unit. cu.")

def Cylinder(r,h):
    # Volume of Cylinder is the product of Pie,square of radius and height
    return ("Volume of Cylinder is " + str(round(((22/7)*(pow(r,2))*(h)),2)) + " unit. cu.")

def Sphere(r):
    # Volume of Sphere is the product of 4,Pie,and cude of radius whole divided by 3
    return ("Volume of Sphere is " + str(round(((4/3)*(22/7)*(pow(r,3))),2)) + " unit. cu.")

def Hemisphere(r):
    # Volume of Hemisphere is the product of 2,Pie,and cude of radius whole divided by 3
    return ("Volume of Hemi-Sphere is  " + str(round(((2/3)*(22/7)*(pow(r,3))),2)) + " unit. cu.")

shape = ''
while valid == False:
    x = str(input("Chose Shape from (Cube, Cuboid, Cone, Cylinder, Sphere, Hemisphere) : ")).lower()
    if x in ['cube','cuboid','cone','cylinder','sphere','hemisphere']:
        valid = True
        shape = x
    else:
        print('Please only input name of shape')

if shape == 'cube':
    a = input("Enter the Dimentions in the following way(side): ") 
    print(Cube(float(a)))
elif shape == 'cuboid':
    l,b,h = input("Enter the Dimentions in the following way(length breadth height): ").split()
    print(Cuboid(float(l),float(b),float(h)))
elif shape == 'cone':
    r,h = input("Enter the Dimentions in the following way(radius height): ").split()
    print(Cone(float(r),float(h)))
elif shape == 'cylinder':
    r,h = input("Enter the Dimentions in the following way(radius height): ").split()
    print(Cylinder(float(r),float(h)))    
elif shape == 'sphere':
    r = input("Enter the Dimentions in the following way(radius): ").split()
    print(Sphere(float(r)))
elif shape == 'hemisphere':
    r = input("Enter the Dimentions in the following way(radius): ").split()
    print(Hemisphere(float(r)))