from abc import abstractmethod
import datetime
from BC.BCConstants import HASH_NOT_CALCULATED
from BC.functions import sha256, format


class data:

    def __init__(self, bID, ldhash, creationDate = None) -> None:
        self.type = "BCI"
        self.bID = bID
        self.ldhash = ldhash
        self.dhash = HASH_NOT_CALCULATED
        self.creationDate = creationDate if not creationDate == None else datetime.datetime.now()

    @abstractmethod
    def computeHash(self) -> None:
        self.dhash = format(sha256("%s%s%s%s" % (self.bID, self.dhash, self.ldhash, self.creationDate)))

    def __str__(self) -> str:
        return "%s-Hash:%s\nBlock:%s\nCreation date:%s\nLast data hash:%s" % (self.type, self.dhash, self.bID, self.creationDate, self.ldhash)
