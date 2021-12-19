import datetime
from BC.block import block


class manager:

    lastID = 0
    lastBlock = None

    @staticmethod
    def newBlock() -> block:
        bhash = manager.lastBlock.bhash if not manager.lastBlock == None else 0
        _ = block(manager.lastID, bhash)
        manager.lastBlock = _
        manager.lastID += 1
        return _
