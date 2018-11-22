# Program to determine the number of happy and unhappy customers (and their ratio) on a bus route
# Author: David Paul
# Date: 2016-12-05

# The number of passengers that can fit on a bus
BUS_SIZE = 50

# Prompts to be used in the program's main loop

# A prompt for the number of passengers leaving the bus at a particular stop
LEAVING_PROMPT = "How many passengers left the bus at stop #{0}? "
# A prompt for the number of passengers waiting for the bus at a particular stop
ENTERING_PROMPT = "How many passengers were waiting for the bus at stop #{0}? "
# A prompt for when an invalud number of passengers is entered.
INVALID_PASSENGER_NUMBER_PROMPT = "Invalid number of passengers. Please enter a non-negative integer."
# A prompt for when too many passengers are recorded as leaving the bus
INVALID_PASSENGERS_LEAVING_PROMPT = "Invalid number of passengers. Only {0} passengers were on the bus."

def read_integer(request_prompt, error_prompt):
    """
      Presents the given request prompt to the user and reads in an integer value.
      If an invalid value is entered, the error_prompt is displayed and the process repeats.

      Arguments:
      request_prompt -- The prompt displayed to the user when asked to enter an integer
      error_prompt -- The prompt displayed to the user if they enter an invalid value

      Returns the integer value entered by the user (as an int)
    """
    value = 0
    valid = False

    while not valid:
        value_string = input(request_prompt)

        try:
            value = int(value_string)
            valid = True
        except ValueError:
            print(error_prompt)

    return value

def read_positive_integer(request_prompt, error_prompt):
    """
      Presents the given request prompt to the user and reads in a positive integer value.
      If an invalid value is entered, the error_prompt is displayed and the process repeats.

      Arguments:
      request_prompt -- The prompt displayed to the user when asked to enter a positive integer
      error_prompt -- The prompt displayed to the user if they enter an invalid value

      Returns the positive integer value entered by the user (as an int)
    """
    value = read_integer(request_prompt, error_prompt)
    while value <= 0:
        print(error_prompt)
        value = read_integer(request_prompt, error_prompt)
    return value

def read_non_negative_integer(request_prompt, error_prompt):
    """
      Presents the given request prompt to the user and reads in a non-negative integer value.
      If an invalid value is entered, the error_prompt is displayed and the process repeats.

      Arguments:
      request_prompt -- The prompt displayed to the user when asked to enter a non-negative integer
      error_prompt -- The prompt displayed to the user if they enter an invalid value

      Returns the non-negative integer value entered by the user (as an int)
    """
    value = read_integer(request_prompt, error_prompt)
    while value < 0:
        print(error_prompt)
        value = read_integer(request_prompt, error_prompt)
    return value

# The route we are recording the customers for
route = read_positive_integer("Please enter the route number: ", "Invalid route number. Please enter a positive integer.")

# The number of stops on this route
num_stops = read_positive_integer("Please enter the number of stops on this route: ", "Invalid number of stops. Please enter a positive integer.")
# There must be at least two: the start and the end
while num_stops < 2:
    print("Invalid number of stops. There must be at least two stops on the route.")
    num_stops = read_positive_integer("Please enter the number of stops on this route: ", "Invalid number of stops. Please enter a positive integer.")

# The number of customers who successfully complete their journey
happy_customers = 0
# The number of customers unable to get on the bus because it is too full
unhappy_customers = 0

# The number of passengers currently recorded as being on the bus
passengers_on_bus = 0

for i in range(num_stops):
    # The number of passengers leaving the bus at this stop
    num_leaving = 0

    # The number of passengers waiting for the bus at this stop
    num_arriving = 0

    if i != 0:  # No passengers to leave at stop 0!
        # Ensure a valid number of passengers leaving the bus
        num_leaving = read_non_negative_integer(LEAVING_PROMPT.format(i + 1), INVALID_PASSENGER_NUMBER_PROMPT)
        while num_leaving > passengers_on_bus:
            print(INVALID_PASSENGERS_LEAVING_PROMPT.format(passengers_on_bus))
            num_leaving = read_non_negative_integer(LEAVING_PROMPT.format(i + 1), INVALID_PASSENGER_NUMBER_PROMPT)

        if i == num_stops - 1:  # All passengers should leave at the last stop!
            while num_leaving != passengers_on_bus:
                print("This is the last stop. There should be {} passengers leaving.".format(passengers_on_bus))
                num_leaving = read_non_negative_integer(LEAVING_PROMPT.format(i + 1), INVALID_PASSENGER_NUMBER_PROMPT)

    if i != num_stops - 1:  # Passengers should be able to get on at all stops except the last
        num_arriving = read_non_negative_integer(ENTERING_PROMPT.format(i + 1), INVALID_PASSENGER_NUMBER_PROMPT)

    passengers_on_bus -= num_leaving
    # The number of spaces available at this stop after passengers have gotten off
    available_spaces = BUS_SIZE - passengers_on_bus
    if num_arriving <= available_spaces:
        # All happy customers
        happy_customers += num_arriving
        passengers_on_bus += num_arriving
    else:
        # Some missed out
        happy_customers += available_spaces
        unhappy_customers += num_arriving - available_spaces
        passengers_on_bus += available_spaces

# Only calculate ratio if there was at least one unhappy customer
if unhappy_customers == 0:
    ratio = 0
else:
    ratio = float(happy_customers) / float(unhappy_customers)

# Print out results
print("Route number: {}".format(route))
print("Happy customers: {}".format(happy_customers))
print("Unhappy customers: {}".format(unhappy_customers))
print("Ratio of happy to unhappy customers: {:.2f}".format(ratio))
