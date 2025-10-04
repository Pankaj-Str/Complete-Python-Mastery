def bill(price,gst=18):
    gst_amount = price*gst/100
    total_amount = price+gst_amount
    print(f'Price : {price}₹')
    print(f'GST {gst}%')
    print(f'GST amount {gst_amount}₹')
    print(f'Total = {total_amount}₹')
    print(f'--------------------------')


def get_total(price,gst=18):
    gst_amount = price*gst/100
    total_amount = price+gst_amount 
    return total_amount  