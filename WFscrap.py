try:
    import requests
    import os
    from bs4 import BeautifulSoup
except:
    os.system('pip install requests')
    os.system('pip install bs4')

import requests
from bs4 import BeautifulSoup



def findValue_(htmlElement):
    if type(htmlElement) != str:
        raise (ValueError(
            f"htmlElement htmlElement must be a string (not a {type(htmlElement)})"
        ))
    value = ""
    valueFind = False
    for cpt, letter in enumerate(htmlElement):
        if not valueFind:
            if letter == '>':
                valueFind = True
            else:
                pass
        elif valueFind:
            if htmlElement[cpt + 1: cpt + 3] == 'em':
                valueFind = False
            elif htmlElement[cpt + 1: cpt + 4] == '/em':
                valueFind = False
            elif letter == '<':
                break
            value = value + letter
    return value.replace('<', '')


def findAnagram(anagram, letter='max'):
    if type(letter) != int and letter != 'max':
        raise (ValueError("The argument letter must be an integer or equal to 'max'"))

    url = 'https://www.thewordfinder.com/anagram-solver/'
    result = requests.post(url, data={
        'letters': f'{anagram}',
        'pos': 'beg',
        'dict': 'wwf',
        'dic': 1,
        'order': 'length',
    })

    doc = BeautifulSoup(result.text, "html.parser")
    word = doc.find_all(["p"], class_="result")
    values = []
    lengthWord = []

    if letter == 'max':
        for cpt, tag in enumerate(word):
            word = tag.find_all(["a"])
            value = findValue_(str(word))
            lengthWord.append(len(value))
            if lengthWord[cpt - 1] > lengthWord[cpt] and cpt != 0:
                break
            else:
                values.append(value)
    else:
        for tag in word:
            word = tag.find_all(["a"])
            value = findValue_(str(word))
            lengthWord = len(value)
            if lengthWord == letter:
                values.append(value)

    return values


##if __name__ == '__main__':
##
##    print(findAnagram('?ut?mn?l', letter=2))
##
##    print(findAnagram('autumnal', letter=8))
