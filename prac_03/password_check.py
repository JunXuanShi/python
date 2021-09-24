"""password = input("What's your password")
number = len(password)
print("*" * number)"""


def main():
    """the function is to get password and parameter from users and print asterisks."""
    password = input("What's your password")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    number = len(password)
    print("Your {}-character password is valid: {}".format(len(password), password))
    print("*" * number)


def get_parameter():
    """the function is to get parameter from users."""
    length = int(input("What's the size of your password ?"))
    return length


def is_valid_password(password1):
    """the function is to check the password is valid or not."""
    if 0 < len(password1) <= get_parameter():
        return True
    else:
        return False


main()
