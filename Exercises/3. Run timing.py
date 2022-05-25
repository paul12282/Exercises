def run_timing():  # Asks the user repeatedly for numeric input. Prints the average time and number of runs
    number_of_runs = 0
    total_time = 0
    while True:
        user_input = input("Enter 10 km run time: ")
        if not user_input:
            break
        number_of_runs += 1
        total_time += float(user_input)
    average_lap = total_time / number_of_runs
    print(f'Your average lap time is: {average_lap} minutes over {number_of_runs} runs')


run_timing()
