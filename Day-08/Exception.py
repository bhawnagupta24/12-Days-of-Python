a = int(input("tell your number :- "))

print(10 / a)

print("ok i have done the division")


a = int(input("tell your number :- "))

try:
    print(10 / a)

except ZeroDivisionError:
    print("sorry you cannot divide by 0")

print("ok i have done the division")


a = int(input("tell your number :- "))





try:
    print(10 / a)

except Exception as err:
    print(f"sorry there is an err by {err} ")

print("ok i have done the division")









try:
    print(10 / a)

except Exception as err:
    print(f"sorry there is an err as {err}")

else:
    print("good there is no exception")

finally:
    print("i will run no matter what")









age = int(input("tell your age :- "))

if age < 10 or age > 18:
    raise ValueError("your age must be between 10 and 18")

else:
    print("welcome to the club")

print("the club will start soon")

age = int(input("tell your age :- "))

try:

    if age < 10 or age > 18:
        raise ValueError("your age must be between 10 and 18")

    else:
        print("welcome to the club")

except Exception as err:
    print(f"an error occured as {err}")

print("the club will start soon")