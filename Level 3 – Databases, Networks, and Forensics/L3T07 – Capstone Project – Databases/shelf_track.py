# Capstone Project - Databases

import sqlite3

DB_NAME = "ebookstore.db"

INITIAL_BOOKS = [
    (3001, "A Tale of Two Cities", 1290, 30),
    (3002, "Harry Potter and the Philosopher's Stone", 8937, 40),
    (3003, "The Lion, the Witch and the Wardrobe", 2356, 25),
    (3004, "The Lord of the Rings", 6380, 37),
    (3005, "Alice's Adventures in Wonderland", 5620, 12),
]

INITIAL_AUTHORS = [
    (1290, "Charles Dickens", "England"),
    (8937, "J.K. Rowling", "England"),
    (2356, "C.S. Lewis", "Ireland"),
    (6380, "J.R.R. Tolkien", "South Africa"),
    (5620, "Lewis Carroll", "England"),
]

SEPARATOR = "-" * 50

# Database setup

def get_connection():
    """This function opens and returns a connection to the SQLite database."""
    return sqlite3.connect(DB_NAME)

def create_tables(cursor):
    """This function createa the book and author tables if they do not already exist."""
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS author (
            id      INTEGER PRIMARY KEY,
            name    TEXT    NOT NULL,
            country TEXT    NOT NULL
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS book (
            id       INTEGER PRIMARY KEY,
            title    TEXT    NOT NULL,
            authorID INTEGER NOT NULL,
            qty      INTEGER NOT NULL,
            FOREIGN KEY (authorID) REFERENCES author(id)
        )
        """
    )

def seed_tables(cursor):
    """This function inserts initial data only if the tables are empty."""
    cursor.execute("SELECT COUNT(*) FROM author")
    if cursor.fetchone()[0] == 0:
        cursor.executemany(
            "INSERT INTO author (id, name, country) VALUES (?, ?, ?)",
            INITIAL_AUTHORS,
        )

    cursor.execute("SELECT COUNT(*) FROM book")
    if cursor.fetchone()[0] == 0:
        cursor.executemany(
            "INSERT INTO book (id, title, authorID, qty) VALUES (?, ?, ?, ?)",
            INITIAL_BOOKS,
        )

def initialise_database():
    """This function creates tables and seed initial data, then closes the connection."""
    with get_connection() as conn:
        cursor = conn.cursor()
        create_tables(cursor)
        seed_tables(cursor)
        conn.commit()

# Validation helpers

def validate_four_digit_id(raw: str, label: str = "ID") -> int:
    """
    Return the integer value of *raw* if it is a four-digit integer.
    Raise ValueError with a descriptive message otherwise.
    """
    raw = raw.strip()
    if not raw.isdigit():
        raise ValueError(f"{label} must contain digits only.")
    if len(raw) != 4:
        raise ValueError(f"{label} must be exactly 4 digits.")
    return int(raw)


def validate_positive_int(raw: str, label: str = "Value") -> int:
    """This function returns a positive integer or raise ValueError."""
    raw = raw.strip()
    if not raw.isdigit() or int(raw) < 0:
        raise ValueError(f"{label} must be a non-negative integer.")
    return int(raw)


def input_four_digit_id(prompt: str, label: str = "ID") -> int:
    """Prompt until a valid four-digit integer is entered."""
    while True:
        try:
            return validate_four_digit_id(input(prompt), label)
        except ValueError as exc:
            print(f"  Invalid input – {exc}")


def input_positive_int(prompt: str, label: str = "Value") -> int:
    """Prompt until a valid non-negative integer is entered."""
    while True:
        try:
            return validate_positive_int(input(prompt), label)
        except ValueError as exc:
            print(f"  Invalid input – {exc}")


def input_non_empty_string(prompt: str, label: str = "Field") -> str:
    """Prompt until a non-empty string is entered."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print(f"  {label} cannot be empty.")

# CRUD Operations

def add_book():
    """Prompt the user for new book details and insert into both tables."""
    print("\n--- Add New Book ---")
    book_id = input_four_digit_id("  Book ID (4 digits)  : ", "Book ID")
    author_id = input_four_digit_id("  Author ID (4 digits): ", "Author ID")
    title = input_non_empty_string("  Title               : ", "Title")
    qty = input_positive_int("  Quantity            : ", "Quantity")
    author_name = input_non_empty_string("  Author name         : ", "Author name")
    author_country = input_non_empty_string("  Author country      : ", "Author country")

    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            # Insert author first (ignore if already exists with same id)
            cursor.execute(
                """
                INSERT OR IGNORE INTO author (id, name, country)
                VALUES (?, ?, ?)
                """,
                (author_id, author_name, author_country),
            )
            cursor.execute(
                """
                INSERT INTO book (id, title, authorID, qty)
                VALUES (?, ?, ?, ?)
                """,
                (book_id, title, author_id, qty),
            )
            conn.commit()
        print(f"  ✓ Book '{title}' added successfully.")
    except sqlite3.IntegrityError:
        print("  ✗ A book with that ID already exists.")
    except sqlite3.Error as exc:
        print(f"  ✗ Database error: {exc}")


def update_book():
    """
    This function allows the user to update a book's quantity, title, or author details
    (name and/or country).  Uses INNER JOIN to display current info.
    """
    print("\n--- Update Book ---")
    book_id = input_four_digit_id("  Enter Book ID to update: ", "Book ID")

    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT b.id, b.title, b.qty, a.id, a.name, a.country
                FROM book b
                INNER JOIN author a ON b.authorID = a.id
                WHERE b.id = ?
                """,
                (book_id,),
            )
            row = cursor.fetchone()
            if not row:
                print("  ✗ No book found with that ID.")
                return

            _, title, qty, auth_id, auth_name, auth_country = row
            print(f"\n  Current details:")
            print(f"    Title          : {title}")
            print(f"    Quantity       : {qty}")
            print(f"    Author name    : {auth_name}")
            print(f"    Author country : {auth_country}\n")

            print("  What would you like to update?")
            print("    1. Quantity (default)")
            print("    2. Title")
            print("    3. Author name and/or country")
            field_choice = input("  Choice [1]: ").strip() or "1"

            if field_choice == "1":
                new_qty = input_positive_int("  New quantity: ", "Quantity")
                cursor.execute(
                    "UPDATE book SET qty = ? WHERE id = ?",
                    (new_qty, book_id),
                )
                print("  ✓ Quantity updated.")

            elif field_choice == "2":
                new_title = input_non_empty_string("  New title: ", "Title")
                cursor.execute(
                    "UPDATE book SET title = ? WHERE id = ?",
                    (new_title, book_id),
                )
                print("  ✓ Title updated.")

            elif field_choice == "3":
                print("  Leave blank to keep the current value.")
                new_name = input(f"  New author name [{auth_name}]: ").strip()
                new_country = input(f"  New author country [{auth_country}]: ").strip()

                if new_name or new_country:
                    updated_name = new_name if new_name else auth_name
                    updated_country = new_country if new_country else auth_country
                    cursor.execute(
                        "UPDATE author SET name = ?, country = ? WHERE id = ?",
                        (updated_name, updated_country, auth_id),
                    )
                    print("  ✓ Author details updated.")
                else:
                    print("  No changes made.")

            else:
                print("  Invalid choice. No changes made.")
                return

            conn.commit()

    except sqlite3.Error as exc:
        print(f"  ✗ Database error: {exc}")


def delete_book():
    """Remove a book from the database by ID."""
    print("\n--- Delete Book ---")
    book_id = input_four_digit_id("  Enter Book ID to delete: ", "Book ID")

    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT title FROM book WHERE id = ?", (book_id,))
            row = cursor.fetchone()
            if not row:
                print("  ✗ No book found with that ID.")
                return

            confirm = input(
                f"  Delete '{row[0]}'? This cannot be undone. (yes/no): "
            ).strip().lower()
            if confirm != "yes":
                print("  Deletion cancelled.")
                return

            cursor.execute("DELETE FROM book WHERE id = ?", (book_id,))
            conn.commit()
        print(f"  ✓ Book '{row[0]}' deleted.")
    except sqlite3.Error as exc:
        print(f"  ✗ Database error: {exc}")


def search_books():
    """Search for books by ID, title (partial match), or author name."""
    print("\n--- Search Books ---")
    print("  1. Search by Book ID")
    print("  2. Search by title")
    print("  3. Search by author name")
    choice = input("  Choice: ").strip()

    try:
        with get_connection() as conn:
            cursor = conn.cursor()

            if choice == "1":
                book_id = input_four_digit_id("  Book ID: ", "Book ID")
                cursor.execute(
                    """
                    SELECT b.id, b.title, a.name, b.qty
                    FROM book b
                    INNER JOIN author a ON b.authorID = a.id
                    WHERE b.id = ?
                    """,
                    (book_id,),
                )

            elif choice == "2":
                keyword = input_non_empty_string("  Title keyword: ", "Keyword")
                cursor.execute(
                    """
                    SELECT b.id, b.title, a.name, b.qty
                    FROM book b
                    INNER JOIN author a ON b.authorID = a.id
                    WHERE b.title LIKE ?
                    """,
                    (f"%{keyword}%",),
                )

            elif choice == "3":
                keyword = input_non_empty_string("  Author name keyword: ", "Keyword")
                cursor.execute(
                    """
                    SELECT b.id, b.title, a.name, b.qty
                    FROM book b
                    INNER JOIN author a ON b.authorID = a.id
                    WHERE a.name LIKE ?
                    """,
                    (f"%{keyword}%",),
                )

            else:
                print("  Invalid choice.")
                return

            results = cursor.fetchall()

    except sqlite3.Error as exc:
        print(f"  ✗ Database error: {exc}")
        return

    if not results:
        print("  No books found matching your search.")
        return

    print(f"\n  {'ID':<6} {'Title':<45} {'Author':<25} {'Qty'}")
    print("  " + SEPARATOR)
    for book_id, title, author, qty in results:
        print(f"  {book_id:<6} {title:<45} {author:<25} {qty}")


def view_all_book_details():
    """
    Display full details (title, author name, country) for every book,
    using a JOIN and the zip() function as specified in the brief.
    """
    print("\n--- Details of All Books ---")
    print(SEPARATOR)

    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT title FROM book ORDER BY id")
            titles = [row[0] for row in cursor.fetchall()]

            cursor.execute(
                """
                SELECT a.name, a.country
                FROM book b
                INNER JOIN author a ON b.authorID = a.id
                ORDER BY b.id
                """
            )
            author_rows = cursor.fetchall()

    except sqlite3.Error as exc:
        print(f"  ✗ Database error: {exc}")
        return

    if not titles:
        print("  No books in the database.")
        return

    author_names = [row[0] for row in author_rows]
    author_countries = [row[1] for row in author_rows]

    for title, name, country in zip(titles, author_names, author_countries):
        print(f"\nTitle: {title}")
        print(f"Author's Name: {name}")
        print(f"Author's Country: {country}")
        print(SEPARATOR)

# Main Menu Section

def display_menu():
    """Print the main menu."""
    print("\n========== Shelf Track ==========")
    print("1. Enter book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Search books")
    print("5. View details of all books")
    print("0. Exit")
    print("=================================")


def main():
    """Initialise the database and run the main menu loop."""
    initialise_database()

    while True:
        display_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            search_books()
        elif choice == "5":
            view_all_book_details()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("  Invalid option. Please enter a number from 0 to 5.")


if __name__ == "__main__":
    main()
