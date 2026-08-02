# question 1


for i in range(n):
    print("hello world")


#question 2 

n = int(input("please tell your number "))

for i in range(1,n+1):
    print(i)


#question 3

n = int(input("please tell your number "))

for i in range(n,0,-1):
    print(i)



#question 4


n = int(input("which table you want :- "))

for i in range(1, 11):
    print(f"{n} * {i} = {n*i}")



#question 5

n = int(input("please tell your number:- "))

sum = 0

for i in range(1, n + 1):
    sum = sum + i

print(f"your sum is {sum}")



#question 6

n = int(input("please tell your number:- "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print(f"your sum is {fact}")


#question 7

n = int(input("tell your number :- "))

even = 0
odd = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i

print(f"your even and odd sum are {even} , {odd}")


#question 8

n = int(input("which number factors you want :- "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i)



#question 9

n = int(input("check your number is perfect or not :-"))

sum = 0

for i in range(1, n):
    if n % i == 0:
        sum = sum + i

if sum == n:
    print("Your number is perfect")

else:
    print("Not a perfect number")



#question 10

n = int(input("check your number is prime or not :-"))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1

if count==2:
    print("Prime number")
else:
    print("Not a prime")




#question 11

a = "SHERYIANS"

for i in range(len(a) - 1, -1, -1):
    print(a[i])



#question 12

a = "NAMAN"

b = ""

for i in range(len(a) - 1, -1, -1):
    b = b + a[i]

if b == a:
    print("your string is pallindrome")
else:
     print("your string is not pallindrome")




#question 13

a = "sdfsogn12413@#$%^&U"

char = 0
dig = 0
spchr = 0

for i in a:
    if i.isdigit():
        dig += 1

    elif i.isalpha():
        char += 1

    else:
        spchr += 1

print(f"your digits are {dig}\nyour alphabets are {char}\nyour special characters are {spchr}")