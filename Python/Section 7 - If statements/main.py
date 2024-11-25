#If statements look pretty similar to any other language except you do not need brackets nor parenthese.
#This is great sometimes, confusing other times. I reccomend still using () or [] for readability but not required. 

#Very simply cash register program here using if statements
#Lets decided quanitity or weight to get final price of an item

#We punch the price and weight in. If the weight is 0 then it is an invaild item to check out. 

#Price is typically in decimals, so I am choosing to use float type variable here. 
price = float(input("Enter the price of the item: "))

#Now we can ask a question, intutively. 

quantity = input("Enter the amount or weight of product: ")

#IF the response is a whole number, it is quantity. 

#Otherwise, if the response is a float, we can assume it is weight. (i.e. you cannot be buying 1.31234567876543 apples...)

#So lets test what variable type our response is. 
multiplier = type(quantity)

#The only thing about an if statement in Python is that you MUST follow it with a colon :

if (multiplier = float) :
    #We see decimals, so we assume it is weight. 
    print("weighjt")
    total_price = price * quantity
elif (multiplier = int) :
    print("quantity")
    #no decimals so we assume quantity.
    total_price = price * quantity
else : 
    print("Invalid input!")

#We do NOT have to denote the end of loops in Python like we would shell scripts or other languages. 

#Print out the price
print(f"Total price is: {total_price}")

#Lets take a break; read and review.
#
#
#
#
#
##
#This is not the best exmaple because it always results in a float output.
#But you should notice within the code the basic if statement structure.
#
#The next section has previous commands embedded in if statements. 
#
##
#PLEASE - famliiarze yourself and ensure you feel comfortable with the code in the previous 7 sections before moving on!
##
#
#
#
#Thanks for reading!
#
#Can you hear a pterodactyl go to the restroom? 













#No, because their P is silent. 