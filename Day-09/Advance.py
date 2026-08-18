# #decorater

# def decorate(func):

#     def wrapper():
#         print("I will print myself before the function hello ")
#         func()
#         print("I will print after the function")

#     return wrapper


# @decorate
# def hello():
#     print("hello I am akarsh vyas ")

# hello()




# #args


# def addition(*args):
#     print(args)

# addition(12, 12, 23, 56)






# #kwargs



# def decorate(func):

#     def wrapper(*args, **kwargs):
#         print("the addition to your numbers are ")
#         func(*args, **kwargs)
#         print("thankyou I hope you liked it ")

#     return wrapper


# @decorate
# def addition(a, b):
#     print(f"your total is {a + b} ")


# addition(12, 67)









# #Comprehension

# l = [i for i in range(1, 21) if i % 2 == 0]

# print(l)




# #lambda

# addition = lambda a, b: a + b

# print(addition(12, 13))



# #map

# a = [1, 2, 3, 4, 5]

# result = map(lambda x: x * 2, a)

# print(list(result))




# #filter


# def even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# result = filter(even, a)

# print(list(result))


# #same code as before

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# result = filter(lambda x: True if x % 2 == 0 else False, a)

# print(list(result))




import Maths

print(Maths.addition(12,12))
