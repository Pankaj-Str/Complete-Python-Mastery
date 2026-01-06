print("welcome")

total = sum([23,24,25,16])
print(total)
min_1 = min([23,24,25,16])
print(min_1)
max_1 = max([23,24,25,16])
print(max_1)

# basic type
def info():
    print("welcome to codes with pankaj")
    print("cwpc.in")
    print("codeswithpankaj.com")

# call the function

info()
info()

# with arg/parameters(var)
def add(number1,number2):
    result = number1+number2
    print("result :- ",result)

# call the function
add(1200,800)
add(200,400)
add(20,400)

# example -
def bill(price,gst):
    gst_amount = price*gst/100
    final_price = price + gst_amount

    print("------bill-----")
    print("Price = ",price,"₹")
    print("GST = ",gst,"%")
    print("GST Amount = ",gst_amount,"₹")
    print("Total Amount = ",final_price,"₹")
    print("---------------")


#print bill
bill(1200,18.5)
bill(1800,9.2)
bill(560,2)
bill(4500,23)
bill(8900,8)















