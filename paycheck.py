# Name: Jordin Stephens
# Date: September 18, 2026
# Course: COMP 163
# Project 1: Paycheck Calculator

employee_name = input()
hours_worked = float(input())
hourly_rate = float(input())
tax_rate = float(input())

# Hours worked and the hourly rate can have a fraction in them, like 37.5
# hours or 10.25 hours. Use float() for all three numbers, not int().
# int("37.5") crashes.
#
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
