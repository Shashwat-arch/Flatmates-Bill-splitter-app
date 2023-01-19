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

    def pays(self, bill):
        pass


class PdfReport:
    """
    create a pdf file that contain data about the flatmates such as
    their names, their amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def (self, flatmate1, flatmate2, bill):
        pass
