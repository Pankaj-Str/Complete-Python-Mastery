# basic function
def info():
    print("welcome to codeswithpankaj.com")
    print("cwpc.in")


# call function
info()
info()


# function with parameters
def add(x,y):
    result = x + y
    print("this is result = ",result)


# call function
add(34,78)
add(300,800)


# Example :-

def bill(price,gst):
    print("\n-------bill--------\n")
    gst_amount = price*gst/100
    total_price = price + gst

    print("Price = ",price,"₹")
    print("GST % = ",gst,"%")
    print("GST Amount = ",gst_amount,"₹")
    print("MRP (Include GST ",gst,"%) = ",total_price)
    print("\n-------------------\n")


bill(1200,18)
bill(6200,2)
bill(3600,9)
bill(56000,16)


# return type
x = 10
print(x)

def get_number():
    return 100*78

print(get_number())

# return with parameters

def get_number1(a,b):
    return a*b

print(get_number1(10,90))













