from random import randint
class Train :
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book (self, fro, to):
        print(f"ticekt booked from {fro} to {to} in {self.trainNo}")

    def ticketfare(self, fro, to):
        print(f"ticket fare in {self.trainNo} from {fro} to {to} is {randint(222, 999)}")

t = Train(21771)
t.book("firozpur", "USA")
t.ticketfare("allo", "kcahlu")

    