## N1
def func1(test, count = 0):
    for i in test:
        count += 1
    return count
print(func1(input("Enter text -->"))) 
def calculate(x,y,z):
    if z == '+':
        rez = x + y
    elif z == '-':
        rez = x - y
    elif z == '*':
        rez = x * y
    else:
        rez = x / y
    return(rez)
print(calculate(5,8,'-'))
print(calculate(5,8,'+'))
print(calculate(5,8,'*'))
print(calculate(5,8,'/'))
print(calculate(int(input("Enter x : ")), int(input("Enter y : ")), input("Enter deystvie : ")))
# ............................................


# N 2
def max1(n1,n2):
    if n1 > n2:
        print(n1,',', n2, '--> max = ', n1),
    else:
        print(n1, ',', n2, '--> max = ', n2)
max1(15,64) 
max1(int(input("Enter n1 : ", )), int(input("Enter n2 : "))) 
# ............................................

 #N 3
def sum1(*numbers, rez = 0):
    for i in numbers:
        rez += i
    return(rez)
print(sum1(1,2,3,4,15))
#print(sum1(list(input('Enter numbers -->')))) ???
# ............................................

# N4 
def multipl(*numbers, rez = 1):
    for i in numbers:
        rez *= i
    return(rez)
print(multipl(1,2,3,4,15))
#print(multipl(list(input('Enter numbers -->')))) ???
# ............................................


# N6
def start(age1,age2,age3):
    l = (age1,age2,age3)
    for i in l:
        if i <= 16:
            print("Too young!")
        else:
            print("Get start!")
start(int(input("enter age1:")),int(input("enter age2:")),int(input("enter age3:")))
#.........................................................


# N85
def Gipotenuza(a,b):
    c = (a**2 + b**2) ** (1/2)
    return(c)

#a = int(input("Enter a: "))
#b = int(input("Enter b: "))
#Gipotenuza(input("Enter a: "),input("Enter b: "))
print("Dlina gipotenuzy ravna : ", Gipotenuza(int(input("Enter a: ")),int(input("Enter b: "))))
##.........................................


## N86
# def sumTaxi(baze, pl_stavka, rasstojanie):
#     itog = (rasstojanie / 0.14) * pl_stavka  + baze 
#     return(itog)
# print("Summa k oplate sostavljaet : " , round(sumTaxi(4, 0.25, float(input("Vvedite rasstojanie v kilometrax :"))),2))
 ##...............................................

 ## N87
# def dostavka(chislo_zakaza):
#     if chislo_zakaza == 1:
#         print("summa dostavki = ", 10.95)
#     else:
#         print("summa dostavki = ", 10.95 + (chislo_zakaza - 1) * 2.95)

# dostavka(int(input("Vvedite kolichestvo zakaza: ")))
# #..............................

# ## N 88
# def median(a1,a2,a3):
#     a = (a1,a2,a3)
#     #sorted(a)
#     print((sorted(a))[1])
#     # print(a[])
# median(float(input("Enter a1 : ")), float(input("Enter a2 : ")), float(input("Enter a1 : ")))
# #.........................
# ## N93
# def centr(s,w):
#     if len(s) >= w:
#         print(s)
#     else:
#         b = "   "
#         c = (w - len(s)) // 2
#         print(b * c + s)
# centr((input("Eter word : ")), int(input("Enter shirinu okna:  ")))
# #..............................................

## N94
# def treugolnik(a,b,c):
#     if a <= 0 or b <= 0 or c <= 0:
#         rez = False 
#     elif a <= (b + c) and b <= (a + c) and c <= (a + b):
#         rez = True
#     else:
#         rez = False
#     return(rez)        
# B = treugolnik(int(input("Enter a :")),int(input("Enter b :")),int(input("Enter c :")))
# if B == True:
#     print("Treugolnik mojno postroit'") 
# else:
#     print("Treugolnik ne poluchutsa")


## N95

## N96   
# def precedence(char):
#     if char == "+" or char == "-":
#         print(1)
#     elif char == "*" or char == "/":
#         print(2)
#     elif char == "^":
#         print(3)
#     else:
#         print(-1)
# precedence(input("Enter arifmeticheskij znak:  "))
# #..................

## N98

# def prostoe_chislo(chislo):
#     i = 2
#     while i <= chislo:
#         if chislo % i != 0:
#             i +=1 
#         else:
#             break
#     print(i)
#     if i == chislo:
#         print(chislo , " --> prostoe chislo ")
#     else:
#         print(chislo , " --> ne prostoe chislo! ")
# prostoe_chislo(int(input("Enter chislo --> ")))
##..........................................

## N98(2)

# def prostoe_chislo1(chislo):
#     i = 2
#     while i <= chislo:
#         if chislo % i != 0:
#             i +=1 
#         else:
#             break
#     #print(i)
#     if i == chislo:
#         rez = True
#     else:
#         rez = False
#     return(rez)
# r = prostoe_chislo1(int(input("Enter chislo --> ")))
# print(r)
##......................................


# ## N99
# n = int(input("Enter number: - "))
# for i in range(n + 1, 2*n):
#     otvet = prostoe_chislo1(i)
#     if otvet != True:
#         continue
#     else:
#         n1 = i
#         break
# print("Pervoe prostoe chislo, bolshe n --> ", n1 )
## .........................................

## N102
# def goodparol(parol):
#     if len(parol) < 8:
#         rez = False
#     else:
#         k = 0
#         l = 0
#         for i in parol:
#             if i.isdigit():
#                 k += 1
#             else:
#                 if ord(i) >= 65 and ord(i) <= 90:
#                     l += 1
#         if k == 0 or l == 0: 
#             rez = False
#         else:
#             rez = True
#     return(rez)
# nadejniparol = goodparol(input('Enter your parol : --> '))
# if nadejniparol == True:
#     print ("Vash parol nadejnij!")
# else:
#     print("Nenadejni parol, povtorite!")
##.........................


