#let user type input

from xml.etree.ElementTree import PI

PI = 3.142 

#caluculate the area of a circle
radius = input("Enter the radius of the circle")
print("The radius of the circle is " + str (radius))
area = PI * int (radius) * int(radius)
print("The area of a circle is " + str (area) + " square centimetres") 


#volume of a cylinder
radius = input("Enter the radius of the cylinder")
height = input("Enter the height of the cylinder")
print("The radius of the cylinder is " + str (radius))
print("The height of the cylinder is " + str (height))
volume = PI * int(radius) * int(radius) * int (height)
print("The volume of the cylinder is " + str (volume))
 

 #surface area of a cylinder 
radius = input("Enter the radius of the cylinder")
height = input("Enter the height of the cylinder")
print("The radius of the cylinder is " + str (radius))
print("The height of the cylinder is " + str (height))
surface_area =  area + (PI * 2 * int (radius)) 
print("The surface area of the cylinder is " + str(surface_area))


  #volume of a cube
Length = input("The length of one side is ?")
print("The Length of one side is " + str(Length))
volume9 = str (Length) * str (Length) * str (Length)
print("The volume of a cube is" +str(volume9))


