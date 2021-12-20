from abc import abstractmethod
import datetime
from BC.BCConstants import HASH_NOT_CALCULATED
from BC.functions import sha256, format


class data:

    def __init__(self, bID, ldhash, creationDate = None) -> None:
        self.type = "BCI"
        self.bID = bID
        self.ldhash = ldhash
        self.dhash = None
        self.creationDate = creationDate if not creationDate == None else datetime.datetime.now()

    @abstractmethod
    def computeHash(self) -> str:
        h = format(sha256("%s%s%s%s" % (self.bID, self.dhash, self.ldhash, self.creationDate)))
        return h

    def __str__(self) -> str:
        dhash = self.dhash if self.dhash != None else HASH_NOT_CALCULATED
        return "%s-Hash:%s\nBlock:%s\nCreation date:%s\nLast data hash:%s" % (self.type, dhash, self.bID, self.creationDate, self.ldhash)
