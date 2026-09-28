from random import randint


class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(
            f"Ticket fare in train no: {self.trainNo} "
            f"from {fro} to {to} is {randint(222, 55555)}"
        )


t = Train(12399)

t.book("Rampur", "Delhi")

t.getStatus()

t.getFare("Rampur", "Delhi")