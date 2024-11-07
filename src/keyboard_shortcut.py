"""
Given a sentence containing few instances of "Ctrl + C" and "Ctrl + V", return the sentence after those keyboard shortcuts have been applied!

    - "Ctrl + C" will copy all text behind it.
    - "Ctrl + V" will do nothing if there is no "Ctrl + C" before it.
    - A "Ctrl + C" which follows another "Ctrl + C" will overwrite what it copies.


>> keyboardShortcut("the egg and Ctrl + C Ctrl + V the spoon")
>> "the egg and the egg and the spoon"

>> keyboardShortcut("WARNING Ctrl + V Ctrl + C Ctrl + V")
>> output=  "WARNING WARNING"

>> keyboardShortcut("The Ctrl + C Ctrl + V Town Ctrl + C Ctrl + V")
>> output = "The The Town The The Town"

"""


def keyboard_shortcut(sentence: str) -> str:
    words = sentence.split()
    copied_text = ""
    result = []

    for word in words:
        if word == "Ctrl":
            continue
        elif word == "+":  # ignore the "+" symbol used with Ctrl in the shortcuts
            continue
        elif word == "C":  # "Ctrl + C" detected
            copied_text = " ".join(result)  # copy all text up to this point
        elif word == "V":  # "Ctrl + V" detected
            result.extend(copied_text.split())  # paste copied text
        else:
            result.append(word)  # add normal words to result

    return " ".join(result)
