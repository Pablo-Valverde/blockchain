import datetime


class data(list):

    def __init__(self, creationDate = None) -> None:
        self.creationDate = creationDate if not creationDate == None else datetime.datetime.now()

    def __str__(self) -> str:
        sdata = [str(item) for item in self]
        return "\n".join(sdata)
