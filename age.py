from datetime import datetime, date
current_date = date.today()
user_input = input(
    "Please enter your date of birth in the format '01-01-2000': ")
user_dob = datetime.strptime(user_input, "%d-%m-%Y").date()
age = current_date.year - user_dob.year
if current_date.month < user_dob.month:
    age -= 1
print(age)
