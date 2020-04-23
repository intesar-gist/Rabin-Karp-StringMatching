# RABIN KARP STRING MATCHING ALGORITHM

class RollingHash:
    
    def __init__(self, text, slidingWindow):
        self.base = 256
        self.p = 257 # what should be the optimal prime value
        self.hashVal = 0
        self.magic = 1
        
        for i in range(slidingWindow):
            if(ord(text[i]) >= 0 and ord(text[i]) < self.base):
                self.append(text[i])
            else:
                raise Exception("A char in a string is not ASCII!!")
            
    def append(self, new):
        self.hashVal = ((self.hashVal * self.base) + ord(new)) % self.p
        self.magic = (self.magic * self.base) 
    
    def skip(self, old):
        self.magic = self.magic // self.base
        self.hashVal = (self.hashVal - (ord(old) * self.magic) + self.p * self.base) % self.p
    
    
def RapinKarp(txt, pat):
    txtLen = len(txt)
    patLen = len(pat)
    
    txtRh = RollingHash(txt, patLen)
    patRh = RollingHash(pat, patLen)
    
    #print("Initial Pattern hash: {}".format(patRh.hashVal))
    
    for i in range(txtLen-patLen+1):
        #print("Initial txtRh.hashVal {}: {}".format(i, txtRh.hashVal))
        
        if(txtRh.hashVal == patRh.hashVal):
            if(pat == txt[i:i+patLen]):
                print("Match found at {}".format(i))
        
        if(i<txtLen-patLen): # check for array index out of bound 
                txtRh.skip(txt[i])
                txtRh.append(txt[i+patLen])

txt = "abcdabcd"
pat = "cd"
RapinKarp(txt, pat)
