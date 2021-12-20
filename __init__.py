from BC.blockManager import manager as bManager
from BC.bdata.dataManager import manager as dManager
from BC.functions import format
import time
import random

#b1 = bManager.newBlock()
#time.sleep(5)
#b1.data.append(dManager.newTransaction("0xbe807dddb074639cd9fa61b47676c064fc50d62c", "0x0000000000000000000000000000000000001000", 0.013319685103897828, "BNB"))
#b1.computeHash()
#print(b1)

hashes = {}

def randaddress():
    return "0x" + format(random.randbytes(20).decode("Latin1"))
    
while True:
#for _ in range(0, random.randint(100000000,100000000)):
    b = bManager.newBlock()
    #for _ in range(0, random.randint(1,1000)):
    #    fromAddress = randaddress()
    #    toAddress = randaddress()
    #    amount = random.random() * 10
    #    b.data.append(dManager.newTransaction(fromAddress, toAddress, amount, "BNB"))
    b.computeHash()
    try:
        hashes[b.bhash] += 1
        print(b.bhash)
    except:
        hashes[b.bhash] = 1
