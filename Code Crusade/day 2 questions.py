# Assignment day 2 - Questions

# Easy

'''Qn1.)Create variables to store your name, age, height, and student status. 
        Print their values and data types?'''

# # Answer:

name = "Piyush"
age = 19
height = 5.9
student_status = True

print("Name:", name, "Type:", type(name))
print("Age:", age, "Type:", type(age)) 
print("Height:", height, "Type:", type(height))
print("Student Status:", student_status, "Type:", type(student_status))



'''Qn2.)Take two numbers as input and print their sum, difference, product,
        and quotient?'''

# Answer:

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Sum:", x + y)
print("Difference:", x - y)
print("Product:", x * y)
print("Quotient:", x / y)




'''Qn3.)Take two numbers as input and use comparison operators to check which number
        is greater and whether they are equal?'''


# Answer:

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("first number is greater:", a > b)
print("second number is greater:", a < b)
print("both numbers are equal:", a == b)



'''Qn4.).Take a number as input and convert it into integer, float, and string
         types. Print the converted values and their data types.'''


 # Answer:   

num = input("Enter a number: ")

int_num = int(num)
float_num = float(num)
str_num = str(num)

print("Integer:", int_num, "Type:", type(int_num))
print("Float:", float_num, "Type:", type(float_num))
print("String:", str_num, "Type:", type(str_num))





# Medium


'''Qn1.)Create a simple calculator that takes two numbers and an operator
       (+, -, *, /) as input and displays the result.'''

 # Answer:

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

operators = {
    '+': a + b,
    '-': a - b,
    '*': a * b,
    '/': a / b  
}

print("Result:", operators[operator])

'''Qn2.)Take the values of a, b, and c from the user and calculate:
        (a + b) * c / (a - b)'''

# Answer:

a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
c = float(input("Enter value for c: "))

result = (a + b) * c / (a - b)

print("Result:", result)



# Hard

'''Qn1.)Take marks of five subjects as input and calculate the total marks,
        average, and percentage. Also check whether the percentage is greater
        than or equal to 75%.'''

# Answer:

s1 = float(input("Enter marks of subject1:"))
s2 = float(input("Enter marks of subject2:"))
s3 = float(input("Enter marks of subject3:"))
s4 = float(input("Enter marks of subject4:"))
s5 = float(input("Enter marks of subject5:"))

total = s1 + s2 + s3 + s4 + s5
average = total / 5
percentage = (total / 500) * 100

print("Total Marks:", total)
print("Average:", average)
print("Percentage:", percentage)
print("Percentage >= 75%:", percentage >= 75)

'''Qn2.)Take a, b, and c as input and evaluate:
        (a + b) ** 2 / (c + 1) - a * b'''

# Answer:

a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
c = float(input("Enter value for c: "))

result = (a + b) ** 2 / (c + 1) - a * b

print("Result:", result)
