MENU = {"Burger": 10, "Pasta": 13.5, "Beef steak": 22.2, "pork ribs": 14, "sushi": 33}


def restaurant(my_menu):
    running_total = 0
    while True:
        order = input('What would you like to eat? ').strip()  # strip removes any trailing white space
        if order in my_menu:
            running_total += my_menu[order]
            print(f'Item costs: ${my_menu[order]}, your running total is ${running_total}')
        elif not order:
            print(f'Your grand total is: ${running_total}')
            break
        else:
            print(f'Sorry, we are fresh out of {order} today.')


# restaurant(MENU)

CREDENTIALS = {'Matt': 'XQCL', 'Paul': 'Corona', 'Taxi': 'butt123'}


def login_system(users_passwords: dict):
    try:
        username = input('Please enter your username: ')
        password = input('Please enter your password: ')
        if users_passwords[username] in password:
            print('Login succesful')
        else:
            print('Your credentials are wrong, please check your typing')
    except KeyError:
        print('Your credentials are wrong, please check your typing')


# login_system(CREDENTIALS)

BIRTHDAYS = {'tata': 1960, 'mama': 1961, 'Natalia': 1986, 'Mihai': 1990}


def calc_age(ages):
    try:
        name = input("Enter the name who's age you want to know: ")
        age = 2022 - ages[name]
        print(f'{name} is {age} years old')
    except KeyError:
        print("Invalid name, please try again")


calc_age(BIRTHDAYS)
