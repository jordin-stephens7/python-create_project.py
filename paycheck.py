# Name: Jordin Stephens
# Date: September 18, 2026
# Course: COMP 163
# Project 1: Paycheck Calculator

employee_name = input()
hours_worked = float(input())
hourly_rate = float(input())
tax_rate = float(input())

gross_pay = hours_worked * hourly_rate
tax_withheld = gross_pay * (tax_rate / 100)
net_pay = gross_pay - tax_withheld

print(f"Employee: {employee_name}")
print(f"Gross pay: ${gross_pay:.2f}")
print(f"Tax withheld: ${tax_withheld:.2f}")
print(f"Net pay: ${net_pay:.2f}")
# Then print the four required output lines.
# The exact format is in README.md. Match it exactly or the tests will fail.
#
# Chapters 1 and 2 only. Use variables, input(), arithmetic, type conversion,
# and print(). Do not use if statements, loops, functions, or imports.
# Your code runs top to bottom, once.
