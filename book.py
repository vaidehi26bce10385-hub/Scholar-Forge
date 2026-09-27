books=[]
def book_menu():
    while True:
        print("BOOK TRACKER")
        print('''
        1. Add Book
        2. View Books
        3. Change Reading Status
        4. Book Recommendations
        5. Reading Statistics
        6. Delete Book
        7. Exit ''')

        opt_3=int(input("Enter your choice: "))

        if opt_3==1:
            title=input("Book title: ")
            author=input("Author: ")
            genre=input("Genre: ")
            book = {
                "Title": title,
                "Author": author,
                "Genre": genre,
                "Status": "Want to Read"
            }
            books.append(book)
            print("Book has been added.")

        elif opt_3==2:
            if len(books)==0:
                print("No books available.")

            else:
                for i, book in enumerate(books, start=1):
                    print("Book Number: ", i)
                    print("Title: ", book["Title"])
                    print("Author: ", book["Author"])
                    print("Genre: ", book["Genre"])
                    print("Status: ", book["Status"])

        elif opt_3==3:
            if len(books)==0:
                print("No books available.")

            else:
                for i, book in enumerate(books, start=1):
                    print(i, book["Title"])

                num=int(input("Enter book number: "))

                if 1<=num<=len(books):
                    print('''
                    1. Want to Read
                    2. Reading
                    3. Completed
                    ''')
                    status=int(input("Enter status: "))
                    if status==1:
                        books[num - 1]["Status"]="Want to Read"

                    elif status == 2:
                        books[num - 1]["Status"]="Reading"

                    elif status == 3:
                        books[num - 1]["Status"]="Completed"

                    else:
                        print("Invalid status.")
                        continue
                    print("Reading status updated.")

                else:
                    print("Invalid Book Number.")

        elif opt_3==4:
            if len(books) == 0:
               print("No books available.")

            else:
                genre=input("Enter genre: ")
                genre=genre.lower()
                found=False
                for book in books:
                    if book["Genre"].lower()==genre:
                        print(book["Title"])
                        print("Author: ", book["Author"])
                        print("Status: ", book["Status"])
                        found=True

                if found==False:
                    print("No books found for this genre.")

        elif opt_3==5:
            comp=0
            read=0
            want_to_read=0
            for book in books:
                if book["Status"] == "Completed":
                    comp+=1

                elif book["Status"] == "Reading":
                    read+=1

                else:
                    want_to_read+=1

            print("Total Books: ", len(books))
            print("Completed: ", comp)
            print("Currently Reading: ", read)
            print("Want to Read: ", want_to_read)

        elif opt_3==6:
            if len(books)==0:
                print("No books available.")

            else:
                for i, book in enumerate(books, start=1):
                    print(i, book["Title"])

                num=int(input("Enter book number to delete: "))

                if 1<=num<=len(books):
                    dele=books.pop(num-1)
                    print(dele["Title"], " has been deleted.")

                else:
                    print("Invalid Book Number.")

        elif opt_3==7:
            break

        else:
            print("Invalid choice.")