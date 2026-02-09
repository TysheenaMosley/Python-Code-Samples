# Name: Tysheena Mosley
# Date: February 2026
# Program Description:
# This program displays the return day of the week based on a number entered by the user.

day_number = int(input("Enter a number (0-6): "))

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if 0 <= day_number <= 6:
    print("The return day is:", days[day_number])
else:
    print("Invalid number. Please enter a number between 0 and 6.")
