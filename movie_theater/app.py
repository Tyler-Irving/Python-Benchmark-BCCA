import json

MOVIES_FILENAME = "/Users/student/code/python_benchmark/movie_theater/movies.json"
TRANSACTIONS_FILENAME = (
    "/Users/student/code/python_benchmark/movie_theater/transactions.txt"
)


MATINEE_TICKET_PRICE = 3.50
REGULAR_TICKET_PRICE = 5.25


def load_file(filename):
    with open(filename) as movie_file:
        movies = json.load(movie_file)
    return movies.get("movies")


def get_movie_choice(movies):
    for key in movies:
        print(key)
    while True:
        choice = input("Pick a movie: ")
        if choice not in movies:
            print("sorry, we don't have that movie")
        else:
            print("Excellent choice!")
            return movies[choice], movies[choice]["title"]


def ticket_price(string):
    time, am_pm = string.split()
    hour, minute = time.split(":")
    if am_pm == "AM" or int(hour) in {12, 1, 2, 3}:
        return MATINEE_TICKET_PRICE, "matinee"
    else:
        return REGULAR_TICKET_PRICE, "regular"


def get_showtime(movie):
    showtimes = movie.get("showtimes")
    for i in range(len(showtimes)):
        print("Option", i + 1, "at", showtimes[i])
    while True:
        showtime_input_index = input("What option would you like to go to: ").strip()
        if (
            showtime_input_index.isdigit()
            and int(showtime_input_index) >= 1
            and int(showtime_input_index) <= len(showtimes)
        ):
            showtime = showtimes[int(showtime_input_index) - 1]
            return showtime


def get_tickets():
    return int(input("How many tickets would you like: "))


def get_all_data(movie_title, showtime, type_of_show, tickets, total_price):
    return f"\n{movie_title}, {showtime}, {type_of_show}, {tickets}, {total_price}"


def transfer_data(filename, all_data):
    with open(filename, "a") as money_file:
        money_file.write(all_data)


def movie_theater():
    print("Welcome to the movies!")
    movies = load_file(MOVIES_FILENAME)
    movie_choice, movie_title = get_movie_choice(movies)
    showtime = get_showtime(movie_choice)
    tickets = get_tickets()
    price, type_of_show = ticket_price(showtime)
    total_transaction = tickets * price
    total_price = f"{total_transaction:.2f}"
    print(f"""okay, that will be {total_price} \nEnjoy the show! """)
    all_data = get_all_data(movie_title, showtime, type_of_show, tickets, total_price)
    transfer_data(TRANSACTIONS_FILENAME, all_data)


if __name__ == "__main__":
    movie_theater()
