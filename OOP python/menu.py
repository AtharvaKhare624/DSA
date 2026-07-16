book = {
    "asd": {"author":"QWE", "page_no":120},
    "q": {"author":"xcv", "page_no":1220},
    "pl": {"author":"jhg", "page_no":20},
    "ujk": {"author":"ijn", "page_no":1265}
}
movies = {
    "qws": {"hours":3, "actor_name":"r"},
    "mn": {"hours":2, "actor_name":"rs"},
    "t": {"hours":3, "actor_name":"rx"}
}

while True:
    print("\n menu \n")
    print("1. add book")
    print("2. remove book")
    print("3. add movie")
    print("4. remove movie")
    print("5. update page numbers")
    print("6. update hours")
    print("7. display")
    print("8. Exit")

    choice = int(input("enter yoor choice:"))
    if choice == 1:
        name = input("Enter book name: ")
        author = input("Enter author name: ")
        pages = int(input("Enter page number: "))
        book[name] = {"author": author, "page_no": pages}
        print("Book added successfully!")

    
    elif choice == 2:
        name = input("Enter book name to remove: ")
        if name in book:
            del book[name]
            print("Book removed!")
        else:
            print("Book not found.")

    
    elif choice == 3:
        name = input("Enter movie name: ")
        hours = int(input("Enter duration (hours): "))
        actor = input("Enter actor name: ")
        movies[name] = {"hours": hours, "actor_name": actor}
        print("Movie added successfully!")

    
    elif choice == 4:
        name = input("Enter movie name to remove: ")
        if name in movies:
            del movies[name]
            print("Movie removed!")
        else:
            print("Movie not found.")

    
    elif choice == 5:
        name = input("Enter book name: ")
        if name in book:
            pages = int(input("Enter new page number: "))
            book[name]["page_no"] = pages
            print("Page number updated!")
        else:
            print("Book not found.")

    
    elif choice == 6:
        name = input("Enter movie name: ")
        if name in movies:
            hours = int(input("Enter new hours: "))
            movies[name]["hours"] = hours
            print("Movie hours updated!")
        else:
            print("Movie not found.")

    elif choice == 7:
        print("\nBooks:")
        for k, v in book.items():
            print(f"{k} → Author: {v['author']}, Pages: {v['page_no']}")

        print("\nMovies:")
        for k, v in movies.items():
            print(f"{k} → Actor: {v['actor_name']}, Hours: {v['hours']}")


    
    elif choice == 8:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")

#word freq 
s = input("enter sentence: ")
words = s.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
for word, count in freq.items():
    print(f"the frequency of '{word}' is : {count}")
