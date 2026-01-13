#List Methods
#append()
#extend()
#insert()
#remove()
#pop()
#clear()
#index()
#count()
#sort()
#reverse()
#copy()

data = [21,22,23,24,25,26]
print(data)

# print using loop
for i in data:
    print(i)

#append()
data.append(99)
print(data)
#extend()
data.extend([22,33,44])
print(data)
#insert()
data.insert(3,99)
print(data)
#remove()
#data.remove(99)
#print(data)
#pop()
data.pop()
print(data)
#clear()
data.clear()
#index()
print(data.index(23))
#count()
print(data.count(55))

#sort()
data.sort()
print(data)
#reverse()
data.reverse()
print(data)
#copy()
d1 = data.copy()
print(d1)


