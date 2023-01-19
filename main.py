class Bill:
    """
    Object that contains data about a bill such as total amount and period
    of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    creates a flatmate person who lives in the flat and pays the
    share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, Flatmate2):
        weight = self.days_in_house / (self.days_in_house + Flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    create a pdf file that contain data about the flatmates such as
    their names, their amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass

the_bill = Bill(amount=120, period="December 2022")
john = Flatmate(name="john", days_in_house=20)
marry = Flatmate(name="marry", days_in_house=25)

print("John pays : ", john.pays(bill=the_bill, Flatmate2=marry))
print("Marry pays : ", marry.pays(bill=the_bill, Flatmate2=john))

