class Ui:
    def __init__(self,controller):
        self._controller = controller

    @staticmethod
    def PrintMenu():
        string = "1-Add a sentence\n"
        string += "2-Start the game\n"
        string += "0-Exit"
        print(string)

    def MainMenu(self):
        while True:
            self.PrintMenu()
            cmd = input("Please insert command:")
            if cmd == '1':
                sentence = input("Please enter sentence:")
                self._controller.store(sentence)
            elif cmd == '0':
                return False
            elif cmd == '2':
                (hang,sentence) = self._controller.HangSentence()
                for x in hang:
                    print(x)
                h = 0
                while h < 7:
                    if h == 0:
                        print("H\n")
                    if h == 1:
                        print("HA\n")
                    if h == 2:
                        print("HAN\n")
                    if h == 3:
                        print("HANG\n")
                    if h == 4:
                        print("HANGM\n")
                    if h == 5:
                        print("HANGMA\n")
                    if h == 6:
                        print("HANGMAN\n")
                        break
                    letter = input("Please enter a letter: ")
                    hangprop = self._controller.ContinueSentence(sentence,hang,letter)
                    if hangprop == 0:
                        h+=1
                    else:
                        hang = hangprop
                        for t in hangprop:
                            print(t)
                        ver = self._controller.Verify(hangprop)
                        if (ver == 0):
                            print("YOU WON")
                            break


