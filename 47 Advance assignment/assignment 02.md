### Assignment: Library Management System using Functions

#### Objective:
Create a Python program to manage a library system using functions. The program should allow users to add books, borrow books, return books, and view the available books.

#### Assignment Questions:

**Question 1: Basic Library Management System**

1. **Book Management:**
    - Add a Book
    - View All Books

2. **Borrow and Return Books:**
    - Borrow a Book
    - Return a Book

### Features to Implement:
- **Function to Add a Book**: Create a function that allows the user to add books to the library.
- **Function to View All Books**: Create a function that displays all the books in the library.
- **Function to Borrow a Book**: Create a function that allows the user to borrow a book.
- **Function to Return a Book**: Create a function that allows the user to return a book.

### Example Output:

```
Library Management System
-------------------------
1. Add a Book
2. View All Books
3. Borrow a Book
4. Return a Book
5. Exit

Enter your choice: 1

Enter Book Title: Python Programming
Enter Book Author: John Doe
Book added successfully!

Library Management System
-------------------------
1. Add a Book
2. View All Books
3. Borrow a Book
4. Return a Book
5. Exit

Enter your choice: 2

Available Books:
1. Python Programming by John Doe
```

**Question 2: Enhanced Library Management System**

1. **Book Details:**
    - Book ID
    - Book Title
    - Book Author
    - Book Quantity

2. **Borrow and Return Tracking:**
    - Track which user borrowed which book
    - Track the date of borrowing and returning

### Additional Features to Implement:
- **Function to Add Book Details**: Create a function to add detailed information about the books including ID, title, author, and quantity.
- **Function to Track Borrowed Books**: Create a function to track which user borrowed which book and the date of borrowing.
- **Function to Track Returned Books**: Create a function to track when books are returned.

### Example Output with Enhanced Features:

```
Library Management System
-------------------------
1. Add a Book
2. View All Books
3. Borrow a Book
4. Return a Book
5. Exit

Enter your choice: 1

Enter Book ID: 101
Enter Book Title: Python Programming
Enter Book Author: John Doe
Enter Book Quantity: 5
Book added successfully!

Library Management System
-------------------------
1. Add a Book
2. View All Books
3. Borrow a Book
4. Return a Book
5. Exit

Enter your choice: 3

Enter Book ID to Borrow: 101
Enter Your Name: Alice
Book borrowed successfully!

Library Management System
-------------------------
1. Add a Book
2. View All Books
3. Borrow a Book
4. Return a Book
5. Exit

Enter your choice: 4

Enter Book ID to Return: 101
Enter Your Name: Alice
Book returned successfully!
```

**Question 3: Advanced Features for Library Management System**

1. **User Management:**
    - Add User
    - View Users

2. **Search and Filter Books:**
    - Search books by title or author
    - Filter books by availability

3. **Data Persistence:**
    - Save the book and user data to a file
    - Load the data from the file when the program starts

### Features to Implement:
- **Function to Add and View Users**: Create functions to manage user information.
- **Function to Search and Filter Books**: Create functions to search for books by title or author and filter by availability.
- **Function for Data Persistence**: Create functions to save and load data to/from a file.

### Example Output with Advanced Features:

```
Library Management System
-------------------------
1. Add a Book
2. View All Books
3. Borrow a Book
4. Return a Book
5. Add a User
6. View Users
7. Search Books
8. Filter Books by Availability
9. Save Data
10. Load Data
11. Exit

Enter your choice: 1

Enter Book ID: 101
Enter Book Title: Python Programming
Enter Book Author: John Doe
Enter Book Quantity: 5
Book added successfully!

Library Management System
-------------------------
1. Add a Book
2. View All Books
3. Borrow a Book
4. Return a Book
5. Add a User
6. View Users
7. Search Books
8. Filter Books by Availability
9. Save Data
10. Load Data
11. Exit

Enter your choice: 7

Enter title or author to search: Python
Search Results:
1. Python Programming by John Doe

Library Management System
-------------------------
1. Add a Book
2. View All Books
3. Borrow a Book
4. Return a Book
5. Add a User
6. View Users
7. Search Books
8. Filter Books by Availability
9. Save Data
10. Load Data
11. Exit

Enter your choice: 8

Available Books:
1. Python Programming by John Doe
```

### Example Python Code for Basic Functionality:

```python
def add_book(books):
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Book Author: ")
    quantity = int(input("Enter Book Quantity: "))
    books[book_id] = {'title': title, 'author': author, 'quantity': quantity}
    print("Book added successfully!")

def view_books(books):
    print("Available Books:")
    for book_id, details in books.items():
        print(f"{book_id}: {details['title']} by {details['author']} (Quantity: {details['quantity']})")

def borrow_book(books, borrowed_books):
    book_id = input("Enter Book ID to Borrow: ")
    if book_id in books and books[book_id]['quantity'] > 0:
        user_name = input("Enter Your Name: ")
        books[book_id]['quantity'] -= 1
        borrowed_books[book_id] = user_name
        print("Book borrowed successfully!")
    else:
        print("Book not available.")

def return_book(books, borrowed_books):
    book_id = input("Enter Book ID to Return: ")
    if book_id in borrowed_books:
        user_name = input("Enter Your Name: ")
        if borrowed_books[book_id] == user_name:
            books[book_id]['quantity'] += 1
            del borrowed_books[book_id]
            print("Book returned successfully!")
        else:
            print("This book was not borrowed by you.")
    else:
        print("Book ID not found in borrowed books.")

def main():
    books = {}
    borrowed_books = {}
    
    while True:
        print("\nLibrary Management System")
        print("-------------------------")
        print("1. Add a Book")
        print("2. View All Books")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_book(books)
        elif choice == '2':
            view_books(books)
        elif choice == '3':
            borrow_book(books, borrowed_books)
        elif choice == '4':
            return_book(books, borrowed_books)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

This assignment helps students understand how to create a simple library management system using functions, manage data, handle user inputs, and implement basic features for a real-world application.