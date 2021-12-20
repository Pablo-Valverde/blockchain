import hashlib


LETTERS = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

def sha256(s):
    und_hash = hashlib.sha256()
    und_hash.update(s.encode())
    dig_hash = und_hash.digest().decode("Latin1")
    return dig_hash

def format(s):
    formated = ""
    for c in s:
        if c in LETTERS:
            formated += c
        else:
            formated += ord(c).__str__()
    return "0x" + formated
