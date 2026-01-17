#-- User input section
#Enter Product List Size : 4
#Enter Product 1 -
#Samosa
#Enter Product 2 -
#Kachori
#Enter Product 3 -
#Fafda
#Enter Product 4 -
#Jalebi

#Enter Samosa Price :
#300/-
#Enter Kachori Price :
#100/-
#Enter Fafda Price :
#100/-
#Enter Jalebi Price :
#200/-

#--- output

#samosa = 300
#kachori = 100
#fafda = 100
#jalebi = 200

# Answer -


list_size = int(input('Enter List Size - '))
price = []
products = []

for i in range(list_size):
    i = input('Enter Product Name - ')
    products.append(i)


for i in range(list_size):
    i = int(input('Enter Product Price - '))
    price.append(i)



for i in range(list_size):
    print((i+1),'. ',products[i],' = ',price[i])




















