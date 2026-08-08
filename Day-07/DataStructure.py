#List 

a=[20,30,40,50,60,True,print()]

print(a[-1])



#1st way using index

for i in range(len(a)):
    print(a[i])


#2nd way using index
for i in a:
    print(i)


# print(dir(list))   #how many methods of list ds

# help(list)

a.append(6)
print(a)

a.insert(6,5)
print(a)






#Tuple

a =(1,2,3,4,5)

print(a)

#two methids present in tuples are 

a = (1, 2, 3, 4, 5, 5, 5.5, print(), "hello")

index = a.index(5)
print(index)

count = a.count(5)
print(count)



a =(1,)
print(type(a))







#Set
b = hash("Hello")
print(b)

c = hash((1, 2, 344))

print(c)


a= {1,8,9,2,3,4,5}
for i in a:
    print(i)


a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

s = a.union(b)   #a|b
s = a.intersection(b)  #a&b

print(s)





#Dictionary

d = {10: 100, 20: 200, 30: 300, 40: 400}

d[10]=1000
print(d[10])
print(d)

d[50]=500  #creating
d.update({50:500})

del d[30]
print(d)



for i in d.values():
    print(i)

d.clear()
print(d)



#deep copy

a = [1, 2, 3, 4, 5]

b = a

b[0] = 100

print(a)

#shallow copy

a = [1, 2, 3, 4, 5]

b = a.copy()

b[0] = 100

print(a)



d = {10: 100, 20: 200, 30: 300, 40: 400}

d2 = d.copy()
d2 = d.get(20)
d2 = d.items()
print(d2)


d = {10:100,20:200,30:300,40:400}

print(d.items())
