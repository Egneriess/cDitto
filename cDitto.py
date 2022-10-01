import pyperclip


string = pyperclip.paste()
if string != None:
    print(string)
    
while True:
    if pyperclip.paste() != string:
        string = pyperclip.paste()
        pyperclip.copy(string)
        print(string)
