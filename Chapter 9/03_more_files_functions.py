f = open("myfilewrite.txt")

# lines = f.readlines()
# print(lines , type(lines))
#  For single line
# line1 = f.readline() 
# print(line1 , type(line1))
# line2 = f.readline() 
# print(line2 , type(line1))


line = f.readline()
while(line!= ""):
    print(line)
    line = f.readline()


f.close()