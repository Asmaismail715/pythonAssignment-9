class LibraryManagementSystem:
    def __init__(self):
        self.books = []  
        self.users = []  
    def add_book(self, book_id, title, author, genre):
        book = {
            "id": book_id,
            "title": title,
            "author": author,
            "genre": genre,
            "status": "Available"
        }
        self.books.append(book)

    def add_user(self, user_id, name):
        user = {
            "id": user_id,
            "name": name,
            "borrowed_books": []
        }
        self.users.append(user)

    def borrow_book(self, user_id, book_id):
        user = self.get_user(user_id)
        book = self.get_book(book_id)
        if user and book:
            if book["status"] == "Available":
                book["status"] = "Checked Out"
                user["borrowed_books"].append(book_id)
                print(f'You have successfully borrowed "{book["title"]}".')
            else:
                print(f'Sorry, the book "{book["title"]}" is currently checked out.')
        else:
            print("Invalid User ID or Book ID.")

    def return_book(self, user_id, book_id):
        user = self.get_user(user_id)
        book = self.get_book(book_id)
        if user and book and book_id in user["borrowed_books"]:
            book["status"] = "Available"
            user["borrowed_books"].remove(book_id)
            print(f'You have successfully returned "{book["title"]}".')
        else:
            print("Invalid User ID or Book ID, or you haven't borrowed this book.")

    def get_user(self, user_id):
        for user in self.users:
            if user["id"] == user_id:
                return user
        return None

    def get_book(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                return book
        return None

    def search_books(self, search_term):
        results = [book for book in self.books if 
                   search_term.lower() in book["title"].lower() or 
                   search_term.lower() in book["author"].lower() or 
                   search_term.lower() in book["genre"].lower()]
        return results

    def view_books_by_status(self, status):
        return [book for book in self.books if book["status"] == status]

    def display_books(self, books):
        for book in books:
            print(f'{book["id"]}. "{book["title"]}" by {book["author"]} ({book["status"]})')

    def main_menu(self):
        while True:
            print("\nWelcome to the Community Library System!")
            print("----------------------------------------")
            print("Please choose an option:")
            print("1. View all books")
            print("2. Search for a book")
            print("3. Borrow a book")
            print("4. Return a book")
            print("5. View all users")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                print("All Books:")
                self.display_books(self.books)

            elif choice == '2':
                search_term = input("Enter title, author, or genre to search: ")
                results = self.search_books(search_term)
                if results:
                    print("Search Results:")
                    self.display_books(results)
                else:
                    print("No books found.")

            elif choice == '3':
                user_id = int(input("Enter your User ID: "))
                book_id = int(input("Enter the Book ID you want to borrow: "))
                self.borrow_book(user_id, book_id)

            elif choice == '4':
                user_id = int(input("Enter your User ID: "))
                book_id = int(input("Enter the Book ID you want to return: "))
                self.return_book(user_id, book_id)

            elif choice == '5':
                print("Users:")
                for user in self.users:
                    print(f'User ID: {user["id"]}, Name: {user["name"]}, Borrowed Books: {user["borrowed_books"]}')

            elif choice == '6':
                print("Exiting the system.")
                break

            else:
                print("Invalid choice. Please try again.")



library_system = LibraryManagementSystem()
library_system.add_book(1, "To Kill a Mockingbird", "Harper Lee", "Fiction")
library_system.add_book(2, "1984", "George Orwell", "Dystopian")
library_system.add_book(3, "The Great Gatsby", "F. Scott Fitzgerald", "Classic")
library_system.add_user(1, "Alice")
library_system.add_user(2, "Bob")

# Start the menu-driven interface
library_system.main_menu()
