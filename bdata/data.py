from dataManager import dataManager


class data:

    def __init__(self, creationDate) -> None:
        self.data = []
        self.creationDate = creationDate

    def __str__(self) -> str:
        sdata = [str(item) for item in self.data]
        return "\n".join(sdata)
