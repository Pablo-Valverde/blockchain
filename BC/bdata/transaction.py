from abc import abstractmethod
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

    @abstractmethod
    def computeHash(self) -> None:
        super().computeHash()
        s = "%s%s%s%s%s" % (self.dhash, self.fromAddress, self.toAddress, self.amount, self.cID)
        self.dhash = format(sha256(s))

    def __str__(self) -> str:
        return "%s\nFrom address:%s\nTo address:%s\nAmount:%s %s" % (super().__str__(), self.fromAddress, self.toAddress, self.amount, self.cID)
