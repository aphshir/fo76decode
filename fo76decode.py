import requests
import re
def pairing(key,number,pairlist):
    if type(key) != str:
        raise TypeError('expected str at key got, ',type(key))
    if type(number) != int:
        raise TypeError('expected int at number got, ',type(number))
    if type(pairlist) != dict:
        raise TypeError('expected dict at pairlist got, ',type(pairlist))
    pairlist[key] = number
    return(pairlist)
def findscrambled(keyword,pairlist):
    if type(keyword) != str:
        raise TypeError('expected str at keyword got, ',type(keyword))
    if type(pairlist) != dict:
        raise TypeError('expected dict at pairlist got, ',type(pairlist))
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    keyalpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    pairindex=list(pairlist)
    keyletters = re.findall('[a-zA-Z]', keyword)
    for i in range(len(keyletters)):
        keyalpha.remove(keyletters[i])
    keyalpha= keyletters+keyalpha
    pairpos=[]
    for i in range(8):
        pairpos.append(keyalpha.index(pairindex[i]))
    scrambled = []
    for i in range(8):
        scrambled.append(alphabet[pairpos[i]])
    sscrambled="".join(scrambled)
    return(sscrambled)
def findcode(scrambled,word,pairs):
    if type(scrambled) != str:
        raise TypeError('expected str at scrambled got, ',type(scrambled))
    if type(word) != str:
        raise TypeError('expected str at word got, ',type(word))
    if type(pairs) != dict:
        raise TypeError('expected dict at pairs got, ',type(pairs))
    scrambled=re.findall('[a-zA-Z]', scrambled)
    pairindex=list(pairs)
    wordlist=re.findall('[a-zA-Z]', word)
    mirorcode=[]
    codel=[]
    code=""
    temp=None
    for i in range(8):
        mirorcode.append(scrambled.index(word[i]))
    for i in range(8):
        codel.append(pairs[pairindex[mirorcode[i]]])
    code = "".join(map(str,codel))
    return(code)
def findanagram():
    if type != scrambled:
        raise TypeError('expected str at scrambled got, ', type(scrambled))
    anagram=[]
    url="http://www.anagramica.com/all/:"+scrambled
    resp=requests.get(url)
    jsn=resp.json()
    lst=jsn['all']
    for i in range(len(lst)):
        if len(lst[i]) == 8:
            anagram.append(lst[i])
    if anagram == []:
        anagram = None
    return(anagram)
