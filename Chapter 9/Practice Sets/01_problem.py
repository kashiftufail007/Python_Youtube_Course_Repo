#  Read from a poem.txt and check either it have Twinkle word or not
# Write a program to read the text from a given file 'poems.txt' and find out whether it
# contains the word 'twinkle'.

f = open("poem.txt")

data = f.read()

if("twinkle" in data):
    print("Twinkle Present")
else:
     print("Twinkle Not Present")
print(data)
f.close()