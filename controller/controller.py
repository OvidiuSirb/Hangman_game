from domain.entities import Sentence
import random

class Controller:
    def __init__(self,repository):
        self._repository = repository

    def store(self,sentence):
        obj = Sentence(sentence)
        self._repository.store(obj)

    def HangSentence(self):
        repo = self._repository.getAll()
        nr = random.randrange(0,len(repo)-1)
        hang = repo[nr].getHangSentence()
        sentence = repo[nr].getSentence().split()
        return (hang,sentence)

    def ContinueSentence(self,sentence,hang,letter):
        x = 0
        hangprop=[]
        cnt = 0
        while x < (len(sentence)):
            l1 = list(hang[x])
            l2 = list(sentence[x])
            y = 1
            while y < (len(l2)-1):
                if l2[y] == letter and l1[y]=="_":
                    l1[y] = letter
                    cnt = 1
                y+=1
            st = ""
            for a in l1:
                st+=a
            x+=1
            hangprop.append(st)
        if cnt == 0:
            return 0
        return hangprop

    def Verify(self,hang):
        for x in hang:
            l1 = list(x)
            for y in l1:
                if y == "_":
                    return 1
        return 0