from BC.BCConstants import FIRST_ON_CHAIN
from BC.block import block


class manager:

    lastID = 0
    lastBlock = None

    @staticmethod
    def newBlock() -> block:
        bhash = manager.lastBlock.bhash if not manager.lastBlock == None else FIRST_ON_CHAIN
        manager.lastBlock = block(manager.lastID, bhash)
        manager.lastID += 1
        return manager.lastBlock
