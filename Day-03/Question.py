# question 1

number = int(input("Your number is : "))
second = int(input("Your number is : "))

if number>second :
    print("a is greater")
else:
    print("b is greater")


# print(type(number))



# question 2

gen = input("please tell your gender as character (M or F):-")

if gen == 'M' or gen == 'm':
    print("Good morning SIR")

elif gen == "F" or gen == 'f':
    print("Good morning MAM")

else:
    print("Unidentified gender")
    


# question 3

num = int(input("please tell your number :- "))

if num % 2 == 0:
    print("even number")

else:
    print("Odd number")



# question 4

name = input("please tell your name :- ")
age = int(input("now tell your age :- "))

if age >= 18:
    print(f"hello {name} you are a valid vote")

else:
    print(f"hello {name} you are not a valid vote")

    
    
    
# question 5

year = int(input("tell your year :- "))

if year % 100 == 0 and year % 400 == 0:
    print("Its a leap year")

elif year % 100 != 0 and year % 4 == 0:
    print("Its a leap year")

else:
    print("its a normal year")



#question 6 

t = int(input("please tell the temprature :- "))

if t < 0:
    print("Freezing cold")

elif t >= 0 and t < 10:
    print("very cold")

elif t >= 10 and t < 20:
    print("cold")

elif t >= 20 and t < 30:
    print("pleasant")

elif t >= 30 and t < 40:
    print("hot")

else:
    print("very hot")