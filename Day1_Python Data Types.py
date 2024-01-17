print("hello world")


## LIST
a = [1,5.6,'Sakshi',True]
print(a)
a[2]=5.7    #List is mutable
a.append("Ghosalkar")
a.remove(1)
print("List: ",a)
print()

## TUPLE
#immutable
b = (4,5.7,'Sakshi',True)
print("Tuple: ",b)
#  b[0]=5   #immutable- cannot be changed
print()

## DICTIONARY - Key_Value Pair

c = {"Name":"Sakshi1", "Age":25, "Gender":"Female"}
print(c)
print(c["Name"])
c["education"]= 'B-Tech'     #Addnew item to dictionary
print("Dictionary_1: ",c)
del c["Gender"]
print("Dictionanry_2: ",c)
print()



## SET - removes duplicate items

d = {1,2,4,5,3,2,4}
print(d)
d.add(7)
print("set_1:", d)  #Add value to set
d.remove(5)
print("Set_2:", d)  #Remove value from set
print()

#******************DATA TYPES IN PYTHON*****************






