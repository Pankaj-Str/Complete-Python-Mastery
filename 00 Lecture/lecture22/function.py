# basic function
def info():
    print("welcome to codeswithpankaj.com")
    print("welcome to python tutorial...")


# call the function
info()
info()


# function with parameters (var)
def add(number1,number2):
    result = number1 + number2
    print("this is result : = ",result)

# call the function
add(233,567)
add(45,89)


# example -


def bill(price,gst):
    gst_amount = price * gst / 100
    total_price = price + gst_amount
    print("\n----------bill---------------\n")
    print("price = ",price)
    print("gst = ",gst,"%")
    print("gst amount = ",gst_amount)
    print("total = (include GST) ",total_price)


# call the function
bill(1200,18)
bill(1800,2)
bill(2300,9)














