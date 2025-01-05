# Write a program to mine a log file and find out whether it contains 'python'.


# with open("logs.txt") as f:
#     data = f.read()

# if("python" in data):
#     print("PYTHON Present in logs")
# else:
#      print("PYTHON Not Present in logs")


# PYTHON EXIT AT LINE NUMBER


with open("logs.txt") as f:
    lines = f.readlines()

lineNo = 1
for line in lines:
    if("python" in line):
        print(f"PYTHON Present in logs at Line# {lineNo}")
        break
    lineNo +=1

else:
        print("PYTHON Not Present in logs")

