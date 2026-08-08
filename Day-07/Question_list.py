#question 1

l = [-45, 67, 12, -68, -69, 34]

print("positive elements are ")

for i in l:
    if i >= 0:
        print(i)


print("negtive elements are ")
for i in l:
    if i <= 0:
        print(i)


#question 2

a = [1,2,4,5,6]
sum=0

for i in a:
    sum+=i

print(sum/len(a))




#question 3

l = [12, 567, 43, 235, 347, 568, 45]

largest = l[0]
index = 0

for i in range(len(l)):
    if l[i] > largest:
        largest = l[i]
        index = i

print(f"your largest number is {largest} at index {index}")



#question 4



l = [12, 567, 43, 235, 347, 568, 45]

largest = l[0]
Second_largest= l[0]
index = 0

for i in l:
    if i > largest:
        Second_largest=largest
        largest = i
    elif i > Second_largest:
        Second_largest = i

print(Second_largest,largest)



#question 5

a = [12, 13, 14, 15, 16]

for i in range(len(a) - 1):
    if a[i] < a[i + 1]:
        continue

    else:
        print("your list is not sorted")
        break

else:
    print("Your list is sorted")

