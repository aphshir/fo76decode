import requests
import re
import WFscrap as WF #custom lib to scrap wordfinder made by dilgodev !
def pairing(key,number,pairlist):
    if type(key) != str:
        raise TypeError("expected str at key got, " ,errortrans(key))
    if type(number) != int:
        raise TypeError('expected int at number got, ',errortrans(number))
    if type(pairlist) != dict:
        raise TypeError('expected dict at pairlist got, ',errortrans(pairlist))
    pairlist[key] = number
    return(pairlist)
def findscrambled(keyword,pairlist):
    if type(keyword) != str:
        raise TypeError('expected str at keyword got, ',errortrans(keyword))
    if type(pairlist) != dict:
        raise TypeError('expected dict at pairlist got, ',errortrans(pairlist))
    alphabet=tuple(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
    keyalpha=alphabet
    keyalpha=list(keyalpha)
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
        raise TypeError('expected str at scrambled got, ',errortrans(scrambled))
    if type(word) != str:
        raise TypeError('expected str at word got, ',errortrans(word))
    if type(pairs) != dict:
        raise TypeError('expected dict at pairs got, ',errortrans(pairs))
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
def APIfindanagram(scrambled):
    if type != scrambled:
        raise TypeError('expected str at scrambled got, ', errortrans(scrambled))
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
def errortrans(typ):
    r=''
    typ=type(typ)
    if typ == str:
        r='str'
    elif typ == tuple:
        r='tuple'
    elif typ == int:
        r='int'
    elif typ == dict:
        r='dict'
    elif typ == list:
        r='list'
    elif typ == range:
        r='range'
    elif typ == float:
        r='float'
    elif typ == complex:
        r='complex'
    elif typ == bytes:
        r='bytes'
    elif typ == bytearray:
        r='bytearray'
    elif typ == memoryview:
        r='memoryview'
    elif typ == bool:
        r='bool'
    elif typ == set:
        r='set'
    elif typ == frozenset:
        r='frozenset'
    else:
        r=type(typ)
    return(r)
def sameLetter(anagram, word):
    if len(anagram) != len(word):
        raise (ValueError('Les mots doivent être de la même longueur'))
    for cpt in range(len(anagram)):
        if anagram[cpt] == '?':
            pass
        else:
            if anagram[cpt] != word[cpt]:
                return False
    return True
def Fincomplete(anagram,lenth='max'):
    result=[]
    wordlist=WF.findAnagram(anagram,lenth)
    for i in wordlist:
        if sameLetter(anagram,i) == True:
            result.append(i)
    return(result)
    
