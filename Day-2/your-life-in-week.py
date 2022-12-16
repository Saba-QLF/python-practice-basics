age = input("What is your current age? :  ")

age_as_int = int(age)
years_remaining = 90-age_as_int
days = years_remaining*365
weeks = years_remaining*52
months = years_remaining*12
print(f"you have {days} days, {weeks} weeks, {months} months left.")