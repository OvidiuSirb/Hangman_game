class Sentence(object):
    def __init__(self,propozitie):
        self._propozitie = propozitie

    def getSentence(self):
        return self._propozitie

    def getHangSentence(self):
        prop = str(self._propozitie).split()
        prop2 = str(self._propozitie).split()
        letters = []
        hangprop=[]
        hangprop2=[]
        for p in prop:
            p = list(p)
            x = 1
            while x < (len(p)-1):
                if p[x]!= p[0] and p[x] != p[len(p)-1]:
                    p[x]="_"
                x+=1
            st = ""
            for x in p:
                st+=x
            letters.append(st[0])
            letters.append(st[len(p)-1])
            hangprop.append(st)
        x = 0
        while x < (len(prop2)):
            l1 = list(hangprop[x])
            l2 = list(prop2[x])
            y = 1
            while y < (len(l1)-1):
                for z in letters:
                    if l2[y] == z:
                        l1[y] = z
                y+=1
            st = ""
            for a in l1:
                st+=a
            x+=1
            hangprop2.append(st)
        return hangprop2

    def __str__(self):
        return str(self._propozitie)

    def __len__(self):
        self._propozitie.strip()
        cnt = 0
        for x in self._propozitie:
            if x != " ":
                cnt+=1
        return cnt