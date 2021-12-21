from BC.blockManager import manager as bManager
from BC.functions import format
import random

def randaddress():
    return "0x" + format(random.randbytes(20).decode("Latin1"))

for _ in range(0, random.randint(1,10)):
    b = bManager.newBlock()
    for _ in range(0, random.randint(1,10)):
        fromAddress = randaddress()
        toAddress = randaddress()
        amount = random.random() * 10
        b.newTransaction(fromAddress,toAddress,amount,0).computeHash()
    b.computeHash()
    print(b.__str__() + "\n")
