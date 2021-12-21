import datetime
from BC.BCConstants import HASH_NOT_CALCULATED, NO_DATA, FIRST_ON_CHAIN
from BC.bdata.bdata import data
from BC.bdata.transaction import transaction
from BC.functions import sha256, format


class block(list):

    def __init__(self, bID, lbhash, creationDate = None) -> None:
        self.bID = bID
        self.bhash = HASH_NOT_CALCULATED
        self.ldhash = FIRST_ON_CHAIN
        self.lbhash = lbhash
        self.creationDate = creationDate if not creationDate == None else datetime.datetime.now()

    def computeHash(self):
        datahashes = "".join([str(bdata.dhash) for bdata in self if type(bdata) == data])
        s = "%s%s%s%s" % (self.bID, self.creationDate, self.lbhash, datahashes)
        self.bhash = format(sha256(s))

    def newData(self) -> data:
        d = data(self.bID, self.ldhash)
        self.append(d)
        return d

    def newTransaction(self, fromAddress, toAddress, amount, cID) -> transaction:
        t = transaction(self.bID, self.ldhash, fromAddress, toAddress, amount, cID)
        self.append(t)
        return t

    def __str__(self) -> str:
        sdata = "\n".join([str(s) for s in self]) if not self.__len__() == 0 else NO_DATA
        return "BCB-Hash:%s\nbID:%s\nCreation date:%s\nLast block hash:%s\nTotal data transfered:%d\n%s" % (self.bhash, self.bID, self.creationDate, self.lbhash, self.__len__(), sdata)
