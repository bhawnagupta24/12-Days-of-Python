# For loop

a = range(1, 21, 1)

for i in a:
    print(i)


for i in range(16, 0, -1):
    print(i)

for i in range(5,51,5):
    print(i)



a = "BHAWNA TEACHES INDUSTRY THINGS"
print(len(a))

for i in range(len(a)):
    print(a[i])

for i in range(1, 21):
    if i == 15:
        continue

    print(i)









While loop

a = int(input("Tell your number : "))

while a>0:
    print(a%10)
    a//=10



a = int(input("Tell your number : "))
reverse = 0
while a>0:
    reverse = reverse * 10 + a % 10
    a//=10
    print(reverse)



a = int(input("Tell your number : "))
copy = a
reverse = 0

while a>0:
    reverse = reverse * 10 + a % 10
    a//=10

if reverse == copy:
    print("Palindrome number")
else:
    print("Not Palindrome number")