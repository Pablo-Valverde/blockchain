from BC.bdata.binfo import information


class transaction(information):

    def __init__(self, ID, bID, ldhash, fromAddress, toAddress, amount, cID, creationDate = None) -> None:
        super().__init__(ID, bID, ldhash, creationDate)
        self.fromAddress = fromAddress
        self.toAddress = toAddress
        self.amount = amount
        self.cID = cID

    def __str__(self) -> str:
        return "%s|%s->%s|%s->%s" % (super().__str__(), self.fromAddress, self.toAddress, self.amount, self.cID)
