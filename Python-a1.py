print("Hello World")

# Declaring variables 
name = "Hamid Butt"
age = 21
isStudent = False
print(name,age, isStudent)

# Taking input from user
un = input("Enter username:")
print("Username is: " + un)

# Type conversions in Python
age = input("Enter your age ? ")
new_age = int(age) + 2
print(new_age)
first = input("Enter 1st number: ")
second = input("Enter 2nd number: ")

sum = int(first) + int(second)
print("The sum of 2 numbers is: " + str(sum))

# IF-ELSE Statement 

age = 16  
if age>18:
     print("You are an adult") 
elif age>18 and age <30:
     print("You are in University")

# MINI Project Calculator using If-else

first = input("Enter 1st number : ")
operator = input("Select an operator +,-,*,/,% : ")
second = input("Enter 2nd number : ")

first = int(first)
second = int(second)

if operator == "+":
     print(first + second)
elif operator == "-":
     print(first - second)
elif operator == "*":
     print(first * second)
elif operator == "/":
     print(first / second)
elif operator == "%":
    print(first % second)
else:
     print("Invalid operator")

# While Loop

i = 1
while i < 6:
  print(i * "*")
i = i + 1

# Reverse the pattern using while loop
i = 6
while i >= 1:
   print(i * "*")
i = i - 1

# For loop

for i in range(5):
    print(i)

# List Data Type in Python
marks = [10,20,30,40]
print(marks)

# Break and Continue
students = ["Hamid", "Butt"]
for student in students:
     if student == "Hamid":
         break
     print(student)
for student in students:
    if student == "Butt":
        continue
    print(student)

# Dictionary

marks = {"TOA" : 90, "COAL" : 70}
print(marks["STATS"])
marks["DSA"] = 84
print(marks)

# Functions
def sum(first, second):
     print(first + second)
sum(1,7)