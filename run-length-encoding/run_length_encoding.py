def decode(string):
    if (string == '' or isinstance(string, str) == False):
        return ''
    decodedString = ''
    previousChar = ''
    for char in string:
        if char.isdigit():
            previousChar += str(char)
        elif isinstance(char, str):
            if(previousChar == ''):
                previousChar = '1'
            decodedString+= int(previousChar)*char
            previousChar = ''
    return decodedString


def encode(string):
    if (string == ''):
        return ''
    encodedString = ''
    previousChar = ''
    currentLetterCount = 0
    for char in string:
        if char == previousChar :
            currentLetterCount += 1
        else:
            encodedString = updateEncoded(previousChar,currentLetterCount,encodedString)
            currentLetterCount = 1
            previousChar = char
    return updateEncoded(previousChar,currentLetterCount,encodedString)


def updateEncoded(previousChar, count, encodedString):      
    if (count > 0):
        if count == 1 :
            encodedString +=  previousChar
        else:
            encodedString += str(count) + previousChar 
    return encodedString