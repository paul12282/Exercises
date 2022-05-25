RATES = {
    'Chico': 0.5,
    'Groucho': 0.7,
    'Harpo': 0.5,
    'Zeppo': 0.4
}


class HourTooLowError(Exception): pass


class HourTooHighError(Exception): pass


def time_percentage(hour):
    return hour / 24


def calculate_tax(amount, state, hour):
    if hour < 0:
        raise HourTooLowError(f'Hour of {hour} is < 0')
    if hour >= 24:
        raise HourTooHighError(f'Hour of {hour} is >= 24')
    try:
        return amount + (amount * RATES[state] * time_percentage(hour))
    except KeyError:
        print(f'Please enter a valid province')