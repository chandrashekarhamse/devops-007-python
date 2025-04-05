# palindrome.py

def is_palindrome(number: int) -> bool:
    """Function to check if a number is a palindrome."""
    # Convert number to string to easily check if it's the same forward and backward
    str_num = str(number)
    return str_num == str_num[::-1]


if __name__ == "__main__":
    # Example usage
    number = int(input("Enter a number: "))
    if is_palindrome(number):
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")
