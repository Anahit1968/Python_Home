# ## N173
# def sum_znach():
#     n = input("Enter number ")
#     if n == "":
#         return 0
#     else: 
#         return float(n) + sum_znach()
# Summa = sum_znach()
# print("summa = " , Summa)
##..........................................

## N174
# def NOD(a,b):
#     if b == 0:
#         return a
#     else:
#         c = a % b
#     return NOD(b,c)
# print(NOD(int(input("Enter a: ")), int(input(("Enter b: "))))) 
# #................................

# ## 175 ???????????
# def perevod(dec,s = ""):
#     if dec == 0:
#         k = "0"
#         s = s + k
#         return (s)
#     elif dec == 1:
#         k = "1"
#         s = s + k
#         return(s)   
#     else:
#         k = str(dec % 2)
#         s = s + k
#         p = s
#         dec = dec//2
#         perevod(dec, s)   
#     return(p) 
# Chislo = int(input("enter number"))
# if Chislo < 0:
#     print("Oshibka") 
# else:
#     print(perevod(Chislo, s = ""))
#..........................................
## N176
# def func_NATO(**x):
#     slovo = str(input('Enter slovo-->'))
#     for i in slovo:
#         for j in x:
#             if i in x[j]:
#                 print(j)
# func_NATO(Alpha = 'A', Bravo = 'B', Charlie = 'C',  Delta = 'D', Echo = 'E')
##.......................................


# ## N178
# def polindrom(text):
#     if len(text) == 0:
#         return True
#     elif len(text) == 1:
#         return True
#     else:
#         if text[0] == text[-1]:
#             text = text[1:-1]
#             #print(text)
#             return polindrom(text)
#         else:
#             return False
# print(polindrom(input("Enter text:  ")))
##......................................

# ## N179 
# def Kvadr_koren(n,guess = 1):
#     if abs(n - guess*guess) < 10**(-12):
#         return guess
#     else:
#          return Kvadr_koren(n,(guess + n / guess) * 0.5)
# print(Kvadr_koren(int(input("Enter number:  "))))  
##.........................................

## N 180 
# def Red_rasstojanie(s,t):
#     if len(s) == 0:
#         return len(t)
#     elif len(t) == 0:
#         return len(s)
#     else:
#         cost = 0
#         if s[len(s)-1] != t[len(t)-1]:
#             cost = 1
#         d1 = Red_rasstojanie(s[0:len(s)-1],t) + 1
#         d2 = Red_rasstojanie(s,t[0:len(t)-1]) + 1 
#         d3 = Red_rasstojanie(s[0:len(s)-1],t[0:len(t)-1]) + cost
#         return min(d1,d2,d3)
# text1 = input("Text1  ")
# text2 = input("Text2  ")
# print(Red_rasstojanie(text1,text2))
# # print(Red_rasstojanie(input("Enter text1   "),input("Enter text2   ")))
#.........................................

## N 181??
# def Razmen(gumar,qanak):
#     l = ("25","10","5","1")
#     for k in l:
#         if gumar // int(k) > qanak:
#             return ("No")
    
#         elif gumar // int(k) == qanak and gumar % int(k) == 0:
#             return ("yes")
#         else:
#             gumar = gumar % int(k)
#             qanak = qanak - gumar // int(k)

# print(Razmen(int(input("Enter gumar:  ")),int(input("Enter qanak:  "))))   
##......................

## N 186

# def dekod(Spisok):
#     spisok1 = []
#     for i in range(0,len(Spisok),2):
#         spisok1.append(Spisok[i]*Spisok[i+1])
#     for i in spisok1:
#         i.split()
            
#     return(spisok1)
# print(dekod(["a", 4,"b",7,"c", 3]))
##........................................

## N185
#def func(n, s = ''):
#     if n == 1:
#         return (s + '1')[::-1]
#     elif n == 0:
#         return (s + '0')[::-1]#     else:
#         return func(n // 2, s + str(n % 2))
# print(func(int(input('Enter number-->'))))  
# 
#   
# --------------------------------

## N 183
import mendeleev as m

l = m.elements.get_all_elements()
mydict = {}
for i in l:
    mydict[i.symbol.lower()] = i.name.lower()
def func(text, s=''):
    global mydict
    if text == '':
        return s
    if text[0:2] in mydict.keys():
        return func(text[2:], s + mydict[text[0:2]] + ' ')
    else:
        if text[0] in mydict.keys():
            return func(text[1:], s + mydict[text[0]] + ' ')
def func_new(text, s=''):
    global mydict
    if text == '':
        return s
    if text[0] in mydict.keys():
        return func(text[1:], s + mydict[text[0]] + ' ')
    else:
        if text[0:2] in mydict.keys():
            return func(text[2:], s + mydict[text[0:2]] + ' ')
myset = set()
for i in mydict:
    if func_new(mydict[i]) != None:
        print(func_new(i))
        myset.add(mydict[i])
    if func(mydict[i]) != None:
        print(func_new(i))
        myset.add(mydict[i])
    if func_new(mydict[i][::-1]) != None:
        print(func_new(i))
        myset.add(mydict[i])
    if func(mydict[i][::-1]) != None:
        print(func_new(i))
        myset.add(mydict[i])
print(myset, len(myset))
##----------------------------------------------
# N 184
#def flatten(a:any, mylist:list[any]) -> list[any]:
#     if a == []:
#         return mylist
#     else:
#         if not isinstance(a[0], list):
#             mylist.append(a[0])
#             a.remove(a[0])
#             return flatten(a, mylist)
#         else:
#             mylist.extend(flatten(a[0], []))
#             a.remove(a[0])
#             return flatten(a, mylist)
# print(flatten([1, [2, 3], [4, [5, [6, 7]]], [[[8],9], [10]]], []))
# -----------------------