class Repository:
    def __init__(self):
        self._data = []

    def store(self, sentence):
        self._data.append(sentence)

    def getAll(self):
        return self._data