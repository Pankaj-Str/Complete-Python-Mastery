def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        result = None
    except TypeError:
        print("Invalid operand types. Please use numbers.")
        result = None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        result = None
    else:
        print(f"The result is: {result}")
    finally:
        print("Execution completed.")

# Test cases
print("Test case 1:")
divide(10, 2)

print("\nTest case 2:")
divide(10, 0)

print("\nTest case 3:")
divide("10", 2)
