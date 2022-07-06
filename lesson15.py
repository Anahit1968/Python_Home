
# def norhamar(tar, thiv):
#     import random
#     x1 = random.choice(thiv)
#     x2 = random.choice(thiv)
#     a1 = random.choice(tar)
#     a2 = random.choice(tar)
#     x3 = random.choice(thiv)
#     x4 = random.choice(thiv)
#     x5 = random.choice(thiv)
#     print(x1+x2+a1+a2+x3+x4+x5)
# tar = "QWERRYUIOPLKJHGFDSAZXCVBNM"
# thiv = "1234567890"
# norhamar(tar,thiv)


# def funct(n):
#     if n == 0:
#         return 1
#     else:
#         return n * funct(n - 1)
# print(funct(8))

def Fib(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return Fib(n-1) + Fib(n - 2) 
print(Fib(8))

