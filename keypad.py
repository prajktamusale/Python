keypad = {'1': '.,?!:',
          '2': 'ABC',
          '3' :'DEF',
          '4':'GHI',
          '5':'JKL',
          '6':'MNO',
          '7': 'PQRS',
          '8':'TUV',
          '9':'WXYZ',
          '0':''}
def  get_keypresses(message):
    result = []
    message = message.upper()
    
    for char in message:
        for key, chars in keypad.items():
            if char in chars:
                presses = chars.index(char) + 1
                result.append(key * presses)
                break
    return''.join(result)
 
message = input("Enter a message")
keypresses = get_keypresses(message)
print("key presses:", keypresses)        