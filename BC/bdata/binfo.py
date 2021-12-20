import datetime


class information:

    def __init__(self, ID, bID, ldhash, creationDate = None) -> None:
        self.ID = ID
        self.bID = bID
        self.ldhash = ldhash
        self.dhash = None
        self.creationDate = creationDate if not creationDate == None else datetime.datetime.now()

    def __str__(self) -> str:
        return "BCI%s|%s" % (self.ID, self.creationDate)
