import random

def generate_rand_integer(min_value, max_value):
    """
    Generate a random integer between min_value and max_value (inclusive).

    Parameters
    ----------
    min_value : int
        The minimum value for the random integer (inclusive).
    max_value : int
        The maximum value for the random integer (inclusive).
    Returns
    -------
    int
        A random integer between min_value and max_value.
    Raises
    ------
    ValueError
        If min_value or max_value is not an integer.
    Notes
    -----
    If there is an exception, a default random integer between 1 and 5 is returned.
    """
    try:
        # Check if min_value and max_value are integers
        if not isinstance(min_value, int) or not isinstance(max_value, int):
            raise ValueError("min_value and max_value must be integers.")
        
        # Return a random integer within the specified range
        return random.randint(min_value, max_value)
    
    except ValueError as e:
        # Handle the exception, print an error message, and return a default value
        print(f"Error: {e}")
        print("Default random values have been assigned.")
        return random.randint(1, 5)

def generate_rand_operator():
    """
    Generate a random arithmetic operator (+, -, or *).
    Returns
    -------
    str
        A random arithmetic operator.
    """
    # Return a random arithmetic operator from the list ['+', '-', '*']
    return random.choice(['+', '-', '*'])

def math_operation(num1, num2, operation):
    """
    Perform a math operation given two numbers and an operation.
    Parameters
    ----------
    num1 : int
        The first number.
    num2 : int
        The second number.
    operation : str
        The arithmetic operation (+, -, or *).
    Returns
    -------
    tuple
        A tuple containing a string representing the math problem and the correct answer.
    """
    # Create a string representation of the math problem
    problems = f"{num1} {operation} {num2}"
    
    # Perform the specified arithmetic operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    else:
        result = num1 * num2
    
    # Return a tuple with the math problem and the correct result
    return problems, result

def math_quiz():
    """
    Asks the user 3 random math problems using the generate_rand_integer
    and generate_rand_operator functions.
    Checks if the user's answer is correct and updates the score.
    Prints the final score at the end of the game.
    """
    # Initialize the score and the number of questions
    point = 0
    questions = 3
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    # Loop through the number of questions
    for _ in range(questions):
        # Generate random numbers and operator
        num1 = generate_rand_integer(1, 10)
        num2 = generate_rand_integer(1, 5)
        operation = generate_rand_operator()

        # Get the math problem and correct answer
        problem, answer = math_operation(num1, num2, operation)
        print(f"\nQuestion: {problem}")
        
        # Get user input for the answer
        user_answer = input("Your answer: ")
        user_answer = int(user_answer)

        # Check if the user's answer is correct and update the score
        if user_answer == answer:
            print("Correct! You earned a point.")
            point += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    # Print the final score at the end of the game
    print(f"\nGame over! Your score is: {point}/{questions}")

if __name__ == "__main__":
    # Call the math_quiz function if the script is executed directly
    math_quiz()
