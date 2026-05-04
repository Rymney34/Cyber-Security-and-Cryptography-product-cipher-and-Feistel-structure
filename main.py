print("Hello Worldfsdfsdf")

from feistel import *
sampleMessage = "SEC6000 Confidential Data."
print("---Original Message---")
print(sampleMessage)
print()

parameters = {"shift": 3, 'v_key': "KEYS", "rails": 3}


roundKeys = [parameters] * 16
print("---Encryption and Decryption Output ---")
encrypted = feistelEncrypt16Rounds(sampleMessage, roundKeys)
# to prevent unprintable chars utf used hex() can be used to see readable string of characters
print(f"Encrypted: {encrypted.encode('utf-8')}")

decrypted = feistelDecrypt16Rounds(encrypted, roundKeys)
# strip used to cleanup the result
print(f"Decrypted: {decrypted.strip()}")




