import json
from random import choice as randchoice

DONUT_FILENAME = "./donuts.json"
TRANSACTION_FILENAME = "./transactions.txt"


def open_donut_file(filename):
    """ str filename -> list str toppings, list str flavors
    opens the json file and loads the object
    returns the lists from the object """
    with open(filename, "r") as file:
        donut_dictionary = json.load(file)

    toppings = donut_dictionary.get("toppings")
    flavors = donut_dictionary.get("flavors")
    return toppings, flavors


def get_choice(options):
    """ list str -> str
    returns the users input if it is one of the options in the
    parameter list """
    while True:
        choice = input(" ? >>> ").strip().lower()
        if choice in options:
            return choice
        print("Sorry!", choice, "is not an option")


def check_money(str_money):
    """ str -> bool
    return true if the str is in the format 0.00 """
    split_money = str_money.split(".")
    if len(split_money) != 2:
        return False
    dollars, cents = split_money[0], split_money[1]
    if dollars.isdigit() and cents.isdigit() and len(cents) == 2:
        return True
    return False


def get_money():
    """ None -> float
    returns a float value of the money the user is
    paying with """
    while True:
        str_money = input("? >>> $").strip()
        if check_money(str_money):
            money = float(str_money)
            if money >= 0.75:
                return money
            else:
                print("Not enough money!")
        else:
            print("Please enter amount in 0.00 format!")


def make_transaction_line(name, topping, flavor, cash_in, cash_out):
    """ str, str, str, float, float -> str
    returns the input parameters as a single line matching the format
    for the transaction file """
    return "{}, {}, {}, {:.2f}, {:.2f}\n".format(
        name, topping, flavor, cash_in, cash_out
    )


def save_transaction(filename, file_line):
    """ str filename, str -> None
    appends the string line to the file """
    with open(filename, "a") as file:
        file.write(file_line)


def donut_shop():
    """ core of the application """
    toppings, flavors = open_donut_file(DONUT_FILENAME)
    print(
        """Hello! Welcome to the Donut Shop!
    
    All donuts are 75¢, cash only.
    
    Choose your topping and flavor! Or get a random flavor!
    """
    )
    name = input("Can we get the name for this order?\n>>> ").strip()
    print(f"Welcome {name}! We are happy to assist you today!")
    print("[1] custom make your donut? or [2] have a random combination?")
    choice = get_choice(["1", "2"])
    if choice == "1":
        print("What topping would you like?")
        print(" | ".join(toppings))
        topping = get_choice(toppings)
        print("\nWhat flavor would you like?")
        print(" | ".join(flavors))
        flavor = get_choice(flavors)
        print(
            "Your order: donut with {} topping and {} flavored icing, great choice!".format(
                topping, flavor
            )
        )
    else:
        topping = randchoice(toppings)
        flavor = randchoice(flavors)
        print(
            "Your order: donut with {} topping and {} flavored icing, we hope you like it!".format(
                topping, flavor
            )
        )

    print(
        """
>>> Your total is $0.75
How much are you paying with?"""
    )
    cash_in = get_money()
    cash_out = cash_in - 0.75
    print("Here is your change: ${:.2f}\nHave a great day!".format(cash_out))

    file_line = make_transaction_line(name, topping, flavor, cash_in, cash_out)
    save_transaction(TRANSACTION_FILENAME, file_line)


if __name__ == "__main__":
    donut_shop()
