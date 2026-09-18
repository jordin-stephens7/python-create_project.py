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
