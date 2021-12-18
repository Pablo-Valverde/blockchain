from binfo import _information


class __transaction(_information):

    def __init__(self, ID, creationDate, fromAddress, toAddress, amount, cID) -> None:
        super().__init__(ID, creationDate)
        self.fromAddress = fromAddress
        self.toAddress = toAddress
        self.amount = amount
        self.cID = cID

    def __str__(self) -> str:
        return "%s|%s->%s|%s->%s" % (super().__str__(), self.fromAddress,self.toAddress,self.amount,self.cID)
