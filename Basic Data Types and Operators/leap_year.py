# Get the year from the user
year = int(input("Enter a year: "))

# Check leap year conditions
# A year is a leap year if:
# -> Divisible by 4 AND
# -> Not divisible by 100 unless also divisible by 400
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

print("\n")