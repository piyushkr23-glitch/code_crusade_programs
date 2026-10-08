#Left-Aligned Increasing Number Triangle.
#Qn.)Prime numbers from 1 to the current row number, increasing the number of values in every row.
# n = 5 
# for i in range(1, n + 1): 
#        for j in range(1, i + 1):       
#          print(j, end=" ")   
#        print()

#Left-Aligned Repeated Number Triangle
#Print the row number repeatedly across each row.
# n = 5
# for i in range(1,n+1):
#     for j in range(i):
#         print(i, end=" ")
#     print()

#Inverted Left-Aligned Number Triangle
#Print numbers from 1 to n, but decreases the number of values in every next now.

# n = 5
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()

#Floyd's Triangle
#Print Consecutive numbers continuosly across rows, with row 1 containing 1 value, row 2 containing 2 values, and so on.
# n = 5
# num = 1

# for i in range(1,n+1):
#     for j in range(i):
#         print(num , end=" ")
#         num += 1
#     print()


# Solid Square
# Print a solid square containing n rows and n stars in every row.
# n = 5
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
        
#     print()    

#Hollow Sphere
#Print a square where only the boundary contains starts and tbe inside remains empty.
# n = 5
# for i in range(n):
#     for j in range(n):
#          if i == 0 or i == n-1 or j == 0 or j == n-1:
#             print("*",end=" ")
#          else:
#             print(" ", end = " ")
#     print()

# n = 5
# for i in range(1,n+1):
#     print("  "*(n-i) + "* " * i )

# for i in range(1,100):
#     if(i==98):
#         continue
#     print(i)


# print(bool(""))

# for i in range(1,16):
#     if(i==8):
#         pass
#     print(i)


# for i in range(1,6):
#     for j in range(i):
#         print("*", end= " ")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end = " ")
#     print()

n = 5
for i in range(1,n+1):
    print("",end="")

for j in range(n-i):
    print("* ",end="")