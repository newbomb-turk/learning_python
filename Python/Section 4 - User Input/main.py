#User input makes programs more dynamic by allowing human to program or program to program interation. 
#Here we will just be focusing on human to program interactions using the input() function. 

##
#Using the input() function
##

#This is going to expect you to type something in. It WILL NOT ASK YOU to type anything in. 
input()
#Press enter

#To make this more useful, we can ask a question: 
input("What is your favorite movie? : ")
#You can answer the question. 

#or you can just hit enter because while we are asking a question it - we do not remember it. 

#This is something in which I think Python excels in as you can remember things from users all in a simple line. 
#So let's remember for your favorite movie. 

favorite_movie = input("What is your favorite movie? : ")

#And now we can use the information we remembered
#This should print what your favorite movie is...or whatever you entered. (:
print(f"Your favorite movie is {favorite_movie}!")

#Something to note at this point however - input() ALWAYS returns a string type. 
#This is where typecasting (Section 3) comes in handy. 
#And back to line 18 - python excels here as you can define all of this in one easy to read line. 

favorite_number = int(input("What is your favorite number? : "))

#Now we can add twelve to your favorite number. Since it is an int, we can do arithmetic. 
favorite_number = favorite_number + 12

#And print it all out
print(f"Your favorite number + 12 is {favorite_number}")

#If you run this program too fast, and I hope some do - you will probably get it to fail. 
#Notice once you have the typecasting int() function in the input...you MUST type in an Integer. 

#Strings will fail and even floats will fail. 