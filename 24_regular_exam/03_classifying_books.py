def classify_books(*args, **kwargs):
    fiction_books = {}
    non_fiction_books = {}

    for genre, title in args:
        for isbn, book_title in kwargs.items():
            if book_title == title:
                if genre == "fiction":
                    fiction_books[isbn] = title
                elif genre == "non_fiction":
                    non_fiction_books[isbn] = title
                break

    output = []

    if fiction_books:
        output.append("Fiction Books:")
        for isbn in sorted(fiction_books):
            output.append(f"~~~{isbn}#{fiction_books[isbn]}")

    if non_fiction_books:
        output.append("Non-Fiction Books:")
        for isbn in sorted(non_fiction_books, reverse=True):
            output.append(f"***{isbn}#{non_fiction_books[isbn]}")

    return "\n".join(output)
