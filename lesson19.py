import json


# with open ("test.json", "w") as x:
#     json.dump({"name":"Albert"}, x)

# with open("test.json") as f:
#     rez = json.load(f)
# print(rez)

# with open("mydoc.json","w") as P:
#     json.dump({"name": "Anahit", "surname": "Kochinyan"}, P)

# with open("mydoc.json") as Y:
#     rez = json.load(Y)
#     print(rez)

with open("mydoc.json") as X:
    a = json.load(X)
    print(a)
    n = input("Enter name -->  ")
    for i in a.values():
        if i == n:
            print("Yes!")
            break   
        else:
            print("No") 
    
