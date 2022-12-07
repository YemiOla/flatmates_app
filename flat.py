

class Bill:
    """
    Object that contains data about a bill, such as 
    total amount and period of the bill.
    """

    def __init__(self, amount:float, period:str) -> None:
        self.amount = amount
        self.period = period

class Flatmate:
    """
    Create a flatmate person who lives in the flat and 
    pays a share of the bill.
    """

    def __init__(self, name:str, days_in_house:int) -> None:
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house/(self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return round(to_pay, 2)