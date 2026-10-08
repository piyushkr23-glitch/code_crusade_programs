#1.Write a program using a for loop to print the numbers from 1 to 10.
# for i in range(1,10):
#     print(i)


# #2.Write a program using a while loop to print the numbers from 1 to 10.
# i=1
# while i <= 10:
#     print(i)
#     i+=1

# #3.Take a number as input and print its multiplication table from 1 to 10 using a for loop. 
# n = int(input("Enter number:"))
# for i in range(1,10):
#     print(n*i)

# #4.Write a program to calculate and print the sum of numbers from 1 to 100 using a loop.
# sum =0
# for i in range(1,100):
#     sum += i

# print(sum)    

#1.Take a number as input and calculate its factorial using a while loop.

# n = int(input("Enter number:"))
# factorial = 1
# i = 1
# while i <= n:
#     factorial = factorial*i
#     i += 1
# print(factorial)    

 #2.Take a number as input and count the number of digits in it using a while loop.
# n = int(input("Enter number:"))

# count = 0

# while n>0:
#     n = n//10
#     count += 1

# print(count)

#Take a number as input and reverse the number using a while loop. For example, 12345 → 54321.

# num = int(input("Enter number:"))

# reverse = 0

# while num > 0:
#     s = num % 10
#     reverse = reverse*10 + s
#     num//=10

# print(reverse)
    

#2.Take a number as input and check whether it is a prime number using a loop.




















# num = int(input("Enter number:"))
# prime = True
# if num <= 1:
#     prime = False


# for i in range(2,num):
#     if num%i == 0:
#         prime = False
        

# print("Prime: ",prime)



#Questions 55

#1.)for i in range(1, 101):    
 #   print(i)

#2.)
# for i in range(100, 0, -1):   
#      print(i)

#3.)
# for i in range(2, 101, 2):    
#     print(i)

#4.)
# for i in range(1, 101, 2):  
#       print(i)

#5.)
# for i in range(5, 101, 5):   
#      print(i)
            
#6.)
# n = int(input("Enter number: ")) 
# for i in range(1, 11):  
#   print(n * i)

#7.)
# n = int(input("Enter n: "))
# total = 0 
# for i in range(1, n + 1):  
#       total += i
# print(total)

#8.)
# n = int(input("Enter n: ")) 
# product = 1 
# for i in range(1, n + 1):  
#       product *= i 
# print(product)

#9.)
# n = int(input("Enter n: "))
# total = 0 
# for i in range(2, n + 1, 2):   
#      total += i 
# print(total)

#10.)
# n = int(input("Enter n: ")) 
# total = 0 
# for i in range(2, n + 1, 2):    
#     total += i 
#     print(total)

#11.) 
# num = int(input("Enter your number:"))

# if num%2 == 0:
#     print("Even number")
# else:
#     print("odd number")


# original = num
# reverse = 0

# while num>0:
#     digit = num%10
#     reverse = reverse*10 + digit
#     num //= 10

# if original == reverse:
#     print("Panlindrome")
# else:
#     print("Not Panlindrome")

# if

