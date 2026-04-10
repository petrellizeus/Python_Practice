"""
Create a program that generates username suggestions based on the following user input:

1. First Name
2. Last Name
3. Middle Name
4. Year of Birth
5. Title

Recommend usernames based on the following patterns:

1. First Name + Last Name (e.g JeremiahFaluyi)
2. Initials of firstname and middle name plus last name (e.g JOFaluyi)
3. Intial of first name plus last name (e.g. JFaluyi)
4. First Name plus year of birth (e.g Jeremiah2026)
5. Title plus last name (e.g MrFaluyi)
"""

First_Name = input("First Name: ")
Last_Name = input("Last Name: ")
Middle_Name = input("Middle Name: ")
Year_Of_Birth = input("Year Of Birth: ")
Title = input("Title: ")
print("==================================================")

# Firstname_Plus_Last_Name = input("First Name Plus Last name: ")
# Initials_Of_Firstname_With_Middle_Name = input("Initials of Firstname and Middle Name: ")
# Initials_Of_Firstname_With_LastName = input("Initials Of FirstName With LastName: ")
# FirstName_With_Year_Of_Birth = input("FirstName With Year Of Birth: ")
# Title_Plus_LastName = input("Title With Last Name: ")
print(f"Hello, {First_Name}! Below are recommended Usernames Alternatives, Thanks!")
print(f"1. - {First_Name}{Last_Name}")
print(f"2. - {First_Name[0]}{Middle_Name[0]}{Last_Name}")
print(f"3. - {First_Name[0]}{Last_Name}")
print(f"4. - {First_Name}{Year_Of_Birth}")
print(f"2. - {Title}{Last_Name}")