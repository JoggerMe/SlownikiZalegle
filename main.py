import book_functions as bf

def main():
    book = {}
    while True:
        print("\nDostępne opcje:")
        print("1. Dodaj ksiazke")
        print("2. Usun ksiazke")
        print("3. Wyświetl wszystkie książki")
        print("4. Zaktualizuj autora książki")
        print("5. Wyjdź")
        print("-"*70)
        print("Aby wybrac jedna z opcji wpisz przypisany numer")

        choice = input("Wybierz opcję: ")
        print("-"*70)
        if choice == '1':
            title = input("Podaj tytuł książki: ")
            print("-"*70)
            author = input("Podaj autora książki: ")
            print("-"*70)
            bf.add_entry(book, title, author)
            print("-"*70)
        elif choice == '2':
            title = input("Podaj tytuł książki do usunięcia: ")
            print("-"*70)
            bf.remove_entry(book, title)
            print("-"*70)
        elif choice == '3':
            bf.list_entries(book)
            print("-"*70)
        elif choice == '4':
            title = input("Podaj tytuł książki do aktualizacji: ")
            print("-"*70)
            new_author = input("Podaj nowego autora książki: ")
            print("-"*70)
            bf.update_entry(book, title, new_author)
            print("-"*70)
        elif choice == '5':
            print("Zakończenie programu.")
            print("-"*70)
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

if __name__ == "__main__":
    main()