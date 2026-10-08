# # # # print(-12)
# # # # print(abs(-12))
# # # # print(pow(2, 3))
# # # # print(round(3.14159, 2))
# # # # print(sum([1, 2, 3, 4, 5]))

# # # # name = "Piyush"
# # # # full_name = "Piyush Kumar"
# # # # print(len(name))
# # # # print(len(full_name))

# # # a =  "Hello World"
# # # original = a
# # # a = a[::1]
# # # if(original == a): 
# # #  print("Palindrome")

# # a = "abcdefghij"
# # print(a[-3:5:1])

# name = "Alok kumar"
# age = 19
# print("My name is    ", name, "and I am", age, "years old.")
# print(f"My name is     {name} and I am {age} years old.")

# s = "banana" 

# print(s[-1]+s[1:5]+s[0])


# s = "computerscience"
# print(s[8:15])
# n = "programming"
# n = n[::-1]
# print(n[:3:1])
# first_name = input("Enter your first name : ")
# last_name = input("Enter your last name : ")
# city = input("Enter your city : ")
# print("My name is" , first_name ," " , last_name , " and I live in Udit" , " " ,city)
# word = "Udit"
# print((word + "|" ) * 3)

# name = "Python Programming"
# print(name[0])#string indexing
# print(name[5]) #Positive indexing
# print(name[-1]) #Negative indexing  
# print(name[0:8]) #String slicing


# Concatenation and Repetition


first_name = "Piyush"
last_name = "Kumar"
full_name = (first_name + " " + last_name)#cocatenation

print(full_name)


word = "Python"
print(word * 3) #Repetition


#Formatting Strings
name = "Piyush"
age = 19
print(f"My name is {name} and I am {age} years old.") #f-string formatting


#Numbers methods
print(abs(-12)) #absolute value
print(pow(2, 3)) #power
print(round(3.14159, 2)) #rounding
print(sum([1, 2, 3, 4, 5])) #sum of list

name = "Piyush"
print(len(name)) #length of string

print(name.upper()) #convert to uppercase
print(name.lower()) #convert to lowercase   
print(name.capitalize()) #capitalize first letter
print(name.replace("Piyush", "Alok")) #replace substring
print(name.title()) #title case


s = "Hello World"
print(s.split()) #split string into list

print(" ".join(["Hello", "World"])) #join list into string

#Trimming whitespace
s = "   Hello World   "
print(s.strip()) #remove leading and trailing whitespace
print(s.lstrip()) #remove leading whitespace
print(s.rstrip()) #remove trailing whitespace
print(s.find("W")) #find substring
print(s.index("o"))

