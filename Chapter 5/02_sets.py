e = set() #will be a empty sets
e = {}  # Empty dictionary 

# s = {1,2,3,4,5,4,3,4} 

# print(s)  # {1, 2, 3, 4, 5} // remove repatitation


# s = {1, 2, 3, 4, 5, 4, 3, 4, "Kashif"}  # No leading spaces
# s.add(22)  # Proper indentation
# print(s, type(s))  # Proper indentation


# s1 = {1, 2, 3, 4, 5, 4, 3}
# s2 = {1, 4, 3, 8, 6, 7, 3}

# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.issubset(s2))

s = set()
s.add(20)
s.add(20.0)
s.add("20")

print(len(s))   #2  -- due to 20 and 20.0 are single value in sets
