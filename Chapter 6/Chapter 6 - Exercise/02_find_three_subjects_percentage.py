#find percentage of 3 subjects

subject1 = int(input("Enter first subject marks: "))
subject2 = int(input("Enter second subject marks: "))
subject3 = int(input("Enter third subject marks: "))

total_marks = int(input("Enter total subjects marks: "))

percentage = (((subject1+subject2+subject3) / (total_marks*3))*100)

print(f"Total Percentage marks are: {percentage}")

if(percentage >=40 and subject1 <33 and subject2<33 and subject3<33):
    print(f"You are pass with percentage of: {percentage}")
else:
     print(f"You are fail with percentage of: {percentage}")
