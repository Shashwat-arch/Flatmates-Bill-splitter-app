from flat import Bill, Flatmate
from reports import PdfReport

amount = int(input("Enter the bill amount : "))
period = input("Enter the period(Month year) : ")

name1 = input("Enter the name of first person: ")
days_in_house1 = int(input(f"How many days did {name1} stayed in the house during the {period} period : "))

name2 = input("Enter the name of second person: ")
days_in_house2 = int(input(f"How many days did {name2} stayed in the house during the {period} period : "))

the_bill = Bill(amount, period)
first_person = Flatmate(name1, days_in_house1)
second_person = Flatmate(name2, days_in_house2)

# print(f"{first_person.name} pays : ", first_person.pays(bill=the_bill, Flatmate2=second_person))
# print(f"{second_person.name} pays : ", second_person.pays(bill=the_bill, Flatmate2=first_person))

generate_pdf = PdfReport(f"{period}.pdf")
generate_pdf.generate(first_person, second_person, the_bill)