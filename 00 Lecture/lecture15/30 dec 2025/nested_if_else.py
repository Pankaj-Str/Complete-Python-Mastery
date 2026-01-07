x = 100
y = 200
z = 30

# x<y
# x<z

# y<x
# y<z

# z<x
# z<y

if x < y and x < z:
    print("x is smallest...")
elif y < x and y < z:
    print("y is smallest...")
elif z < x and z < y:
    print("Z is smallest...")    
