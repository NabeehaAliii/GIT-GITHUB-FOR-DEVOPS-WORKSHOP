"""
This module demonstrates the calculation of the average of three numbers.
"""


def calculate_average(num1, num2, num3):
    """
    Calculates the average of three numbers and returns the result.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        num3 (float): The third number.

    Returns:
        float: The average of the three numbers.
    """
    total = num1 + num2 + num3
    average = total / 3
    return average


def main():
    """
    Main function to test the calculate_average function.
    """
    number1 = 10.0
    number2 = 15.5
    number3 = 20.0
    result = calculate_average(number1, number2, number3)
    print(f"The average of {number1}, {number2},and {number3} is {result:.2f}")


if __name__ == "__main__":
    main()
