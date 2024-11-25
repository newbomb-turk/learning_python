#Typcasting - Converting one type of variable to another. 
#There is auto typcasting and manual.

#Realistically, each data type, has its own convert function. This seciton covers all 4 and some caveats. 

##
#These below variables sort of describe an item for sale on the shelf.
#You will see this a few times after type casting. 
##

item_name = "Potato Chips"
UPC = 1234567
price = 3.99
is_sold = False

##
#To print out the TYPE of a variable
##

#This should print out class <str>
print(type(item_name))


##
#Convert float to Integer. The int() function
##

price = int(price)

#This should print 3. NOTE - There is not rounding. It just simply truncates the decimal portion. 
print(price)


##
#Convert Integer to float. The float() function
##

UPC = float(UPC)

#This should print 1234567.0
print(UPC)


##
#Resetting variables again
##

item_name = "Potato Chips"
UPC = int(UPC)
price = 3.99
is_sold = False

##
#Converting Integer to string. The str() function
##

#This should print 1234567
print(UPC)

#This should print class <int>
print(type(UPC))

#Convert it to a string
UPC = str(UPC)

#This will print 1234567. 
print(UPC)

#Yes, it's confusing becuase you see no change until you print the type.
#This should print class <str>
print(type(UPC))

#Once you move to a string, you lose the ability to do arithmetics on the variable.


##
#Converting a string to a boolean. The bool() function.
##

item_name = bool(item_name)

#This should print out true
print(item_name)

#And it prints out true only because the string was not empty. 
#This is great for checking for check if strings are empty and in particular, user input. 