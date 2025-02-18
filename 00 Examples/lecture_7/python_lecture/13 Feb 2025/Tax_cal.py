def tax_18(price):
    gst = 18
    gst_amount = price*gst/100
    return gst_amount

def tax_18_include(price):
    gst = 18
    gst_amount = price*gst/100
    mrp = price + gst_amount
    return mrp