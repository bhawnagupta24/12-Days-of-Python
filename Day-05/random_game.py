import random

random_number = random.randint(1,10)
print(random_number)

tries = 0

while True:

    a = int(input("Guess your number"))

    if random_number == a:
        tries += 1
        print(f"you are right u guess the number in {tries} tries")
        break

    elif a < random_number:
        print("go a little higher")
        tries += 1

    else:
        print("go a little lower")
        tries += 1
