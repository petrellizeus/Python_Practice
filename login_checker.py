"""
Create a login validator that checks multiple criteria for a user's password.

1. Length Check: The password must be at least 8 characters long
2. Special Characters: It must contain either a "!" or "@"
3. Restricted Username: The password cannot be thesame as the username
4. Admin Bypass: If the username is "admin", it bypasses the special character rule but must be 12+ characters long
"""

username = input("Enter Username: ")
password = input("Enter Password: ")

is_admin = username == "admin"
min_char = 12 if is_admin else 8

# if is_admin:
#     min_char = 12

# if username == "admin":
#     is_admin = True
# else:
#     is_admin = False

if len(password) < min_char:
    print(f"ERROR: Password must be at least {min_char} chars!")
    exit()

if username == password:
    print("ERROR: Password must not be the same as username!")
    exit()

contains_at = password.find("@") > -1
contains_exclamation = password.find("!") > -1

if not is_admin and not(contains_at or contains_exclamation):
    print("ERROR: Password must contain @ or !")
    exit()