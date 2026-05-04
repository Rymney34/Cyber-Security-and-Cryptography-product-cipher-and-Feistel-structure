
def caesarEncrypt(text, shift):
        result = ""

        for i in range(len(text)):
            char = text[i]

            if(char.isupper()):
                result += chr((ord(char) + shift-65) % 26 + 65)
            else:
                result += chr((ord(char) + shift-97) % 26 + 97)
        # print(result)
        return result

def caesarDecrypt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if(char.isupper()):
            result += chr((ord(char) - shift-65) % 26 + 65)
        else:
            result += chr((ord(char) - shift-97) % 26 + 97)
    # print(result)
    return result


def vigenereEncrypt(text, key):
    result = ""
    key = key.upper()
    keyIndex = 0

    for char in text:
        #  is alpha checks each char if it letter
        if char.isalpha():
            # print(key)
            # print(type(key))
            shift = ord(key[keyIndex % len(key)]) - ord('A')
            if char.isupper():
                result += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
            else:
                result += chr((ord(char) - ord("a") + shift) % 26 + ord('a'))

            keyIndex += 1
        else:
            result += char
    # print(result)
    return result

def vigenereDecrypt(cipherText, key):
    result = ""
    key = key.upper()
    keyIndex = 0

    for char in cipherText:
        #  is alpha checks each char if it letter
        if char.isalpha():

            shift = ord(key[keyIndex % len(key)]) - ord('A')

            if char.isupper():
                result += chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
            else:
                result += chr((ord(char) - ord("a") - shift) % 26 + ord('a'))

            keyIndex =+ 1
        else:
            result += char
    return result

def encryptRailFence(text, key):
    rail =[['\n' for i in range(len(text))]
           for j in range(key)]

    direction = False
    row, col = 0,0

    for i in range(len(text)):
        if(row == 0) or (row == key -1):
            direction = not direction

        rail[row][col] = text[i]
        col += 1

        if direction:
            row += 1
        else:
            row -= 1

    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("".join(result))

def decrytpRailFence(cipher, key):

    rail =[['\n' for i in range(len(cipher))]
           for j in range(key)]

    direction = None
    row, col = 0,0

    for i in range(len(cipher)):
        if row == 0:
            direction = True
        if row == key -1:
            direction = False


        rail[row][col] = '*'
        col += 1

        if direction:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == "*") and
            (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1


    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            direction = True
        if row == key-1:
            direction = False
        if(rail[row][col] != "*"):
            result.append(rail[row][col])
            col += 1

        if direction:
            row += 1
        else:
            row-=1
    return ("".join(result))
