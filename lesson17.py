# ## Calkulator
# try:
#     #print("X + " , x = int(input(" Enter x : ")), "\ny =  ", y = int(input("Enter y:  ")), x + y )
#     x = int(input("Enter X:  "))
#     y = int(input("Enter Y:  "))
#     char = input("Enter dejstvie: ")
#     if char == "+":
#         rez = x + y
#     elif char == "-":
#         rez = x - y
#     elif char == "/":
#         rez = x / y
#     elif char == "*":
#         rez = x * y
#     else:
#         rez = "Neizvestnoe dejstvie"      
#     print(x , char, y,  " = " , rez)
# except ZeroDivisionError:
#     print(" nelzja delit' na 0")
# except  KeyboardInterrupt:
#     print("ne ispolsujte ctr + V")
# except ValueError: 
#     print("Vvedite chislo")
# ##.........................................

# ## Password Generator
# try:
#     n = input("Enter password of 8 characters:  ")
#     if len(n) != 8:
#         raise ValueError("Enter  8 characters, please!")
#     elif n[0].isdigit():
#         raise ValueError("Password does not start with number!" )
#     elif not n.isalnum():
#         raise ValueError("Password does not contain spaces or other charakters!" )
#     else:
#         print("Good!")
# except Exception as e:
#     print(e)
# ##...................................



##... ..........
import random

# ### ......................
# l = random.randint(7,11)
# print(l)
# pas = ""
# for i in range(1,l+1):
#     k = chr(random.randint(33, 126))
#     pas += k

# print(pas)
# ##...................................

with open("Doc1.txt", "rt") as f:
    res = f.readlines()
    print(res[:4]) 
with open("Doc1.txt", "a") as f:
    f.write("I Love you!")

with open("Doc1.txt", "rt") as f:
    res = f.readlines()
    res.sort(key = len)
    print(res[-1])

## N152

# oldfile = input("Enter file name: ")
# newfile = input("Enter new file name: " )
# with open("oldfile.txt", "rt") as a:
#     num. = 1
#     rez = a.readline()



