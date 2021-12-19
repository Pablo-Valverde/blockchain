class information:

    def __init__(self, ID, creationDate) -> None:
        self.ID = ID
        self.creationDate = creationDate

    def __str__(self) -> str:
        return "BCI%s|%s" % (self.ID, self.creationDate)
