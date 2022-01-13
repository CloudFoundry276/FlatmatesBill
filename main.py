from flat import Bill, Flatmate
from reports import PdfReport


amount = float(input("Hey user, enter the bill amount: "))
period = input("What is the bill period (ex. December 2020): ")

name1 = input("Enter name of first flatmate: ")
days1 = int(input(f"How many days did {name1} stay in the house during the bill period: "))

name2 = input("Enter name of second flatmate: ")
days2 = int(input(f"How many days did {name2} stay in the house during the bill period: "))

the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days1)
flatmate2 = Flatmate(name2, days2)

print("Amount paid by {} is ${}".format(flatmate1.name, flatmate1.pays(the_bill, flatmate2)))
print("Amount paid by {} is ${}".format(flatmate2.name, flatmate2.pays(the_bill, flatmate1)))

pdf_report = PdfReport("{}.pdf".format(the_bill.period))
pdf_report.generate(flatmate1, flatmate2, the_bill)
