from BC.bdata.bdata import data
from BC.functions import sha256, format


class transaction(data):

    def __init__(self, bID, ldhash, fromAddress, toAddress, amount, cID, creationDate = None) -> None:
        super().__init__(bID, ldhash, creationDate)
        self.type = "BCT"
        self.fromAddress = fromAddress
        self.toAddress = toAddress
        self.amount = amount
        self.cID = cID

    def computeHash(self) -> None:
        s = super().computeHash + "%s%s%s%s" % (self.fromAddress, self.toAddress, self.amount, self.cID)
        h = format(sha256(s))
        return h

    def __str__(self) -> str:
        return "%s\nFrom address:%s\nTo address:%s\nAmount:%s %s" % (super().__str__(), self.fromAddress, self.toAddress, self.amount, self.cID)
