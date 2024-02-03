# Python butterfly star pattern
# Code by @codeswithpankaj.com

def create_butterfly_pattern(rows):
    """
    Function to create a butterfly star pattern.
    
    :param rows: Number of rows in each wing of the butterfly.
    """
    for i in range(0, rows):
        # Print left wing spaces
        for j in range(0, i):
            print(" ", end="")
        
        # Print left wing stars
        for k in range(0, 2 * (rows - i) - 1):
            print("*", end="")
        
        # Move to the next line after each row
        print()
    
    for i in range(rows-2, -1, -1):
        # Print right wing spaces
        for j in range(0, i):
            print(" ", end="")
        
        # Print right wing stars
        for k in range(0, 2 * (rows - i) - 1):
            print("*", end="")
        
        # Move to the next line after each row
        print()

# Example: Create a butterfly pattern with 5 rows in each wing
create_butterfly_pattern(5)