# import random
# def func(s:str = "")->str:
#     for _  in range(random.randint(7,10)):
#         s+= chr(random.randint(33,126))
#     return s


##........................
# list1 = [-1, 150, 190, 170, -1, -1, 160, 180]
# ind_1 = []
# for i in range(0,len(list1)):
#     if list1[i] == -1:
#         ind_1.append(i)
# print(ind_1)
# list1.sort()
# print(list1)
# newlist = []
# for i in list1:
#     if i != -1:
#         newlist.append(i)
# print(newlist)
# for i in ind_1:
#     newlist.insert(i,-1)
# print(newlist) 

list1 = [-1, 150, 190, 170, -1, -1, 160, 180]
ind_1 = []
newlist = []
for i in range(0,len(list1)):
    if list1[i] == -1:
        ind_1.append(i)
    else:
        newlist.append(list1[i])
for i in ind_1:
    newlist.insert(i,-1)
print(newlist) 
##................................
