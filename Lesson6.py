#learning about lists 
motorcycle_owner = "Mojo Jojo"
plate_number = ['H1234','Y1234','S1234','B1234']
motorcycle = ['Honda','Yamaha','Suzuki'] 
print(motorcycle) 

#accessing list items using index 
print(motorcycle[0]) 

#changing elements in a list
#motorcycle[0] = "Bugatti" 
print(motorcycle) 
print("i love " + str(motorcycle[0]) )

#adding elements in a list
motorcycle.append('Bugatti') #appending only takes one item
print(motorcycle)  

#putting each motorcycle with its plate numbers
print(str(motorcycle[0]) + "  " + str(plate_number[0])) 
print(str(motorcycle[1]) + "  " + str(plate_number[1])) 
print(str(motorcycle[2]) + "  " + str(plate_number[2]))
print(str(motorcycle[3]) + "  " + str(plate_number[3]))

#deleting an item from a list 
#del motorcycle[0]
#print(motorcycle) 

#pop removes the last index on your list
#popped_motorcycle = motorcycle.pop()
#print(motorcycle) 
#print(popped_motorcycle) 

#task
print("My name is {} and I own a motorcycle {} plate number {}".format(motorcycle_owner,motorcycle[0],plate_number[0]))

#removing an item from a list
motorcycle.remove('Suzuki') 
print(motorcycle) 

school = ['Joy','Hope','Mercy','Happy']
pupil = ['Peace','Patience','Amani','Charity'] 

#task(each pupil and their own school)
#hard way
#print(f"{pupil[0]} goes to {school[0]}
#print(f"{pupil[1]} goes to {school[1]}
#print(f"{pupil[2]} goes to {school[2]}
#print(f"{pupil[3]} goes to {school[3]}

print(f"{pupil[0]} goes to {school[0]} \n{pupil[1]} goes to {school[1]} \n{pupil[2]} goes to {school[2]} \n{pupil[3]} goes to {school[3]} ") 

#simplified
for pupil in pupil:
    print(f'Hello I am pupil {pupil}')

