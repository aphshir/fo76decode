class fo76decode:
    def paring(key,number,pairlist):
        pairlist[key] = number
        return(pairlist)
    def findscrambled(keyword,pairlist):
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
        return(scrambled)
    def findcode(scrambled,word,pairs):
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