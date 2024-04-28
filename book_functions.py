def add_entry(book, title, author):
    """Dodaj książkę do słownika."""
    book[title] = author
    print(f"Dodano książkę: {title} autorstwa {author}.")

def remove_entry(book, title):
    """Usuń książkę ze słownika, jeśli istnieje."""
    if title in book:
        del book[title]
        print(f"Usunięto książkę: {title}.")
    else:
        print("Książka nie została znaleziona.")

def list_entries(book):
    """Wyświetl wszystkie książki w słowniku."""
    if not book:
        print("Biblioteka jest pusta.")
    else:
        for title, author in book.items():
            print(f"{title} autorstwa {author}")

def update_entry(book, title, new_author):
    """Zaktualizuj autora książki w słowniku."""
    if title in book:
        book[title] = new_author
        print(f"Zaktualizowano książkę: {title}, nowy autor: {new_author}.")
    else:
        print("Książka nie została znaleziona.")