### Assignment: Advanced Library Management System

#### Objective:
Enhance the basic library management system by adding advanced features such as user management, book search, data persistence, and reporting functionalities.

#### Assignment Questions:

**Question 1: User Management System**

1. **User Registration:**
    - Add a User
    - View All Users

2. **User Details:**
    - User ID
    - User Name
    - User Email
    - User Phone Number

### Features to Implement:
- **Function to Add a User**: Create a function that allows the user to register new users.
- **Function to View All Users**: Create a function that displays all registered users.

### Example Output:

```
Library Management System
-------------------------
1. Add a User
2. View All Users
3. Exit

Enter your choice: 1

Enter User ID: U101
Enter User Name: Alice
Enter User Email: alice@example.com
Enter User Phone Number: 1234567890
User added successfully!

Library Management System
-------------------------
1. Add a User
2. View All Users
3. Exit

Enter your choice: 2

Registered Users:
1. User ID: U101, Name: Alice, Email: alice@example.com, Phone: 1234567890
```

**Question 2: Book Search and Filtering**

1. **Search Books:**
    - Search by Title
    - Search by Author

2. **Filter Books:**
    - Filter by Availability

### Features to Implement:
- **Function to Search Books by Title or Author**: Create a function to search for books based on the title or author.
- **Function to Filter Books by Availability**: Create a function to filter and display books that are currently available for borrowing.

### Example Output:

```
Library Management System
-------------------------
1. Search Books
2. Filter Books by Availability
3. Exit

Enter your choice: 1

Enter title or author to search: Python
Search Results:
1. Book ID: 101, Title: Python Programming, Author: John Doe

Library Management System
-------------------------
1. Search Books
2. Filter Books by Availability
3. Exit

Enter your choice: 2

Available Books:
1. Book ID: 101, Title: Python Programming, Author: John Doe, Quantity: 5
```

**Question 3: Data Persistence**

1. **Save and Load Data:**
    - Save Book Data to a File
    - Load Book Data from a File

### Features to Implement:
- **Function to Save Data**: Create a function that saves the book and user data to a file.
- **Function to Load Data**: Create a function that loads the book and user data from a file when the program starts.

### Example Output:

```
Library Management System
-------------------------
1. Save Data
2. Load Data
3. Exit

Enter your choice: 1

Data saved successfully!

Library Management System
-------------------------
1. Save Data
2. Load Data
3. Exit

Enter your choice: 2

Data loaded successfully!
```

**Question 4: Reporting Features**

1. **Generate Reports:**
    - Generate a Report of All Books
    - Generate a Report of All Borrowed Books

### Features to Implement:
- **Function to Generate a Report of All Books**: Create a function that generates a report of all books in the library.
- **Function to Generate a Report of All Borrowed Books**: Create a function that generates a report of all borrowed books, including details of who borrowed them and when.

### Example Output:

```
Library Management System
-------------------------
1. Generate Report of All Books
2. Generate Report of All Borrowed Books
3. Exit

Enter your choice: 1

Report of All Books:
1. Book ID: 101, Title: Python Programming, Author: John Doe, Quantity: 5
2. Book ID: 102, Title: Data Science Basics, Author: Jane Smith, Quantity: 3

Library Management System
-------------------------
1. Generate Report of All Books
2. Generate Report of All Borrowed Books
3. Exit

Enter your choice: 2

Report of All Borrowed Books:
1. Book ID: 101, Title: Python Programming, Borrowed By: Alice, Borrowed On: 2024-07-01
```

### Example Python Code for Advanced Features:

```python
import json

def add_user(users):
    user_id = input("Enter User ID: ")
    name = input("Enter User Name: ")
    email = input("Enter User Email: ")
    phone = input("Enter User Phone Number: ")
    users[user_id] = {'name': name, 'email': email, 'phone': phone}
    print("User added successfully!")

def view_users(users):
    print("Registered Users:")
    for user_id, details in users.items():
        print(f"User ID: {user_id}, Name: {details['name']}, Email: {details['email']}, Phone: {details['phone']}")

def search_books(books):
    query = input("Enter title or author to search: ").lower()
    results = [book for book in books.values() if query in book['title'].lower() or query in book['author'].lower()]
    print("Search Results:")
    for book in results:
        print(f"Book ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")

def filter_books_by_availability(books):
    available_books = [book for book in books.values() if book['quantity'] > 0]
    print("Available Books:")
    for book in available_books:
        print(f"Book ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Quantity: {book['quantity']}")

def save_data(books, users):
    data = {'books': books, 'users': users}
    with open('library_data.json', 'w') as f:
        json.dump(data, f)
    print("Data saved successfully!")

def load_data():
    try:
        with open('library_data.json', 'r') as f:
            data = json.load(f)
        return data['books'], data['users']
    except FileNotFoundError:
        return {}, {}

def generate_report_of_all_books(books):
    print("Report of All Books:")
    for book_id, details in books.items():
        print(f"Book ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Quantity: {details['quantity']}")

def generate_report_of_all_borrowed_books(borrowed_books):
    print("Report of All Borrowed Books:")
    for book_id, details in borrowed_books.items():
        print(f"Book ID: {book_id}, Title: {details['title']}, Borrowed By: {details['borrowed_by']}, Borrowed On: {details['borrowed_on']}")

def main():
    books, users = load_data()
    borrowed_books = {}

    while True:
        print("\nLibrary Management System")
        print("-------------------------")
        print("1. Add a User")
        print("2. View All Users")
        print("3. Search Books")
        print("4. Filter Books by Availability")
        print("5. Save Data")
        print("6. Load Data")
        print("7. Generate Report of All Books")
        print("8. Generate Report of All Borrowed Books")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_user(users)
        elif choice == '2':
            view_users(users)
        elif choice == '3':
            search_books(books)
        elif choice == '4':
            filter_books_by_availability(books)
        elif choice == '5':
            save_data(books, users)
        elif choice == '6':
            books, users = load_data()
        elif choice == '7':
            generate_report_of_all_books(books)
        elif choice == '8':
            generate_report_of_all_borrowed_books(borrowed_books)
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

This assignment helps students understand how to implement advanced features in a library management system using Python functions. It covers user management, book search, data persistence, and reporting functionalities.