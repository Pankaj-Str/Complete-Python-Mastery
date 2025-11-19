def info():
    print("welcome to python")
    print("this is basic function")

# call the function

info()
info()

def add():
    number1 = 800
    number2 = 800
    result = number1 + number2
    print("this is result : ",result)

# call the function
add()
add()

# function with arg...

# def FunctionName(Var1,Var2...etc):
#    output


def mul(number1,number2):
    result = number1 * number2
    print("this is result ",result)

# call function
mul(1200,8)
mul(456,80)
mul(1200,18)


x = 10
print(x)

# function with return type

def print_number():
    return 100*23

print(print_number())

# function with arg and return type

def get_result(number1,number2):
    result = number1*number2
    return result



print("this is result ",get_result(23,80))


def bill(price,gst):
    gst_amount = price*gst/100
    final_amount = gst_amount+price
    print("Price ",price)
    print("GST ",gst)
    print("GST Amount ",gst_amount)
    print("final Amount ",final_amount)


bill(1200,18)


