import pyperclip
import time
import webbrowser
copyBuff = ' '

copyedText = pyperclip.paste()
copyBuff=copyedText
normalizedText = copyBuff.replace('\r', '\\r').replace('\n', '\\n').replace(
    '-\\r\\n', '').replace("\\r\\n", " ")
print(normalizedText)
