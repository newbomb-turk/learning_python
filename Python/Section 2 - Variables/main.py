#Variable = Container for a value. Python is sort of a typeset. You can define types but it can also convert. 
#You get to reference variables without any special character. 


##
#Strings
##

#Use double quotes to define a string
first_name = "Newbomb"

#This will print out Newbomb
print(first_name)

#This will print out first_name
print("first_name")

#To combine constant text with string variables, use f string. 
#when you use f string, you must put your variable in brackets. 
print(f"Hello {first_name}")


##
#Intgers
##

#whole numbers only, does not use quotes. Can do math with Integers. 
age = 28

#Prints out 28
print(age) 

#Prints out "I am 28 years old"
print(f"I am {age} years old")


##
#Floats
##

#Much like integers but supports decimal numbers
price = 19.99

#Prints out 19.99
print(price)

#Can still use f string for more complex output
print(f"The cost of this item is ${price}")


##
#Boolean
##

#Can only be True or False. (the capitalization matters)
#This means I AM an employee
is_employee = True 

#this means the iteam is NOT for sale. 
for_sale = False

#You mainly use these for checking conditions
#Use if statements for checking conitions. 

#if for_sale is true, then print out that the car is for sale. 
#other wise we assume the car has been sold. 
if for_sale: 
    print("This care is for sale")
else: 
    print("This car has been sold")
