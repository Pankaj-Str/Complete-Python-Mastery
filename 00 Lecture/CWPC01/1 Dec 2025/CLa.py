import sys
# command line arguments
print("Command Line Arguments:", sys.argv)

if len(sys.argv) < 2:
   print("No additional command line arguments provided.")
else:
    name1 = sys.argv[1]
    print(f"Hello, {name1}!")
    
age = 21 
if age < 18:
    sys.exit("Sorry, you are not eligible to vote.")
    sys.exit()
print("welcome.")    