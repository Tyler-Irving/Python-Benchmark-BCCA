from datetime import datetime
import json

# additional imports if needed

# global variables
SHOWS_FILE = "concert_tickets/shows.json"
TRANSACTIONS_FILE = "concert_tickets/transactions.txt"
TICKET_FILE = "concert_tickets/ticket.txt"
SALES_TAX = 0.07  # 7% Sales Tax


def tickets_json():
    with open(SHOWS_FILE) as shows:
        return json.load(shows)


def show_concert(collection):
    for element in collection:
        print(
            f"Main Artist: {element.get('artist')} | Opening Artist: {element.get('opener')} ||| Tickets: {element.get('tickets')}"
        )


def pick_show(collection):
    name = input("Name: ").title()
    print("Use the main artists name for the show!")
    while True:
        choice = input(">>> ").title()
        for element in collection:
            if choice == element.get("artist") and element.get("tickets") != "SOLD OUT":
                return (
                    element.get("price"),
                    choice,
                    name,
                    element.get("code"),
                    element.get("opener"),
                    element.get("date"),
                    element.get("doors"),
                    element.get("show"),
                )


def final_transactions(choice, price, collection):
    print(f"Price per ticket: ${price:.2f}")
    print("How many would you like? You may only buy 4!")
    while True:
        tickets_sold = int(input(">>> "))
        purchase_amount = price * tickets_sold
        tax = purchase_amount * SALES_TAX
        for element in collection:
            if choice == element.get("artist") and tickets_sold <= 4:
                available_tickets = element.get("tickets") - tickets_sold
                return purchase_amount, tickets_sold, tax, available_tickets
            elif tickets_sold > 4:
                print("Exceeds ticket purchasing limit")
                break


def make_transaction_line(name, show, code, tickets, price, tax, timestamp):
    return "\n{}, {}, {}, {}, {:.2f}, {:.2f} {}".format(
        name, show, code, tickets, price, tax, timestamp
    )


def save_transactions(file_line):
    with open(TRANSACTIONS_FILE, "a") as file:
        file.write(file_line)


def update_json(choice, available_tickets):
    with open(SHOWS_FILE) as shows:
        concerts = json.load(shows)
    for idx, val in enumerate(concerts):
        if choice == val.get("artist"):
            concerts[idx]["tickets"] = int(available_tickets)
            with open(SHOWS_FILE, "w") as shows:
                json.dump(concerts, shows)


def update_ticket(choice, opener, date, doors, show, code, tickets_sold):
    ticket = f"""\n
==================================================
]                 THE JEFFERSON                  [
]                  featuring...                  [
]                                                [
                 ]  {choice}[
]                with {opener}                   [
]                {date}                      [
]           Doors: {doors}, Show: {show}          [
]                                                [
]       Admit: {tickets_sold}, Code: {code}               [
==================================================
"""
    with open(TICKET_FILE, "a") as file:
        file.write(ticket)


def main():
    print("Welcome to The Jefferson venue ticket purchasing tool!")
    print(
        """Only 4 tickets per person, unless show is sold out.
    What show would you like to see?"""
    )
    tickets = tickets_json()
    timestamp = datetime.now()
    show_concert(tickets)
    print()
    price, choice, name, code, opener, date, doors, show = pick_show(tickets)
    purchase_amount, tickets_sold, tax, available_tickets = final_transactions(
        choice, price, tickets
    )
    transaction_line = make_transaction_line(
        name, choice, code, tickets_sold, purchase_amount, tax, timestamp
    )
    save_transactions(transaction_line)
    update_json(choice, available_tickets)
    update_ticket(choice, opener, date, doors, show, code, tickets_sold)


if __name__ == "__main__":
    main()
