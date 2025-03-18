import Tax_cal as tc

price = 5000

gst = tc.tax_18(price)

print(f'your gst values : {gst}  and {price}')

mrp = tc.tax_18_include(price)
print(f'the MRP : {mrp}')