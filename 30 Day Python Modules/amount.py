def bill(price,gst):
    gst_amount = price*gst/100
    final_total = gst_amount + price
    print('----bill-------')
    print(f'Price : {price}')
    print(f'GST % {gst}%')
    print(f'GST Amount {gst_amount}/-')
    print(f'MRP include GST : {final_total}/-')