error_message = "\nInvalid input\n Try Again\n"
# Library Book Management


# Function - Input for everything
def input_all(message):
    
    while True:
        print(f"\n\n{message}", end=" ")
        inp = input("-> ").strip()
        if inp:
            return inp
        else:
            print(error_message)

# Function - Input for alphabets
def input_alpha(message):
    
    while True:
        print(f"\nEnter 'stop' to stop\n\n{message}", end=" ")
        inp = input("-> ").strip().lower()
        if inp and inp.isalpha():
            return inp
        else:
            print(error_message)

# Function - Input for alphabets or numbers
def input_alnum(message):
    
    while True:
        print(f"\nEnter 'stop' to stop\n\n{message}", end=" ")
        inp = input("-> ").strip().lower()
        if inp and inp.isalnum():
            return inp
        else:
            print(error_message)

# Function - Input for numbers
def input_num(message):

    while True:
        print(f"\nEnter 0 to stop\n\n{message}", end=" ")
        inp = input("-> ").strip()
        if inp and inp.isdigit():
            return int(inp)
        else:
            print(error_message)

# Function - Input for numbers within a specific range
def input_specific_num(start, ends, message):
    while True:
        print(f"\n\n{message}", end=" ")
        inp = input("-> ").strip()
        if inp and inp.isdigit():
            inp = int(inp)
            if start <= inp <= ends:
                return inp
            else:
                print(f"\nEnter value between [{start} to {ends}]")
        else:
            print(f"\nTry Entering a numeric value between [{start} to {ends}]")

# Function - Input for yes or no
def yes_no(message):
    while True:
        inp = input(f"{message} -> ")
        if inp and inp in "yn":
            match inp:
                case "y": return True
                case "n": return False
        else:
            print("\nEnter either 'y' or 'n' ")

# Function - Formatting
def center_align(message, size, fill, ends):
    print(f"{message.center(size, fill)}", end = ends)

# Essential Dictionaries
library = {}
author = {}
student = {}
library_rec = {}

# Function - Admin Verification with Password
def admin_verification(password):

    # Loop for retry
    while True:
        pw = input_all("Enter Password")
        if pw == password:
            return True
        else:
            print("\nWrong Password")
            proceed = yes_no("Want to Try Again")
            if proceed:
                continue
            else:
                return False

# Function - Add Books in Library
def add_books(record_dict, duplicate_dict, author_dict):

    # Loop for Add books in one go
    while True:
        book = input_all("Name of Book")

        # Condition to stop program
        if book == "stop":
            center_align("Adding Books Stopped", 30, "!", "\n")
            return
        
        # Checks existance of book in library
        if book not in record_dict:
            record_dict[book] = {}

            qty = input_num("Enter Quantity")

            # Condition to stop program
            if qty == 0:
                center_align("Adding Books Stopped", 30, "!", "\n")
                return

            # Adding Details with default Value

            record_dict[book]["Available Quantity"] = qty
            duplicate_dict[book] = {"Available Quantity" : qty}

            author = input_all(f"Author of '{book}'")

            # Condition to stop program
            if author == "stop":
                center_align("Adding Books Stopped", 30, "!", "\n")
                return

            # Check existance of author in author's record
            if author not in author_dict:

                # Adding books wrote by author and assigning default popularity value
                author_dict[author] = {}
                author_dict[author]["Books"] = [book]
                author_dict[author]["Popularity"] = 0
            else:
                author_dict[author]["Books"].append(book)

            # Adding initialized Borrower's list and Popularity of book 
            record_dict[book]["Borrowers"] = {}
            record_dict[book]["Popularity"] = 0

            center_align(f"{book} added", 50, "-", "\n\n")

            # Asks to add more books
            proceed = yes_no("Want to add more books")
            if proceed:
                continue
            else:
                return
            
        else:       # If book already exists
            print(f"{book} already exist in our records")
            proceed = yes_no("Want to add quantity")

            # Asks to add quantity
            if proceed:
                qty = input_num("Enter Quantity")

                if qty == 0:
                    center_align("Adding Books Stopped", 30, "!", "\n")
                    return

                record_dict[book]["Available Quantity"] += qty
                duplicate_dict[book]["Available Quantity"] += qty
                center_align(f"{book} added by {qty}", 50, "-", "\n\n")
            else:
                return

# Function - Add Students in the records of Library
def add_student(student_dict):

    # Loop for adding students in one go
    while True:
        name = input_alpha("Enter Student's Name")

        # Condition to stop program
        if name == "stop":
            print("\nAdding Student Stopped\n")
            return
        
        # Checks existance of name in students record
        if name not in student_dict:

            # Initialising Details with default value
            student_dict[name] = {}
            student_dict[name]["Issues"] = {}
            student_dict[name]["Credit Score"] = 0
            student_dict[name]["Books Issued till now"] = 0
            student_dict[name]["Books Returned Till now"] = 0
            
            # Informing user that name is added
            print("\n")
            center_align(f"{name} added", 50, "-", "\n\n")
            
        else:   # If name already exists in records
            print(f"\n{name} already exists in our records")

            # Asks to add another student
            proceed = yes_no("Want to add another student ?")
            if proceed:
                continue
            else:
                return

# Function - Display - Current Stock
def display_current_books_qty(record_dict):

    # Checks existance of books in Library
    if len(record_dict) != 0:

        # Header
        center_align("=", 82, "=", "|\n")
        center_align("Code", 10, " ", "|")
        center_align("Books", 60, " ", "|")
        center_align("Quantity", 10, " ", "|\n")
        center_align("=", 82, "=", "|\n")

        i = 1

        # Loop for accessing each book of library
        for book in record_dict:
            
            # Stores Quantity of each book
            qty = record_dict[book]["Available Quantity"]

            # Data for Table
            center_align(f"{i}", 10, " ", "|")
            center_align(f"{book}", 60, " ", "|")
            center_align(f"{qty}", 10, " ", "|\n")
            center_align(f"=", 82, "=", "|\n")
            i += 1
    else:   # If there are no books in the library

        # Formatted Message
        center_align("=", 82, "=", "|\n")
        center_align("No Books in the library", 82, " ", "|\n")
        center_align("=", 82, "=", "|\n")

# Function - Display - Current Student's Issues
def display_student_issues(student_dict):

    # Making a temporary copy dictionary of students
    student_dict_copy = student_dict.copy()

    # Checking who have to return books
    for name in student_dict:

        total_issued = student_dict[name]["Books Issued till now"]
        total_returned = student_dict[name]["Books Returned Till now"]
        net_book = total_issued - total_returned
        if net_book == 0:
            del student_dict_copy[name]

    # Checking - If no one is left to return books
    if len(student_dict_copy) == 0:

        # Formatted Message
        center_align("=", 70, "=", "|\n")
        center_align("No Books are left to return", 70, " ", "|\n")
        center_align("=", 70, "=", "|\n")
        return

    # When there are students left to return books
    i = 1

    # Header
    center_align("=", 70, "=", "|\n")
    center_align("Code", 7, " ", "|")
    center_align("Student", 30, " ", "|")
    center_align("Books", 20, " ", "-")
    center_align("Quantity", 10, " ", "|\n")
    center_align("=", 70, "=", "|\n")

    # Data 

    # Accessing Name who are left to return books
    for name in student_dict_copy:
        
        center_align(f"{i}", 7, " ", "|")
        center_align(f"{name}", 30, " ", "|")
        center_align(f" ", 20, " ", " ")
        center_align(f" ", 10, " ", "|\n")

        # Accessing borrowed Books of name
        for book in student_dict_copy[name]["Issues"]:
            qty = student_dict_copy[name]["Issues"][book]

            # Data
            center_align(f" ", 7, " ", "|")
            center_align(f" ", 30, " ", "|")
            center_align(f"{book}", 20, " ", "-")
            center_align(f"{qty}", 10, " ", "|\n")
        center_align("-", 70, "-", "|\n")
        i += 1
    center_align("=", 70, "=", "|\n\n")

# Function - Display - Current Specific Student's Details
def display_specific_student_details(name, student_dict):

    # Header

    center_align("=", 73, "=", "\n")
    center_align("Code", 10, " ", "|")
    center_align("Books", 50, " ", "|")
    center_align("Quantity", 10, " ", "|\n")
    center_align("=", 73, "=", "\n")

    # Checks if the student didn't borrowed any book
    if len(student_dict[name]["Issues"]) == 0:
        center_align("No Books Found", 73, " ", "|\n")
        center_align("=", 73, "=", "\n")

    else:   # When student borrowed books
        i = 1

        # Accessing borrowed books
        for book in student_dict[name]["Issues"]:

            qty = student_dict[name]["Issues"][book]

            # Putting Data into Table
            center_align(f"{i}", 10, " ", "|")
            center_align(f"{book}", 50, " ", "|")
            center_align(f"{qty}", 10, " ", "|\n")
            center_align("=", 73, "=", "\n")

            i += 1
    center_align("=", 73, "=", "\n\n")
    
    issued = student_dict[name]["Books Issued till now"]
    returned = student_dict[name]["Books Returned Till now"]
    credit = student_dict[name]["Credit Score"]

    center_align("=", 63, "=", "\n")
    center_align("Books Issued", 20, " ", "|")
    center_align("Books Returned", 20, " ", "|")
    center_align("Credit Score", 20, " ", "|\n")
    center_align("=", 63, "=", "\n")

    center_align(f"{issued}", 20, " ", "|")
    center_align(f"{returned}", 20, " ", "|")
    center_align(f"{credit}", 20, " ", "|\n")
    center_align("=", 63, "=", "\n")

# Function - Issue Book
def book_issue(record_dict, student_dict, author_dict):

    # Loop for Issue books in one go
    while True:
        name = input_alpha("Enter name of Student")

        # Condition to stop program
        if name == "stop":
            center_align("Book Issue Stopped", 30, "!", "\n")
            return

        # Checks Existance of name in students record
        if name in student_dict:
            credit = student_dict[name]["Credit Score"]                     # Stores credit score of that student
            books_borrowed = student_dict[name]["Books Issued till now"]    # Stores No. of books issued till now

            # Condition for issuing the book
            if credit >= 5 or books_borrowed <=5:
                
                # Display Current Stock of Library
                display_current_books_qty(record_dict)

                # Takes input for book
                book_index = input_specific_num(0, len(record_dict), "Enter 0 to stop\n\nEnter code of book")

                # Condition to stop program
                if book_index == 0:
                    center_align("Book Issue Stopped", 30, "!", "\n")
                    return

                book = list(record_dict.keys())[book_index-1]

                # Accessing Author name from author record
                for author_name in author_dict:
                    # Accessing books written by author
                    for book_1 in author_dict[author_name]["Books"]:

                        # Matching issued book and author book
                        if book == book_1:
                            author = author_name
                            break
                
                # Stores available quantity of desired book
                available_qty = record_dict[book]["Available Quantity"]

                # Checks availability of book
                if available_qty != 0:
                    
                    # Loop if desired quantity don't match with availability
                    while True:
                        qty = input_num("Enter Quantity")

                        # Condition to stop program
                        if qty == 0:
                            center_align("Book Issue Stopped", 30, "!", "\n")
                            return
                        
                        # Desired quantity > availability
                        if qty <= available_qty:

                            # Checks if the issuer first time issuing this book
                            if book not in student_dict[name]["Issues"] and name not in record_dict[book]["Borrowers"]:
                                
                                # Updating details of library amd student
                                record_dict[book]["Borrowers"][name] = qty
                                record_dict[book]
                                student_dict[name]["Issues"][book] = qty
                            else:   # if the issuer already have that book
                                
                                # Updating Details
                                record_dict[book]["Borrowers"][name] += qty
                                student_dict[name]["Issues"][book] += qty
                            

                            # Upadting Other details for library and student and author

                            record_dict[book]["Available Quantity"] -= qty
                            record_dict[book]["Popularity"] += qty

                            student_dict[name]["Books Issued till now"] += qty
                            total_issue = student_dict[name]["Books Issued till now"] 
                            total_return = student_dict[name]["Books Returned Till now"] 
                            student_dict[name]["Credit Score"] = (total_return/total_issue) * 10

                            author_dict[author]["Popularity"] += qty

                            center_align(f"{book} issued to {name} Succesfully", 50, "-", "\n\n")
                            break

                        else:   # Quantity > availability
                            print(f"\nQuantity Not Availbale\n{available_qty} units are available only\n")
                            
                            # Asks to add quantity
                            proceed = yes_no("Want to issue under the limit ?")
                            if proceed:
                                continue
                            else:
                                center_align(f"Issue of {book} Failed, because {name} wants more quantity than available", 100, "-", "\n\n")
                                break

                    # Asks to add issue more books
                    proceed = yes_no("Want to Issue Another Book ?")
                    if proceed:
                        continue
                    else:
                        return
                else:   # If Book is not available in Library
                    print(f"{book} not available for this time\nCome Later\n\n")
                    return
                
            else:   # when user is not eligilble to issue book
                print(f"\n{name} is not eligible to issue more books\nFirst return the books you have previosuly issued.\n\n")
                return
        else:   # if name is not in students record
            print(f"\n{name} not in our records\nFirst add he name in our records, then handover the book\n\n")

# Function - return Book
def book_return(record_dict, student_dict):

    # Asks Information
    name = input_alpha("Enter name of Student")
    book_issued_dict = student[name]["Issues"]

    # Condition to Stops the program
    if name == "stop":
        center_align("Returning Stopped", 30, "!", "\n")
        return
    
    # Checks existance of student in records
    if name in student_dict:
        total_issued = student_dict[name]["Books Issued till now"]
        total_returned = student_dict[name]["Books Returned Till now"]
        net_book = total_issued - total_returned

        # Checks any book is left to return
        if net_book != 0:

            # Displays student's all details
            display_specific_student_details(name, student_dict)

            # Asks book to return
            book_index = input_specific_num(0, len(book_issued_dict), "Enter 0 to stop\n\nBook Code")

            # Condition to Stops the program
            if book_index == 0:
                center_align("Returning Stopped", 30, "!", "\n")
                return

            book = list(book_issued_dict.keys())[book_index-1]

            # Asks quantity to return
            qty = input_specific_num(0, book_issued_dict[book], "Enter 0 to stop\n\nEnter Quantity")

            # Condition to Stops the program
            if qty == 0:
                center_align("Returning Stopped", 30, "!", "\n")
                return

            # Updating Details

            record_dict[book]["Borrowers"][name] -= qty

            # Deletes borrower's name from the borrowed list of that book, if the student returned all units of that book
            if record_dict[book]["Borrowers"][name] == 0:
                del record_dict[book]["Borrowers"][name]

            student_dict[name]["Issues"][book] -= qty

            # Deletes boook's name from the issued list of that student, if the student returned all units of that book
            if student_dict[name]["Issues"][book] == 0:
                del student_dict[name]["Issues"][book]

            # Updating additional detials

            student_dict[name]["Books Returned Till now"] += qty
            total_issued = student_dict[name]["Books Issued till now"]
            total_returned = student_dict[name]["Books Returned Till now"]

            student_dict[name]["Credit Score"] = (total_returned/total_issued) * 10
            record_dict[book]["Available Quantity"] += qty
        else:   # when student left no books to return 
            print(f"{name} has no books left to return\nThankyou {name}\n")

# Function - Display - Total Inflow of booksin Library
def display_all_books_inflow(duplicate_dict):

    # Checks inflow of books from the starting of the programm
    if len(duplicate_dict) != 0:

        # Header
        center_align(f"=", 72, "=", "|\n")
        center_align("Code", 10, " ", "|")
        center_align("Books", 50, " ", "|")
        center_align("Quantity", 10, " ", "|\n")
        center_align("=", 72, "=", "|\n")

        i = 1

        # Accessing book
        for book in duplicate_dict:

            # Stores Quantity of book
            qty = duplicate_dict[book]["Available Quantity"]

            # Formatted Data 
            center_align(f"{i}", 10, " ", "|")
            center_align(f"{book}", 50, " ", "|")
            center_align(f"{qty}", 10, " ", "|\n")
            center_align(f"=", 72, "=", "|\n")
            i += 1
    else:   # If didn't added books from starting
        center_align("=", 82, "=", "|\n")
        center_align("No Books in the library", 82, " ", "|\n")
        center_align("=", 82, "=", "|\n")

# Function - Display - Popularity of Books
def display_popularity_books(record_dict):

    # Initialising Required things
    most_popularity = 0
    top_book = []

    # Accessing book to find most popularity index
    for book in record_dict:
        popularity = record_dict[book]["Popularity"]
        if most_popularity <= popularity:
            most_popularity = popularity
    
    # Accessing book to Add Books with Most popularity index
    for book in record_dict:
        if most_popularity == record_dict[book]["Popularity"]:
            top_book.append(book)
    
    center_align("=", 100, "=", "|\n")
    
    # When There are more 1st position holder
    if len(top_book) != 1:
        center_align(f"Highest Popularity Index is {most_popularity}", 100, " ", "|\n")
        center_align("-", 100, "-", "|\n")
        center_align(f"Acheivers", 100, " ", "|\n")
        center_align("=", 100, "=", "|\n")
        for book in top_book:
            center_align(f"{book}", 100, " ", "|\n")
            center_align("-", 100, "-", "|\n")

    else:   # Only one popular book
        center_align(f"' {top_book[0]} ' is the Most Popular Book", 100, " ", "|\n")
    center_align("=", 100, "=", "|\n")

    # Displays Every Book's Popularity

    # Header
    center_align("=", 121, "=", "|\n")
    center_align(f"Name of Books", 100, " ", "|")
    center_align(f"Popularity", 20, " ", "|\n")
    center_align("=", 121, "=", "|\n")

    # Accessing Popularity and name of book of library
    for book in record_dict:
        popularity = record_dict[book]["Popularity"]

        # Formatted data
        center_align(f"{book}", 100, " ", "|")
        center_align(f"{popularity}", 20, " ", "|\n")
        center_align("-", 100, "-", "|")
        center_align("-", 20, "-", "|\n")
    center_align("=", 121, "=", "|\n")

# Function - Display - Popularity of Authors
def display_popularity_author(author_dict):
    most_popularity = 0
    top_author = []

    # Accessing author to find most popularity index
    for author in author_dict:
        popularity = author_dict[author]["Popularity"]
        if most_popularity <= popularity:
            most_popularity = popularity
    
    # Accessing author to Add authors with Most popularity index
    for author in author_dict:
        if most_popularity == author_dict[author]["Popularity"]:
            top_author.append(author)
    
    center_align("=", 100, "=", "|\n")
    
    # When There are more than one 1st position holder
    if len(top_author) != 1:
        center_align(f"Highest Popularity Index is {most_popularity}", 100, " ", "|\n")
        center_align("-", 100, "-", "|\n")
        center_align(f"Acheivers", 100, " ", "|\n")
        center_align("=", 100, "=", "|\n")
        for author in top_author:
            center_align(f"{author}", 100, " ", "|\n")
            center_align("-", 100, "-", "|\n")

    else:   # Only one popular author
        center_align(f"' {top_author[0]} ' is the Most Popular Author", 100, " ", "|\n")
    center_align("=", 100, "=", "|\n")

    # Displays Every Author's Popularity

    # Header
    center_align("=", 121, "=", "|\n")
    center_align(f"Name of Author", 100, " ", "|")
    center_align(f"Popularity", 20, " ", "|\n")
    center_align("=", 121, "=", "|\n")

    # Accessing Popularity and name of author 
    for author in author_dict:
        popularity = author_dict[author]["Popularity"]

        # Formatted data
        center_align(f"{author}", 100, " ", "|")
        center_align(f"{popularity}", 20, " ", "|\n")
        center_align("-", 100, "-", "|")
        center_align("-", 20, "-", "|\n")
    center_align("=", 121, "=", "|\n")

# Function - Display - Top Credit Scores of Students
def display_credit_score(student_dict):

    # Temporary Containers
    credit_dict = {}
    credit_list = []

    # Extracting Credit score of each student and importing in credit dict
    for name in student_dict:
        credit_dict[name] = student_dict[name]["Credit Score"]
    
    # Taking highest credit score
    max_credit = max(list(credit_dict.values()))
    credit_dict_copy = credit_dict.copy()

    length = len(credit_dict_copy)

    # loop for accessing every element of credit dict
    while length > 0:

        # Accessing name in copied credit dict
        for name in credit_dict_copy:
            credit = credit_dict[name]

            # Matching with highest credit score
            if credit == max_credit:
                credit_list.append(name)
                break
        
        # Deleting from copied credit dict for prevention of checking the same students credit
        del credit_dict_copy[name]
        length -= 1

    center_align("=", 60, "=", "|\n")
    
    # If there is one with highest credit score
    if len(credit_list) == 1:
        for name in credit_list:

            # Formatted data
            center_align("Most Credit Score", 60, " ", "|\n")
            center_align("=", 60, "=", "|\n")
            center_align(f"{name.capitalize()} is having the highest Credit Score : {max_credit:.2f}", 60, " ", "|\n")
    else:   # Many with highest score

        # Header
        center_align(f"Highest Credit Score amongst student : {max_credit}", 60, " ", "|\n")
        center_align("=", 60, "=", "|\n")
        center_align("Acheivers", 60, " ", "|\n")
        center_align("=", 60, "=", "|\n")

        for name in credit_list:

            # Formatted data
            center_align(f"{name}", 60, " ", "|\n")
            center_align("-", 60, "-", "|\n")

    center_align("=", 60, "=", "|\n\n")

# Function - Display - All students Credit Score
def display_total_credit_score(student_dict):

    # Header
    center_align("=", 71, "=", "|\n")
    center_align("Student Name", 50, " ", "|")
    center_align("Credit Score", 20, " ", "|\n")
    center_align("=", 71, "=", "|\n")

    # Formatted Data
    for name in student_dict:
        center_align(f"{name}", 50, " ", "|")
        center_align(f"{student_dict[name]["Credit Score"]}", 20, " ", "|\n")
        center_align("-", 71, "-", "|\n")
    center_align("=", 71, "=", "|\n")

# Function - Display - Borrowers of specific Book
def display_specific_books_borrower(book, record_dict):

    # Header
    center_align("=", 66, "=", "|\n")
    center_align(f"Borrowers of {book}", 50, " ", "|")
    center_align("Quantity", 15, " ", "|\n")
    center_align("=", 66, "=", "|\n")

    # Checks existance of borrower
    if len(record_dict[book]["Borrowers"]) == 0:
        center_align(f"No Borrowers of ' {book} ' found", 66, " ", "|\n")
    else:   # When there are borrowers
        for name in record_dict[book]["Borrowers"]:

            qty = record_dict[book]["Borrowers"][name]
            
            # Formatted data
            center_align(f"{name}", 50, " ", "|")
            center_align(f"{qty}", 15, " ", "|\n")
    center_align("=", 66, "=", "|\n")

# Function - Delete A stock from Library
def delete_stock(record_dict):

    # Takes Name of book
    book = input_all("Enter 'stop' to stop\n\nEnter Book Name")

    # Checks to stop the program
    if book == "stop":
        print("!! Deletion Stopped !!")
    
    # Checks existance of book in library
    if book in record_dict:
        
        # Checks existance of borrowers
        if len(record_dict[book]["Borrowers"]) == 0:
            del record_dict[book]
        else:   # If Borrowers are there 
            print("\nFirst take back the borrowed books from these students and remove the stock\n")
            display_specific_books_borrower(book, record_dict)      # Displayes borrowers with quantity
    else:
        print(f"\n{book} is not in the library\n")

# Function - Display - Features
def display_tasks(number):

    # Tasks list
    task = ["Stop the Program", "Add Books", "Current Stock", "Total Inflow of Books in Library", "Add Students", "Delete Stock",
            "Issue Book", "Return Book", "Student Current Issue Record", "Individual Student Current record", "Popular Book",
            "Popular Author", "Top Credit Score of Students", "Particular Book's Issuer List", "All Student Credit Score"]
    i = 0

    # Header
    print("\n\n")
    center_align("=", 76, "=", "|\n")
    center_align("Task No.", 15, " ", "|")
    center_align("Tasks", 60, " ", "|\n")
    center_align("=", 76, "=", "|\n")

    while i < number:

        # Formatted Data
        center_align(f"{i}", 15, " ", "|")
        center_align(f"{task[i]}", 60, " ", "|\n")
        center_align("-", 76, "-", "|\n")
        i += 1
    center_align("=", 76, "=", "|\n")

# Function - Evaluate Situations of presenting features accordingly
def conditions_check(record_dict, student_dict):

    # Checks Stock in library
    if len(record_dict) != 0:
        
        # Checks Student's record
        if len(student_dict) != 0:

            for book in record_dict:

                # Checks Popularity of books
                if record_dict[book]["Popularity"] != 0:
                    condition = 5
                    break
                else:   # When No issues happens
                    condition = 4
                    continue
        else:   # When No students have added
            condition = 3
    else:   # When no books in library
        condition = 2
    
    return condition

# Function - Condition 2
def condition_2(record_dict, duplicate_dict, author_dict):

    # Displays Taks based on condition
    display_tasks(4)

    # Asks the task
    task = input_specific_num(0, 3, "Enter Task")

    # Matching the task
    match task:
        case 1: add_books(record_dict, duplicate_dict, author_dict)
        case 2: display_current_books_qty(record_dict)
        case 3: display_all_books_inflow(duplicate_dict)
        case 0: return 0

# Function - Condition 3
def condition_3(record_dict, student_dict, duplicate_dict, author_dict):

    # Displays Taks based on condition
    display_tasks(5)

    # Asks the task
    task = input_specific_num(0, 6, "Enter Task")

    # Matching the task
    match task:
        case 1: add_books(record_dict, duplicate_dict, author_dict)
        case 2: display_current_books_qty(record_dict)
        case 3: display_all_books_inflow(duplicate_dict)
        case 4: add_student(student_dict)
        case 5: delete_stock(record_dict)
        case 0: return 0

# Function - Condition 4
def condition_4(record_dict, student_dict, duplicate_dict, author_dict):

    # Displays Taks based on condition
    display_tasks(7)

    # Asks the task
    task = input_specific_num(0, 6, "Enter Task")

    # Matching the task
    match task:
        case 1: add_books(record_dict, duplicate_dict, author_dict)
        case 2: display_current_books_qty(record_dict)
        case 3: display_all_books_inflow(duplicate_dict)
        case 4: add_student(student_dict)
        case 5: delete_stock(record_dict)
        case 6: book_issue(record_dict, student_dict, author_dict)
        case 0: return 0

# Function - Condition 5
def condition_5(record_dict, student_dict, duplicate_dict, author_dict):

    # Displays Taks based on condition
    display_tasks(15)

    # Asks the task
    task = input_specific_num(0, 14, "Enter Task")

    # Displays Taks based on condition
    match task:
        case 1: add_books(record_dict, duplicate_dict, author_dict)
        case 2: display_current_books_qty(record_dict)
        case 3: display_all_books_inflow(duplicate_dict)
        case 4: add_student(student_dict)
        case 5: delete_stock(record_dict)
        case 6: book_issue(record_dict, student_dict, author_dict)  
        case 7: book_return(record_dict, student_dict)
        case 8: display_student_issues(student_dict)
        case 9: 
            name = input_alpha("\nEnter Student's Name")
            if name in student_dict:
                display_specific_student_details(name, student_dict)
            else:
                print(f"\n{name} is not in our records\n")
        case 10: display_popularity_books(record_dict)
        case 11: display_popularity_author(author_dict)
        case 12: display_credit_score(student_dict)
        case 13: 
            book = input_all("\nEnter name of student")
            if book in record_dict:
                display_specific_books_borrower(book, record_dict)
            else:
                print(f"\n' {book} ' Book is not available in the library")
        case 14: display_total_credit_score(student_dict)
        case 0: return 0

# Function - Full Program
def library_management(record_dict, student_dict, duplicate_dict, author_dict):

    # welcoming Line
    print("\n\n")
    center_align(" Welcome To Library Management Programme ", 100, "*", "\n\n")

    # Loop for asking tasks
    while True:

        # Admin verification
        verify = admin_verification("Admin@1234")

        # checks if the password is correct
        if verify:
            while True:

                # Checks the suitable condition
                condition = conditions_check(record_dict, student_dict)

                # Match it woth the current scenario
                match condition:
                    case 2: 
                        two = condition_2(record_dict, duplicate_dict, author_dict)
                        if two == 0:
                            print("\nProgram Stoped\n")
                            return
                        else:
                            continue

                    case 3: 
                        three = condition_3(record_dict, student_dict, duplicate_dict, author_dict)
                        if three == 0:
                            print("\nProgram Stoped\n")
                            return
                        else:
                            continue

                    case 4: 
                        four = condition_4(record_dict, student_dict, duplicate_dict, author_dict)
                        if four == 0:
                            print("\nProgram Stoped\n")
                            return
                        else:
                            continue

                    case 5: 
                        five = condition_5(record_dict, student_dict, duplicate_dict, author_dict)
                        if five == 0:
                            print("\nProgram Stoped\nGood Bye!!")
                            return
                        else:
                            continue
        else:   
            # If password is wrong
            proceed = yes_no("Want to Try Again ?")
            if proceed:
                continue
            else:
                print("\nProgram Stoped because admin can't remeber the password\n")
                return
    
library_management(library, student, library_rec, author)
