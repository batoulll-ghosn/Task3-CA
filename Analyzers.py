import os
import subprocess


def run_bandit(file_path):
    """
    Run Bandit static code analysis on the specified file.
    """
    print("\nRunning Bandit...")
    try:
        result = subprocess.run(
            ["bandit", "-r", file_path], capture_output=True, text=True
        )
        print(result.stdout)
    except FileNotFoundError:
        print("Error: Bandit is not installed. Install it using 'pip install bandit'.")


def run_pylint(file_path):
    """
    Run Pylint static code analysis on the specified file.
    """
    print("\nRunning Pylint...")
    try:
        result = subprocess.run(
            ["pylint", file_path], capture_output=True, text=True
        )
        print(result.stdout)
    except FileNotFoundError:
        print("Error: Pylint is not installed. Install it using 'pip install pylint'.")


def run_flake8(file_path):
    """
    Run Flake8 linting and security analysis on the specified file.
    """
    print("\nRunning Flake8...")
    try:
        result = subprocess.run(
            ["flake8", file_path], capture_output=True, text=True
        )
        print(result.stdout)
    except FileNotFoundError:
        print("Error: Flake8 is not installed. Install it using 'pip install flake8'.")


def main():
    """
    Main function to run static code analyzers on a Python script.
    """
    # Specify the Python file to analyze
    file_to_check = input("Enter the Python file path to analyze: ").strip()

    if not os.path.exists(file_to_check):
        print(f"Error: File '{file_to_check}' does not exist.")
        return

    # Run Bandit, Pylint, and Flake8
    run_bandit(file_to_check)
    run_pylint(file_to_check)
    run_flake8(file_to_check)


if __name__ == "__main__":
    main()
