#find greatest of 4 numbers entered by user.

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
d = int(input("Enter 4th number: "))

if(a >= b and a>=c and a>=d):
    print("Greater number is: ", a)
elif(b >= a and b>=c and b>=d):
    print("Greater number is: ",b)
elif(c >= a and c>=b and c>=d):
    print("Greater number is: ", c)
else:
    print("Greater number is: ", d)


