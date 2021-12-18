import datetime
from transaction import _transaction


class dataManager:

    lastID = 0

    @staticmethod
    def newTransaction(fromAddress, toAddress, amount, cID):
        _ = _transaction(dataManager.lastID, datetime.datetime.now(), fromAddress, toAddress, amount, cID)
        dataManager.lastID += 1
        return _
