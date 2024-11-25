#Math (Arithmetic) Operations 

##
#Incrementing a variable 
##

counter = 0

#Normal "long" way to do it
counter = counter + 1

##NOTE - Before moving on, I want to point out spaces do not matter here
#counter=counter+1 works just as fine but I find it much harder to read with spaces.
#Use what is easiest on your eyes! 

#Increment shortcut
counter += 1

#counter=+1 works too! 

##
#Decrement
##

counter = 0

#Normal "long" way to do it
counter = counter - 1

#Using the short cut again. 
counter -= 1


##
#Multiplication
##

#Pretty standard here
total = 2 * 5

#This works too for repeated mulitplication
total *= 2


##
#Division
##

#Also standard looking
golden_ratio = 3 / 2

#Repeated division
golden_ratio /= 2


##
#Modulo Division (Remainder)
##

#Modulo division results in the remiander from dividing two numbers

#You do not typically assign this to the same variable but you could.

#This results in 2
remainder = 8 % 3


##
#Exponents 
##

#This would be 3 to the second power, or 3 squared. 
square = 3 ** 2

#Repeated squaring
#Be careful testing here - you can get a large number fast and crash your IDE here!)
square **= square


###############################
##Built In Arthimetic Functions
###############################

#These are other various useful mathematical functions that come standard with Python

##
#Round function
##

a = 2.6789

#This results in 3
rounded_number = round(a)

#Specify number of decimal places to round to. 

#This results in 2.68
rounded_number = round(a, 2)


##
#Absolute Value - Whole number value "away from 0"
##

#a does NOT equal b
a = -17
b = 17

#But absolute_a equals absolute_b
absolute_a = abs(a)
absolute_b = abs(b)


##
#Power function
##

#Very similar to exponents above. This would be 2 to the 8th power or 256. 
old_school_memory = pow(2, 8)

#which is the same as old_school_memory = 2 ** 8


##
#Max function - finds maximum in a given set of numbers
##

#Results in 237
largest_number = (89, 32, 2, 237)


##
#Min function - finds the minimum in a given set of numbers 
##

#results in 2
smallest_number = min(89, 32, 2, 237)