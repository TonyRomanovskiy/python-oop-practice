"""Demo of the Library."""

from library import (
    Book, Library,
    BookNotFoundError,
    BookAlreadyExistsError,
    BookNotAvailableError,
)


def main():
    # Создание из CSV
    lib = Library.from_csv("Война и мир,Толстой,1869;1984,Оруэлл,1949")
    print(f"Книг: {len(lib)}")
    print(f"Доступных: {lib.available_count}")
    print(lib)

    # Выдача книги
    lib.borrow_book("1984")
    print(f"Доступных после выдачи: {lib.available_count}")

    # Итерация
    for book in lib:
        print(book.title)

    # to_dict
    print(lib.to_dict())

    # Обработка ошибок
    try:
        lib.add_book(Book("1984", "Оруэлл", 1949))
    except BookAlreadyExistsError as e:
        print(f"Ошибка: {e}")

    try:
        lib.borrow_book("1984")
    except BookNotAvailableError as e:
        print(f"Ошибка: {e}")

    try:
        lib.remove_book("Несуществующая")
    except BookNotFoundError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()