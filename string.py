# # \n : Next line 
# # \t : Tab spacing
# # \\ : Backslash
# # \" : Adding quote in quoted statement

# print("Hello everyone, My name Mayuri \nHow are you?")
# print('Mayuri:\t20')
# print("new\\old")
# print('Mayuri\'s phone')
# print("Hey!! \"Mayuri\"")

# Membership Operations

s="Python is a Computer Language."
print("Java" in s)
print("python" in s)
print("Python" in s)
print("Java" not in s)

# Replace
print(s.replace("Python","Java"))
print(s.replace('a',"A"))
print(s.replace('a',"A",1))
print(s.replace('a',"A",2))

# Strip
s="Python "
s1= s.strip()
print(s1=="Python")