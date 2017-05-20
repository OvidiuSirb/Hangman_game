from repository.repo import Repository

class FileRepo(Repository):
    def __init__(self):
        Repository.__init__(self)

    def store(self,sentence):
        Repository.store(self,sentence)
        self.storeToFile()

    def storeToFile(self):
        f = open ("sentences.txt",'w')
        repo = Repository.getAll(self)
        for x in repo:
            f.write(str(x))
            f.write('\n')
        f.close()