"""This program emulates a simple expense tracking program. It employs various functions
to add expenses to a list, save those expenses, and perform a certain number of 
operations on those expenses (total cost, matching of categories, etc.)

Task: Your task is to complete the implementation of the code and make sure that matches
the requirements set in the assignment's prompt.
First, you will have to make your code identifiable by setting the following information.

******************************************************
Name: Alagbe Israel Oluwaferanmi
Andrew ID: ioa
Semester: Summer 2023
Course: Introduction to Python
Last modified: 30th June 2023
******************************************************

"""

from typing import Tuple

# Declare a global variable to contain all the expenses processed in the program
expenses = []


class BadInputException(Exception):
    """Vanilla exception class used for testing"""
    pass


def add_expense(category: str, amount: float):
    """Appends an expense to the `expenses` variable.

    Args:
       - category: the name of the category of the expense. type: string
       - amount: the amount of the expense. type: float

    Returns: None

    Raises: 
       - ValueError: if the input is not valid.
    """
    # statement to use the global expenses object
    global expenses
    # Python is not a strong typed language meaning that you have
    # no certainty over the type of data that you receive in your
    # calls. So it is good practice to verify that the type of the input is
    # okay.

    # TODO: Verify that the category variable contains at least three characters
    if not category or not amount:
        raise BadInputException("Invalid input: Category and amount cannot be empty.")

    if len(category) < 3:
        raise BadInputException("Invalid input: Category should contain at least three characters.")

    if not isinstance(amount, float):
        raise BadInputException("Invalid input: Amount should be a floating value.")

    if amount <= 0:
        raise BadInputException("Invalid input: Amount should be strictly greater than zero.")
    # now that you have confirmed that the values are valid, you can add them to the list
    # TODO: Append a tuple (category, amount) to the `expenses` list

    expenses.append((category, amount))


def dump_expenses(file_path = 'expenses.txt'):
    """Dumps the content of the list to a file

       Returns: None

       Args:
          - file_path: the location of the output file. type 'string'
    """
    global expenses
    # TODO: Open the file by overriding its content first (https://docs.python.org/3/tutorial/inputoutput.html#tut-files)
    # TODO: For each tuple in the `expenses`' list, write a line in the file in the CSV format (e.g., Clothes,10.05)
    # Use a precision of 2 decimal points for the amount.
    with open(file_path, 'w') as file:
        for expense in expenses:
            category, amount = expense
            line = f"{category},{amount:.2f}\n"
            file.write(line)


def read_expenses(file_path = 'expenses.txt'):
    """Reads the expenses from a file and saves it as a tuple into the expenses list

    Returns: None

    Args:
       - file_path: the path to the input file. type: string
    """
    global expenses

    # TODO:Read the file, and based on the output format used in `dump_expenses`, load the content into
    # the list. If the file does not exist, safely return from the function.
    # Refer to https://docs.python.org/3/tutorial/errors.html for more guidance on how to handle
    # errors in Python and https://docs.python.org/3/tutorial/inputoutput.html for access to the file.
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        category, amount = line.split(',')
                        expenses.append(
                            (category.strip(), float(amount.strip())))
                    except ValueError:
                        print(f"Ignoring invalid line: {line}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found. No expenses read.")


def get_expenses_by_category(category):
    """Returns a list of all the expenses that matches the category passed as argument.

    Args:
       - category: the category to match the expenses against.

    Returns:
       A list of expenses matching the set criteria
    """
    global expenses
    # TODO:Return a list of tuple of expenses of which the category is equal to the parameter
    # Create an empty list to store the matching expenses
    requested_expenses = []
    for expense in expenses:
        # Check if the category of the current expense matches the provided category
        if expense[0] == category:
            requested_expenses.append(expense)
    return requested_expenses


def calculate_total_expenses():
    """Returns the total of the amounts recorded as expenses.

    Args: None

    Returns: the total amount of the expenses

    """
    global expenses
    # TODO: compute and return the total of the amounts in the list.
    total = 0.0  # Initialize the total amount to zero
    for expense in expenses:
        total += expense[1]  # Add the amount of each expense to the total
    return total


def get_menu_action() -> int:
    """This function shows the menu and interprets the action to be done
    by the user.

    Args: None
    Returns: the user's selection.

    """
    # TODO: Change the loop's condition so that the user keeps being prompted
    # until their input is valid (i.e. in [1, 4])
    while True:
        print('Menu:')
        print('1. Add an expense')
        print('2. View expenses by category')
        print('3. Calculate total expenses')
        print('4. Exit')

        # TODO: Modify the next line to have the `choice` variable store the selection
        # of the user
        # choice = None
        try:
            choice = int(input("Enter your choice: "))
            if choice in [1, 2, 3, 4]:
                break  # Valid choice, exit the loop
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return choice


def print_expense(expense: Tuple[str, float]) -> str:
    """Prints an instance of an expense.

    Args:
       - expense: the expense to be displayed. type: a tuple of a string and a floating point number

    Returns:
       - The string representation to be displayed
    """
    category, amount = expense
    # TODO:Produce an output such that the line starts with a | and ends with the same |.
    # the category should be output by using 10 characters, left-aligned, space-filled.
    # the amount is preceded by a $ sign, and occupies as well 10 characters, left-aligned, space filled.
    # here space filled means that if there is less than 10 characters, you should fill the
    # line with spaces. Extra characters can be truncated. Use 2 decimal positions for the amount.
    # Below two examples

    # in: (Clothes,5.5525) -> out: |Clothes   |$5.55     |
    # in: (House Materials,2424.69) -> out: |House Mate|$2424.69  |

    # This formats the category with 10 characters, left-aligned and space-filled
    formatted_category = category[:10].rjust(10)

    # This formats the amount with 2 decimal positions and 10 characters, left-aligned and space-filled
    formatted_amount = f"${amount:.2f}".rjust(10)

    # Prints the final formatted string with the expense representation
    formatted_expense = f"|{formatted_category}|{formatted_amount}|"

    return formatted_expense


if __name__ == "__main__":
    # TODO: Read the expenses, if file exists, into the 'expenses' list
    read_expenses()
    # Retrieve the user's choice
    while True:
        command = get_menu_action()
        if command == 1:
            category = input('Expense Category: ')
            amount = input('Expense Amount: ')
            try:
                if not amount:
                    raise BadInputException("Invalid input: Amount cannot be empty.")
                amount = float(amount)
                add_expense(category=category, amount=amount)
                print('Expense', category, 'added successfully!')
            except BadInputException:
                print('Invalid value!')

        elif command == 2:
            category = input('Expense Category: ')
            expenses = get_expenses_by_category(category=category)
            print('|Category  |Amount    |')
            print('***********************')
            for expense in expenses:
                formatted_expense = print_expense(expense)
                print(formatted_expense)

        elif command == 3:
            total = calculate_total_expenses()
            print(f'Total expenses is: ${total:.2f}')

        elif command == 4:
            # TODO: Save the list of expenses into a file for future use
            # TODO: change the next statement to exit the program gracefully
            dump_expenses()  # Save the list of expenses into a file
            print("Expenses saved successfully.")
            print("Exiting the Expense Tracker Application....")
            # TODO: Add any additional steps or messages if needed
            break  # Exit the loop and end the program
        else:
            raise ValueError('Invalid command entered')
