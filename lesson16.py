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

# ## N179 ???????????????????????
# def Kvadr_koren(n,guess = 1):
#     if n - guess*guess < 10**(-12):
#         return guess
#     else:
#          return Kvadr_koren(n,(guess + n / guess) * 0.5)
# print(Kvadr_koren(int(input("Enter number:  "))))  
##.........................................

## N 180 ??????????????????????????
# def Red_rasstojanie(s,t):
#     if len(s) == 0:
#         return len(t)
#     elif len(t) == 0:
#         return len(s)
#     else:
#         cost = 0
#         if s[len(s)-1] != t[len(t)-1]:
#             cost = 1
#             d1 = Red_rasstojanie(s[0:len(s)-1],t) + 1
#             d2 = Red_rasstojanie(s,t[0:len(t)-1]) + 1 
#             d3 = Red_rasstojanie(s[0:len(s)-1],t[0:len(t)-1]) + cost
#             return min(d1,d2,d3)
# text1 = input("Text1  ")
# text2 = input("Text2  ")
# print(Red_rasstojanie(text1,text2))
# # print(Red_rasstojanie(input("Enter text1   "),input("Enter text2   ")))


#.........................................

## N 181?????????????????????????

# def razmen(summa,moneti):
#     m = ("25","10","5","1")
#     k = m[0]
#     d = summa // k
#     if d > moneti:
#         print("Net")
#     else:
#         summa = summa % k
#         moneti = moneti - d
#         razmen (summa,moneti,k)



