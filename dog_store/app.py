import json
from datetime import datetime

SERVICES_FILENAME = "/Users/basecamp/code/dog_spa_practice/dog_spa/services.json"
TRANSACTIONS_FILENAME = "transactions.txt"


def print_welcome_message():
    print(
        """
                         .--~~,__
            :-....,-------`~~'._.'
            `-,,,  ,_      ;'~U'
            _,-' ,'`-__; '--.
            (_/'~~      ''''(;
 WELCOME TO LUXURY DOG SERVICES!
    """
    )

def load_services(filename):
    with open(filename) as file:
        json_services = json.load(file)
    return json_services['services']

def print_selection(services):
    print("These are the services we offer")
    for key, value in services.items():
        print("\t{}.......{:.2f}".format(value['name'], value['price']))

def get_service_choice(valid_options):
    print('What would you like today?')
    while True:
        choice = input('>>> ').lower().strip()
        if choice in valid_options:
            return choice

def print_exit_message(item):
    name, price = item['name'], item['price']
    print(f"{name} such a good choice")
    print(f"Your total will be {price}")
    print("Thank you, have a nice day!")

def save_transaction(filename, item):
    name, price = item['name'], item['price']
    with open(filename, "a") as file:
        file.write(f"\n{datetime.now()}, {name}, {price}")

def dog_spa():
    print_welcome_message()
    services = load_services(SERVICES_FILENAME)
    print_selection(services)
    customer_service_selection = get_service_choice(services.keys())
    item = services.get(customer_service_selection)
    print_exit_message(item)
    save_transaction(TRANSACTIONS_FILENAME, item)
    
if __name__ == "__main__":
    dog_spa()
    
