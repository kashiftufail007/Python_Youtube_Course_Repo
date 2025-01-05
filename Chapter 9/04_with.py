f = open("file.txt")
print(f.read())

f.close()

# Same can be done with "with" statement 


with open("file.txt") as f:
    print(f.read())