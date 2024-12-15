import os
import bcrypt

def get_password_from_user():
    """
    Prompt the user to enter a password securely.
    Returns the password as a string.
    """
    try:
        # Use input as fallback if environment variable is not set
        password = os.getenv('USER_PASSWORD')
        if not password:
            password = input("Enter your password: ").strip()
        return password
    except Exception as e:
        raise ValueError("Error obtaining password input: " + str(e))


def hash_password(password: str, salt_rounds: int = 12) -> str:
    """
    Hashes the provided password using bcrypt with the specified number of salt rounds.
    Returns the hashed password as a string.
    """
    try:
        # Hash the password securely
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(salt_rounds))
        return hashed_password.decode('utf-8')  # Decode for storage or display
    except Exception as e:
        raise RuntimeError("Error hashing password: " + str(e))


def main():
    """
    Main function to demonstrate secure password handling.
    """
    try:
        # Obtain password securely
        password = get_password_from_user()

        # Validate password length and complexity
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
            raise ValueError("Password must contain both letters and numbers.")

        # Hash the password
        hashed_password = hash_password(password)

        # Print the hashed password
        print("Your hashed password is:", hashed_password)
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except RuntimeError as re:
        print(f"System Error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
