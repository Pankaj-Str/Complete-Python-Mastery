product = []
price = []

size = int(input('Enter List Size '))

for i in range(size):
    i = input('Enter Product Name - ')
    product.append(i)

for i in range(size):
    i = int(input('Enter Product Price  '))
    price.append(i)

print('----------------------------')
yes = input('Do You Want to add GST [Y/N]')

if yes == 'Y' or yes == 'y':
    gst = int(input('Enter GST % '))
    total = 0
    for i in range(size):
        total = total + price[i]
        print((i+1),'. ',product[i],' => ',price[i],'/-')
    gstamount = total*gst/100
    mrp = gstamount+total
    print('GST % ',gst)
    print('GST Amount =>  ',gstamount,'/-')    
    print('MRP [include GST : ]',mrp)
else:
    total = 0
    for i in range(size):
        total = total + price[i]
        print((i+1),'. ',product[i],' => ',price[i],'/-')

    print('-----------------------------------------')
    print("total without GST = ",total)
