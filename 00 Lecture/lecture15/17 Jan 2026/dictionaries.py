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
    

