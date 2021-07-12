Morse_Dict = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-',
'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-',
'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--',
'X':'-..-', 'Y':'-.--', 'Z':'--..'}

def encrypt(message):
    convert = ' '
    for letter in message:
        if letter != ' ':
            convert += Morse_Dict[letter] + ' '
        else:
            convert += ' '
    return convert

def decrypt(message):
    message += ' '
    decode = ''
    text = ''
    for letter in message:
        if (letter != ' '):
            i = 0
            text += letter
        else:
            i += 1
            if i == 2:
                decode += ' '
            else:
                decode += list(Morse_Dict.keys())[list(Morse_Dict.values()).index(text)]
                text = ''
    return decode

def main():
    text = input("Enter Message: ")
    output = encrypt(text.upper())
    print(output)
if __name__ == '__main__':
    main()