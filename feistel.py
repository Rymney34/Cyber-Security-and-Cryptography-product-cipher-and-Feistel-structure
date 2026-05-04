
from ciphers import *

def productEncrypt(plaintext, caeserShift, vigenereKey, railDepth):
    encryption1 = caesarEncrypt(plaintext, caeserShift)
    encryption2 = vigenereEncrypt(encryption1, vigenereKey)
    # print("Product",encryptRailFence(encryption2, railDepth))
    return encryptRailFence(encryption2, railDepth)

def feistelEncrypt16Rounds(dataBlock, roundKeys):
    """Executing the 16 round Feistel structure"""

    if len(dataBlock) % 2 != 0:
        dataBlock += " "

    halfLen = len(dataBlock) // 2
    lHalf = list(dataBlock[:halfLen])
    rHalf = list(dataBlock[halfLen:])

    for i in range(16):
        newL = rHalf
        keys = roundKeys[i]

        funcOutput = productEncrypt(
            "".join(rHalf),
            keys["shift"],
            keys['v_key'],
            keys['rails']
        )

        newR = [chr(ord(a) ^ ord(b)) for a, b in zip(lHalf, funcOutput)]

        lHalf = newL
        rHalf = newR
    return ''.join(lHalf + rHalf)

def feistelDecrypt16Rounds(ciphertext, roundKeys):
    """Decryption in 16 rounds """

    halfLen = len(ciphertext) // 2
    lHalf = list(ciphertext[:halfLen])
    rHalf = list(ciphertext[halfLen:])

    reversedKeys =  roundKeys[::-1]

    for i in range(16):
        # newL = rHalf
        keys = reversedKeys[i]

        funcOutput = productEncrypt(
            "".join(lHalf),
            keys["shift"],
            keys['v_key'],
            keys['rails']
        )

        newL = [chr(ord(a) ^ ord(b)) for a, b in zip(rHalf, funcOutput)]
        newR = lHalf

        lHalf = newL
        rHalf = newR
    return ''.join(lHalf + rHalf)