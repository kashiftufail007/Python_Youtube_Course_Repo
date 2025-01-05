# A file contains a word "Donkey" multiple times. You need to write a program which
# replace this word with ##### by updating the same file.
# Repeat program 4 for a list of such words to be censored.

words = ["Donkey" , "bad" , "Whimsyville"]

with open("donkey.txt" , "r") as f:
    # print(f.read())
    content = f.read()
for word in words:
    content = content.replace(word , "#"*len(word))

with open("donkey.txt", "w") as f:
    f.write(content)