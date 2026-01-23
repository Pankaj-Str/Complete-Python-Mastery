data = "CWPC"

for i in data:
    print(i)

# range(end) # start 0
print("# range(end) # start 0")
for i in range(10):
    print(i)

# range(start,end) 
print("# range(start,end)")

for i in range(11,20):
    print(i)


# range(start,end,steps) 
print("# range(start,end,step)")

for i in range(20,100,5):
    print(i)


# end =''

for i in range(30):
    print(i,end='|')


for i in range(-11,1):
    print(-i)


print('-------------------------')
a = 0
for i in range(11):
    a = a + i
print(a)


print('-----------------------')
a = int(input('Enter Number = '))
for i in range(1,11):
    print(a,'X ',i,'=',i*a)









