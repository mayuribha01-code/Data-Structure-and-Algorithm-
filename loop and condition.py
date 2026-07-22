# EASY
# Check if a number is positive or negative.
num= int(input("Enter a no.:"))
if num>0:
    print("Number is: Positive")
elif num<0:
    print("Number is: Negative")
else:
    print("Number is: Zero")

# Check if a number is even or odd.
num= int(input("Enter a no.:"))
if num%2==0:
    print("No.: Even")
else:
    print("No.: Odd")

# Find the greater of two numbers.
num1= int(input("Enter a 1st No.:"))
num2= int(input("Enter a 2nd No.:"))
if num1>num2:
    print("1st No. is greater:",num1)
elif num1<num2:
    print("2nd No. is greater:",num2)  
else:
    print("Both No. are Equal")  

# Print numbers from 1 to 10 using a for loop.
for i in range (1,11):
    print(i)
    
# Print numbers from 10 to 1 using a while loop.
for i in range (10,0,-1):
    print(i)

# MEDIUM
# Print the multiplication table of a number.
num= int(input("Enter a No. for multiplication table:"))
for i in range (1,11):
    print(f"{num}*{i} = {num*i}")


# Find the sum of numbers from 1 to n.
n= int(input("Enter a No.:"))
total=0
for i in range (1, n+1):
    total+=i
print(total)

# Print all even numbers from 1 to 100.
for i in range (1,101):
    if i%2==0:
        print(i)

for i in range (2,101,2):
    print(i)

# Print all odd numbers from 1 to 100.
for i in range (1,101):
    if i%2!=0:
        print(i)

for i in range (1,101,2):
    print(i)

# Count how many vowels are in a string.
vowel=['a','e','i','o','u']
count=0
name=input("Enter a string:")
for i in name:
    if i in vowel:
        count+=1
print(count)

# HARD
# Check whether a year is a leap year.
year= int(input("Enter a year:"))
if year%4==0:
    print("Leap year")
else:
    print("Not a Leap year")

# Find the factorial of a number.
n= int(input("Enter a no.:"))
fac=1
for i in range (1,n+1):
    fac*=i
print("Factorial:",fac)

# Print a right triangle using *:
# *
# **
# ***
# ****
# *****
for i in range (1,6):
    print("*"*i)

# Reverse a string using a loop (don't use [::-1]).
name="Mayuri"
name=list(str)
rev=[]
for i in range (len(name)-1,-1,-1):
    rev.append(name[i])
rev=str(rev)
print(rev)

# Guess a secret number using a while loop until the user enters the correct value.
n= int(input("Enyter a secret code:"))
num=None
while num!=n:
    num=int(input("Enter a guessing no."))
print("Congratulations")

# CHALLENGE
# Create a Student Result System:
# Take the student's name.
# Take marks (0–100).
# If marks ≥ 90 → Grade A
# If marks ≥ 75 → Grade B
# If marks ≥ 60 → Grade C
# If marks ≥ 40 → Grade D
# Otherwise → Fail
# Then print:
# ===== RESULT =====
# Name  : Mayuri
# Marks : 82
# Grade : B
# Status: PASS
# ==================

name=input("Enter Student name:")
marks=int(input("Enter marks:"))
if marks>=90:
    grade='A'
elif marks <90 and marks>=75:
    grade='B'
elif marks <75 and marks >=60:
    grade='C'
elif marks<60 and marks>=40:
    grade='D'
else:
    grade="Fail"

print("======RESULT======")
print("Name:",name)
print("Marks:", marks)
print("Grade:",grade)
if (marks>=40):
    print("Status: PASS")
else:
    print("Status:FAIL")