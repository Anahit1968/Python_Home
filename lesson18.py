# with open("Doc1.txt", "rt") as f:
#     res = f.readlines()
#     print(res[:4]) 
# with open("Doc1.txt", "a") as f:
#     f.write("I Love you!")

# with open("Doc1.txt", "rt") as f:
#     res = f.readlines()
#     res.sort(key = len)
#     print(res[-1])

## N152

# oldfile = input("Enter file name: ")
# newfile = input("Enter new file name: " )
# with open(oldfile, "rt") as a:
#     num = 1
#     rez = a.readline()
#     while rez != "":
#         with open(newfile, "a") as b:
#             b.write(str(num) + ":" + rez) 
#             num += 1
#             rez = a.readline()
##..................................................

# with open("Doc2.txt", "rt") as text:
#     rez = "a"
#     s = 0
#     while rez != "":
#         rez = text.readline()
#         for i in rez:
#             if i.isdigit():
#                 s += int(i)
# print(s) 




