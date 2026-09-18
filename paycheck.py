# Name: Jordin Stephens
# Date: 09-18-2026
# Course: COMP 163
# Project 1: Paycheck Calculator

name = input("Employee name: ")
hours = float(input("Hours worked: "))
rate = float(input("Hourly rate: "))
tax_rate = float(input("Tax rate: "))

gross = hours * rate
tax = gross * (tax_rate / 100)
net = gross - tax

print(f"Employee: {name}")
print(f"Gross pay: ${gross:.2f}")
print(f"Tax withheld: ${tax:.2f}")
print(f"Net pay: ${net:.2f}")

# Then calculate:
#   gross pay     = hours worked * hourly rate
#   tax withheld  = gross pay * (tax rate / 100)
#   net pay       = gross pay - tax withheld
#
# Then print the four required output lines.
# The exact format is in README.md. Match it exactly or the tests will fail.
#
# Chapters 1 and 2 only. Use variables, input(), arithmetic, type conversion,
# and print(). Do not use if statements, loops, functions, or imports.
# Your code runs top to bottom, once.
