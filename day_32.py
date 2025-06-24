


def test_function():
    print("testing function")

def setsMethods():
    s1 = {1,2,3,4,5}
    s2 ={5,6,7}
    print(s1.union(s2))
    print(s1.intersection(s2))
    print(s1.symmetric_difference(s2))

def dictionary():
    dict = {"vivek": "sharma", "Neha":"Vashistha"}
    print(dict["Neha"])
    print(dict.values())
    for val in dict.values():
        print(val)
    for key in dict.keys():
        print(f"Fisrt name: {key} , surname is : {dict[key]}")

def forWithElse():
    for i in range(5):
        print(i)
    else:
        print(f"sorry no {i}")

    for i in range(5):
        if(i==4):
            break:
    else:
        print("check break")

if __name__ == "__main__":
    print("test main script file")
    test_function()
    setsMethods()
    dictionary()
    forWithElse()