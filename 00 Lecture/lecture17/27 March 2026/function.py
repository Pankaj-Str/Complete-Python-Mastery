# create a function
def info():
    print("welcome to codeswithpankaj.com")
    print("welcome to cwpc.in")

# call function
info()

for i in range(5):
    print(i+1)
    info()

# ---- function with arg., parameters (var)
def result(number1,number2):
    add = number1 + number2
    print("result = ",add)

# call the function
result(900,800)
result(1900,800)
result(4500,800)
result(6700,600)



def bill(price,gst):
    gst_amount = price*gst/100
    final_price = price + gst_amount
    print("----bill----------")
    print("Price = ",price,"₹")
    print("GST % = ",gst,"%")
    print("GST amount = ",gst_amount,"₹")
    print("MRP = ",final_price,"₹")
    print("--------------")
    

bill(1200,18)
bill(3400,9)
bill(4500,2)
bill(7800,12)


















