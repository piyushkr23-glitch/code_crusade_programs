# #Create a string variable to store your name and print the string along with its length.

# name = "Piyush"
# print("Name:",name)
# print("Length:",len(name))

# #.Take a string as input and print the first character, last character, and middle character using indexing.

# # a = input("Enter your string:")

# # print(a[0])
# # print(a[-1])
# # print(a[len(a)//2])

# a = input("Enter your string:")

# print(a[:3])
# print(a[-3:])


# s1 = input("Enter first string:")
# s2 = input("Enter second string:")
# result = s1 + s2
# print(result)

# s = input("Enter your string:")
# print(len(s))
# print(s.upper())
# print(s.lower())

# a = input("Enter your string:")

# print(a[::-1])

# s1 = input("Enter a sentence:")
# words = s1.split()
# print(len(words))
# print(s1.upper())
# print(s1.lower())
# print(s1.replace(" ","-"))

s = input ("Enter your string:")
if s == s[::-1]:
    print("Palindrome")

else:
    print("not Palindrom")





