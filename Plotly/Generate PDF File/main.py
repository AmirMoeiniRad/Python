# This Python app has a Command-Line Interface (CLI).

# Description:
# An app that get as input the amount of a bill for a particular period and
# the days that each of the flatmates stayed in the house for that period and returns how much each flatmate
# has to pay. It also generates a PDF report stating the names of the flatmates, the period and how much
# each of them had to pay.

from flat import Bill, Flatmate
from reports import PDFReport


amount = float(input("Hey user, enter the bill amount: "))
period = input("What is the bill period? e.g. December 2020: ")

name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house during the bill period? "))

name2 = input("What is the name of the other flatmate? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill period? "))

the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{flatmate1.name} pays:", flatmate1.pays(the_bill, flatmate2))
print(f"{flatmate2.name} pays:", flatmate2.pays(the_bill, flatmate1))

pdf_report = PDFReport(filename=f"Report - {the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, bill=the_bill)
