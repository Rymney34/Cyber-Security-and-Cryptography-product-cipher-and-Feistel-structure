
from feistel import *
sampleMessage = "SEC6000 Confidential Data."
print("---Original Message---")
print(sampleMessage)
print()

parameters = {"shift": 3, 'v_key': "KEYS", "rails": 3}

def demonstrateTransformations(plaintext, caesar_shift, vigenere_key, rail_depth):
    print("--- Step-by-Step Transformation Demonstration ---")
    print(f"1. Input Text :          '{plaintext}'")

    step1 = caesarEncrypt(plaintext, caesar_shift)
    print(f"2. Caesar Output:          '{step1}'")


    step2 = vigenereEncrypt(step1, vigenere_key)
    print(f"3. Vigenère Output:        '{step2}'")


    step3 = encryptRailFence(step2, rail_depth)
    print(f"4. Rail Fence (Final) Output: '{step3}'")
    print("---------------")
    print()
demonstrateTransformations(sampleMessage, 3, "KEYS", 3)

roundKeys = [parameters] * 16
print("---Encryption and Decryption Output ---")
encrypted = feistelEncrypt16Rounds(sampleMessage, roundKeys)
# to prevent unprintable chars utf used hex() can be used to see readable string of characters
print(f"Encrypted: {encrypted.encode('utf-8')}")

decrypted = feistelDecrypt16Rounds(encrypted, roundKeys)
# strip used to cleanup the result
print(f"Decrypted: {decrypted.strip()}")




