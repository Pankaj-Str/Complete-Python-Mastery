def info():
    print("welcome")
    
def Print_bill(price,tax):
    gst_amount = price*tax/100
    total_amount = gst_amount+price
    print(f'---------bill-----------')
    print(f'Amount = ₹{price}')
    print(f'GST = {tax}%')
    print(f'GST Amount = ₹{gst_amount}')
    print(f'Total Amount + GST = ₹{total_amount}')    
 
def get_mrp(price,tax):
    gst_amount = price*tax/100
    total_amount = gst_amount+price
    return total_amount    