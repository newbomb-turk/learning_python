#This is a short program that prompts the user for the length and width of a rectangular shape and returns the area. 

#I reccomend you read this code line by line as you run this script. 
#Each comment and line has an explanation and all of this is based off functions seen in Sections 1 - 4. 

#Print out the starting message to let users know the program is running. 
print("Welcome to the Rectangle Area Calculator")

#Obtain the LENGTH from user and store it as an Integer. 
length = int(input("Please enter the LENGTH of your rectangle: "))

#Obtain the WIDTH from user and store it as an Integer. 
width = int(input("Please enter the WIDTH of your rectangle: "))

#BOTH of the above variables are integers. 
#So we can do arithmetic. 
area = length * width

print(f"The AREA of your rectangle is {area}")



#There is one simple way to improve the usefulness of this script.
#Can you figure it out? 

#Check ANSWERS.txt file for solution. 