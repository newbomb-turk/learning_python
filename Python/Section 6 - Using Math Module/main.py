#Python Module - Think of it like an add on set of functions you can choose to use in your scripts.

##
#Importing a Module
##

#simply use import
#It is normal to do this it at the very beginning of your script

#Import the math module - This is a built in module included with the standard Python download. 
import math

#How to use things in a module
#Reference the module name first then a dot then the variable or function within the module you wish to use. 

#Incase you need the logrithmic e constant...
#Prints out 2.718281828459045
print(math.e)

#Note that we have the math module dot e (the constant)

##
#Square Root
##

#Results in 5
root = math.sqrt(25)


##
#Ceiling - Forces a float to be rounded up
##

#This results in 9. 
whole_number = math.ceil(8.01)

#It is essentially a way to check if a number is over a certain threshold.
#Or force it to be. 


##
#Floor - Opposite of ceiling. Forces numbers to be rounded down. 
##

#This results in 8. 
whole_number = math.floor(8.01) 