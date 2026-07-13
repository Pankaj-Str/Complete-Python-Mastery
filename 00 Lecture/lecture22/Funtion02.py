# basic
# with parameter
# return type
# x = 100
# print(x)

# return type
def get_number():
    return 67 * 7
# print function
print(get_number())

def get_name():
    return "Nishant"

print("my name is ",get_name())
# return + parameter
def mul(number1,number2):
    result = number1 * number2
    return result

# print function
print("result is ",mul(1200,6))
print("result is ",mul(450,2))

# example :
def bill(price,gst):
    gst_amount = price * gst / 100
    return gst_amount

# function call
price1 = 1200
gst_amount = bill(price1,18)
print("total gst ",gst_amount+price1)

# min()
print(min([12,13,14,15,6,7,8]))
# max()
print(max([12,13,14,15,6,7,8]))
# sum()
print(sum([12,13,14,15,6,7,8]))






    


