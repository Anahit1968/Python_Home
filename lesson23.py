# N1 - a, c
# N2
# N3 -g
# N4 -


# N5 
# def Sum1(b):
#     s = 0
#     for i in b:
#         s += i
#     return s 
# print(Sum1([7,8,5,4]))

# N6
# N7 - mylist.sort()
# mylist = [7,8,4,5,3,4,6]
# mylist.sort()
# print(mylist)

# N9 - [1,2,3]

# N10 -g
# N11 - առանձնացնում է տարրերը միմյանցից

# N12 - miavorum e tarrer@
# N13 - d  \([:])
# N14 
# mydict = {1:"a", 2:"b",3:"c"} 
# for key in mydict:
#     print(key)

# N15 
mydict = {
    "D" :56,
    "E" :12,
    "F" :69,
    "C" :45,
    "B" :23,
    "A" :67
}

mydict_sorted = sorted(mydict.values())
print (mydict_sorted)
# for i in range(0,4):
#     print(i ,":" ,mydict_sorted[i])


# N16
mydict = {"a": 1, "b" : 2}

# N17
# N18
# N19
# N20 - b
# N21  mekangamja funcion - 
# N 22 - a
# N23 ինքնուրույն աշխատող ծրագիր, որն օգտագործվում է, մեծ ծրագրերում 
# N24 - functia, vorn inq ir mej kanchum e iren
# N25 
def mult1(*x):
    p = 1
    for i in x:
        p *= i
    return p
print(mult1(1,2,3,4,5))
# N26
def recurs(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * recurs(n-1)
print(recurs(int(input("Enter number:   "))))

# N27 - raise

# N28 tvjalneri tesak
# N29
import json
mylist = [1,2,3,4,5,6,7,8,9]
s = 0
for i in mylist:
    s += i
print(s)
with open("sum1.json","w") as P:
     json.dump( {"Summa " : s} , P)



