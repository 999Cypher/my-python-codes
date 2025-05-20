try:
    import pyperclip  #text is copied to clipboard
except ImportError:
    pass

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('This simple cipher code lets you encrypt letters, try and have fun')

#Is user decrypting or encrypting
#the loop continues until user enters e or d

while True:
    print('Do you want to encrypt(e) or decrypt?(d)')
    response =input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter letter e or d')

 #User enters key to use
while True: #Asks until a valid key is entered
     maxKey = len(SYMBOLS) - 1
     print('Please enter the key (0 to {}) to use'.format(maxKey))
     response = input('> ').upper()
     if not response.isdecimal():
         continue

     if 0 < int(response)  < len(SYMBOLS):
         key = int(response)
         break
#User enters message to encrypt or decrypt
print('Enter the message to {}.'.format(mode))
message = input('> ')

#ceaser cipher only works on uppercase
message = message.upper()

#stores the encrypted/decrypted form of the message

translated = ''

#Encrypt/decrypt each symbol in the message
for symbol in message:
    if symbol in SYMBOLS:
        #get the encrypted or decrypted number for this symbol
        num = SYMBOLS.find(symbol) #Gets symbol number
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        #handle the wrap-around if num is larger than the length of
        #SYMBOLS or less than 0

        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)
        #add encrypted or decrypted number's symbol to the translated:
        translated = translated + SYMBOLS[num]
    else:
        #add the symbol without encrypting or decrypting
        translated = translated + symbol

#Display the message encrypted/decrypted
print(translated)

try:
    pyperclip.copy(translated)
    print('Full {} ed text copied to clipboard.'.format(mode))
except:
    pass # Do nothing if pyperclip is not installed





