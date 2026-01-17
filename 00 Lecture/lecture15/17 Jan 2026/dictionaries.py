# https://cwpc.in/unleash-the-power-of-python-dictionaries-a-comprehensive-guide-with-examples-04adf6449de2
data = {} # empty dictionaries
print(type(data))


# data = {"key":"value"}

data = {"Name":"Joy","Age":56,"height":4.5}

print(data)


# access data
print(data["Name"])

# new data into dictionaries

data['city'] = 'mumbai'
print(data)

# update item
data['Age'] = 23
print(data)

# using for loop data print

for i in data:
    print(i,' = ',data[i])

# delete

del data['city']

print(data)


#clear()
# data.clear()
#copy()
d1 = data.copy()
print(d1)
#get()
print(data.get('Name'))
#items()
print(data.items())
#keys()
print(data.keys())
#values()
print(data.values())
#pop()
data.pop('height')
print(data)
#update() # add new data
data_new = {"course":"Java","Marks":56}
data.update(data_new)
print(data)


