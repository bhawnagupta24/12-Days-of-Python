# def hello():
#     print("hello i am here")

# hello()



# #positional argument

# def sum(a, b):
#     print(f"The sum of your numbers is {a + b}")

# sum(12, 12)




# #keyword argument

# def hello(name, age):
#     print(f"your name is {name} and your age is {age}")

# hello(age = 22, name = "Bhawna")




# #default argument


# def sum(a, b=45):
#     print(f"The sum of your numbers is {a + b}")

# sum(12)
# sum(12,12)



def pallindrome(st):
    rev = ""

    for i in range(len(st)-1, -1, -1):
        rev = rev + st[i]

    if rev == st:
        print("pallindrome")
    else:
        print("not a pallindrome")

pallindrome("NAMAN")
pallindrome("CURSOR")
    

def hello():
    return "HELLO HOW ARE YOU"
print(hello())