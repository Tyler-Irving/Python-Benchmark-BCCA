import json
from datetime import datetime

BOOK_FILENAME = "/Users/student/code/python_benchmark/library/books.json"
LOG_FILENAME = "/Users/student/code/python_benchmark/library/log.txt"


def get_books(BOOK_FILENAME):
    with open(BOOK_FILENAME) as fiile:
        books = json.load(fiile)
    return books["books"]["PR6039.O32"]


def print_books(collection):
    print("Our books:")
    for element in collection:
        book_info = element.values()
        for info in book_info:
            print(f'{info["title"]} |In-stock: {info["in-stock"]}|')


def choose_book(collection):
    new_list = []
    for book in collection:
        info = book.values()
        for title in info:
            new_list.append([title["title"], title["in-stock"], book.keys()])
    print("Which one would you like?")
    choice = input(">>> ")
    for items in new_list:
        if choice == items[0] and items[1] == True:
            number = str(items[2])
            print("Excellent Choice")
            return choice, number[12:15]
    print("Sorry, that is not an option.")


def update_checkin(collection, choice, num):
    for element in collection:
        for thing in element.values():
            if choice == thing["title"]:
                print(thing)
                ya = thing["in-stock"] = False
                with open(BOOK_FILENAME, "a") as book_file:
                    json.dump(False, book_file)


def check_out(choice, number, now):
    with open(LOG_FILENAME, "a") as file:
        file.write(f"\n{now},PR6039.O32 {number}, CHECK OUT, {choice}")


def choose_checkin(collection):
    new_list = []
    for book in collection:
        info = book.values()
        for title in info:
            new_list.append([title["title"], title["in-stock"], book.keys()])
    print("Which one would you like?")
    choice = input(">>> ")
    for items in new_list:
        if choice == items[0] and items[1] == False:
            number = str(items[2])
            print("Excellent Choice")
            return choice, number[12:15]
    print("Sorry, that is not an option.")


def check_in(choice, number, now):
    with open(LOG_FILENAME, "a") as file:
        file.write(f"\n{now},PR6039.O32 {number}, CHECK IN, {choice}")


def main():
    now = datetime.now()
    print("welcome to the middle-earth public library.".title())
    while True:
        action = input("Check in / Check out / Leave? [I/O/L]:")
        if action == "O":
            books = get_books(BOOK_FILENAME)
            print_books(books)
            choice, number = choose_book(books)
            update_checkin(books, choice, number)
            check_out(choice, number, now)
        elif action == "I":
            books = get_books(BOOK_FILENAME)
            print_books(books)
            choice, number = choose_checkin(books)
            check_in(choice, number, now)
            pass
        elif action == "L":
            print("Have a nice day!")
            break
        else:
            print("That is not an option.")


if __name__ == "__main__":
    main()
