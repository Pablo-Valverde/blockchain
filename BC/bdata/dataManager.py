from BC.bdata.bdata import data
from BC.bdata.transaction import transaction


class manager:

    lastID = 0
    lastData = None

    @staticmethod
    def newData():
        d = data(manager.lastID, 0, 0)
        manager.lastID += 1
        return d

    @staticmethod
    def newTransaction(fromAddress, toAddress, amount, cID) -> transaction:
        t = transaction(manager.lastID, fromAddress, toAddress, amount, cID)
        manager.lastID += 1
        return t
