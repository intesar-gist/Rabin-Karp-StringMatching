# RABIN KARP STRING MATCHING ALGORITHM
# Author: Intesar Haider

class RollingHash:
    
    def __init__(self, text, slidingWindow):
        self.base = 256
        self.p = 257 # what should be the optimal prime value
        self.ibase = self.modinv(self.base, self.p) % self.p
    
        self._hashVal = 0
        self.magic = 1
        
        for i in range(slidingWindow):
            if(ord(text[i]) >= 0 and ord(text[i]) < self.base):
                self.append(text[i])
            else:
                raise Exception("A char in a string is not ASCII!!")
            
    def append(self, new):
        self._hashVal = ((self._hashVal * self.base) + ord(new)) % self.p
        self.magic = (self.magic * self.base) % self.p
    
    def skip(self, old):
        self.magic = (self.magic * self.ibase) % self.p
        self._hashVal = (self._hashVal - (ord(old) * self.magic) + (self.p * self.base)) % self.p
        
    def hashValue(self):
        return self._hashVal
        
    def egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def modinv(self, a, m):
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

def RapinKarp(txt, pat):
    txtLen = len(txt)
    patLen = len(pat)
    
    txtRh = RollingHash(txt, patLen)
    patRh = RollingHash(pat, patLen)
    
    print("Initial Pattern hash: {}".format(patRh.hashValue()))
    
    for i in range(txtLen-patLen+1):
        #print("Initial txtRh.hashVal {}: {}".format(i, txtRh.hashVal))
        
        if(txtRh.hashValue() == patRh.hashValue()):
            #print("HASH MATCHED at [{}]".format(txt[i:i+patLen]))
            if(pat == txt[i:i+patLen]):
                print("Match found at {}".format(i))
        
        if(i<txtLen-patLen): # check for array index out of bound 
                txtRh.skip(txt[i])
                txtRh.append(txt[i+patLen])

#txt = "This program implements Rabin-Karp algorithm. This particular algo uses rolling hashes to optimally perform string searches."
#pat = " rolling hashes to optima"

txt = "HelloWorldHelloWorldHelloWorld"
pat = "rld"
RapinKarp(txt, pat)

