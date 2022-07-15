## N1
# first = ["Ani", "Anna","Aram"]
# second = [1,2,3]
# newlist = {}
# for i , j in zip(first,second):
#     newlist[i] = j
# print(newlist)
# with open("mydict.txt", "w") as X:
#     X.write(f"{newlist}")
##...................................................


## N2
import json
# text = '''Whether I'm riding down a highway
# Or walking down a street
# It makes no difference, baby doll
# Wherever we chance to meet
# Each time I hold your little hand
# It makes me feel so very nice '''
# with open("mysong.json", "w") as Y:
#     json.dump(text,Y)
# with open("mysong.json") as x:
#     rez = json.load(x)
# print(rez)
#.................................................
# 
# # N3 
# def summa(num):
#     s = 0
#     list1 = []
#     for i in range(1,num):
#         if i % 3 == 0 or i % 5 == 0:
#             s += i
#             list1.append(i)
#     Q = f'summa = {s}\n3- i ev 5- i bajanararnern en {list1}'
#     return Q
# D = summa(int(input("enter number -->")))
# print(D)
# with open("Sum1.json", "w") as f:
#     json.dump(D,f)
##..........................................

# ## N4
# char = "a,e,i,o,u,y"
# s = 0
# slovo = input("Enter word: -->")
# for i in slovo:
#     if i in char:
#         s += 1
# rez = f'word is - {slovo}\nvowels count - {s}'
# print(rez) 
# with open("Wovels.json", "w") as X:
#     json.dump(rez,X)
# ##.......................................

## N5
##Another pause and more eying and siding around each other
# with open("text.txt","w") as T:
#     T.write("Another pause and more eying and siding around each other")
# count1 = 0
# count2 = 0
# mydict ={}
# with open("text.txt", "rt") as X:
#     X1 = X.read()
#     X1 = X1.split(" ")
#     print(X1)
#     for i in X1:
#         if i == "Another" :
#             count1 += 1
#         elif i == "and":
#             count2 += 1
#     mydict["Another"] = count1
#     mydict["and"] = count2
#     print(mydict)

##.........................................

# ## N 6
# list1 = ["a", "b", "c", "d", "b", "f"]
# list2 = [] 
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)

## ............................................

## N7
# with open("text.txt", "rt") as text:
#     count1 = 0
#     count2 = 0
#     rez  = text.read()
#     for i in rez:
#         if i.islower():
#             count1 +=1
#         elif i.isupper():
#             count2 += 1
# print(f'louer letter is {count1}\n upper letters is {count2}') 

