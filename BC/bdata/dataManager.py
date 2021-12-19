import datetime
from BC.bdata.transaction import transaction


class manager:

    lastID = 0

    @staticmethod
    def newTransaction(fromAddress, toAddress, amount, cID) -> transaction:
        t = transaction(manager.lastID, datetime.datetime.now(), fromAddress, toAddress, amount, cID)
        manager.lastID += 1
        return t
