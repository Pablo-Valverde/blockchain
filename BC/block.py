from BC.bdata.data import data as bdata
from BC.functions import sha256, format


class block:

    def __init__(self, bID, lbhash, data = None) -> None:
        self.bID = bID
        self.bhash = None
        self.lbhash = lbhash
        self.data = data if not data == None else bdata()

    def computeHash(self):
        self.bhash = "0x" + format(sha256("%s%s" % (self.lbhash, self.data)))

    def __str__(self) -> str:
        shash = self.bhash if self.bhash != None else "Not computed"
        sdata = str(self.data) if str(self.data) != "" else "No data"
        return "%s\n%s\n%s\n%s\n%s" % (self.data.creationDate, self.bID, shash, self.lbhash, sdata)
