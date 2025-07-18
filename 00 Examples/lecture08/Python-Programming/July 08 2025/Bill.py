import tax as t
def demo():
    print("this is demo file ..........")
    
    
# call the function    
demo()

t.info()



t.Print_bill(1400,2)

mrp = t.get_mrp(1400,18)

final_mrp = mrp-20
print(final_mrp)