# ## Exercise 1
# def list_of_elements(start,stop,step):
#     lst = []
#     for i in range(start,stop,step):
#         lst.append(i)
#     return(lst)

# a = int(input("Enter start: -->"))
# b = int(input("Enter stop: -->"))
# c = int(input("Enter step: -->"))
# print(list_of_elements(a,b,c))
# ## ..............................

# ## Exercise 2
# def neighbours_products(lst1):
#     lst2 =[]
#     for i in range(0,len(lst1) -1):
#         lst2.append(int(lst1[i]) * int(lst1[i+1]))
#     return(lst2)
# list1 = [1,4,6,3,8,5, 23, 45, 67 ]
#print(neighbours_products(list1))
# ##..............................

# ## Exercise 3

# sent = "_, we have a _ !"
# word = ["Ashot","problem"]
# for i in word:
#     sent = sent.replace("_", i, 1)
# print(sent)
# ##....................................

# ## Exercise 4
# list_string = ["asdfg","as","asdfghjk","qwer","asd", "a", "asdfghjk"]
# max1 = list_string[0]
# min1 = list_string[0]
# for i in range(1,len(list_string)):
#     if len(max1) < len(list_string[i]):
        
#         max1 = list_string[i]
#     else:
#         if len(min1) > len(list_string[i]):
#             min1 = list_string[i]
# print(min1,"\n",max1,"\n",len(min1) + len(max1))
# ##........................

## Exercise 5
# try:
#     list_of_number =[23,54,76,45,12,34,98,78,-56,34,-61,-34,98,-98, 8]
#     list_of_number.sort()
#     print(list_of_number)
#     def ind(l,first,last,n):
#         midl = (first+last)//2
#         if l[midl] == n:
#             return midl
#         elif n < l[midl]:
#             return ind(l,first,midl - 1,n)
#         else:
#             return ind(l,midl+1,last,n )
#     f = 0
#     l = len(list_of_number)
#     k = int(input("Enter number:-->"))

#     rez = ind(list_of_number,f,l,k)
# except RecursionError:
#     rez = ind(list_of_number,f,l,k+1)
# print(rez) 
## .............................................

# ##  Exercise 6
# def mydict(n):
#     dict1 ={}
#     for i in range(1,n+1):
#         dict1[i] = i * i
#     return dict1
# print(mydict(int(input("Enter N --> ")))) 
## ..........................

#  ##  Exercise 7
# olddict = {
#     1 : "a",
#     2 : "b", 
#     3 : "d",
#     4 : "b"
# }
# newdict = {}
# list1 = []
# list2 = []
# for i in olddict.values():
#     list1.append(i)
# print(list1)
# for i in olddict:
#     list2.append(i)
# print(list2)
# for i , j in zip(list1,list2):
#     newdict[i] = j
# print(newdict)
## ......................................


## Exercise 8
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return fib(n - 1) + fib(n - 2)
list1 = []
for i in range(0,int(input("Enterb naumber:-- >"))+1):
    list1.append(fib(i))
print(list1)
# ##.............................   
