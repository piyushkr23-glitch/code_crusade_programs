# Qn1.)Take a number as input and check whether it is positive, negative, or zero using conditional statements.


num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#Q2.Take a number as input and check whether it is even or odd using an if-else statement.
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")



# Q3.) Take a person's age as input and check whether they are eligible to vote or not.

age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
   print("Not eligible to vote")



#Q4.)Take two numbers as input and print the greater number using an if-else statement.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("Greater number is:", num1)
else:
    print("Greater number is:", num2)



# Q5.)Take marks as input and display the grade using if-elif-else: A, B, C, D, or F based on the marks.

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")



#Q6.)Take a username and password as input. 
# Use conditional statements to check whether the login details are correct and display an appropriate message.

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")

#Hard

# Q1.Take a student's marks in three subjects as input.
#   Calculate the percentage and display the grade only if the student has passed all three subjects; otherwise, display "Fail".


marks1 = float(input("Enter marks in subject1: "))
marks2 = float(input("Enter marks in subject2: "))
marks3 = float(input("Enter marks in subject3: "))



if marks1 >= 33 and marks2 >= 33 and marks3 >= 33:
   percentage = (marks1 + marks2 + marks3)/3
   print("Percentage:", percentage)


if percentage >= 90:
 print("Grade A")

elif percentage >= 75:
    print("Grade B")
elif percentage >= 60:
       print("Grade C")
elif percentage >= 33:
      print("Grade D")

else:
   print("Fail")

#Q2.)Create a simple electricity bill calculator using nested if statements. 
# Take the number of units as input and calculate the bill according to different unit ranges.

units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 5
else:
    if units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)
    else:
        if units <= 300:
            bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
        else:
            bill = (100 * 5) + (100 * 7) + (100 * 10) + ((units - 300) * 12)

print("Electricity Bill =", bill)