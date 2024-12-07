age = int(input("Enter your Age: "))

#if satement 1
if(age%2 == 0):
    print("Age is even!")
#end of statement 1

#if statement 2
if(age >=18):
    print("Your age is above 18")
    print("Good for you")
elif(age<0):
    print("You are entering an invalid negative age")
elif(age==0):
    print("You are entering 0 which is not valid age0")
else:
    print("Your age is below 18")
#end of statement 2

print("Program Ended!")

