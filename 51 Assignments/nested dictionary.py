nested_dict = {
    "person1": {
        "name": "Alice",
        "age": 25,
        "address": {
            "street": "123 Main St",
            "city": "Cityville",
            "zipcode": "12345"
        }
    },
    "person2": {
        "name": "Bob",
        "age": 30,
        "address": {
            "street": "456 Oak St",
            "city": "Townsville",
            "zipcode": "67890"
        }
    }
}

# Function to print nested dictionary keys and values
def print_nested_dict(dictionary, path=""):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            print_nested_dict(value, f"{path}/{key}")
        else:
            print(f"{path}/{key}/\"{value}\"")

# Example usage
print_nested_dict(nested_dict)