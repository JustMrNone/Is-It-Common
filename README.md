# Is-It-Common

# Password Strength Checker Script

This Python script checks the strength of a user's password by comparing it against a list of the top 1,000,000 most common passwords. The script also enforces a minimum password length requirement.

## Script Components

- **Imports**:
  - `sys`: Used for handling command-line arguments and exiting the program.

- **Classes**:
  - **Pass**: 
    - Handles file operations to read a list of common passwords from a file.
    - The `__init__` method opens the specified file, reads its contents, and stores the lines.
    - The `readlines` method returns the file contents as a list of stripped lines.
  - **Compare**: Inherits from `Pass`.
    - `__init__` method initializes the parent class with a predefined password file.
    - `lengthcheck` method verifies that the password length is at least 5 characters.
    - `compare` method checks if the provided password is in the list of common passwords.

- **Main Function**:
  - Handles input either through command-line arguments or user input.
  - Verifies the password length using `lengthcheck`.
  - Compares the password against the list of common passwords.
  - Prints appropriate messages based on the password's strength.

## Usage

- Run the script with a password as a command-line argument or input it when prompted.
- The script will inform you if the password is too short or if it is found in the list of common passwords.


```bash
python your_script.py yourpassword

```
