class TitleKocka:
    def __init__(self, TposX, TposY, Ttype):
        self.POS = [TposX, TposY]
        self.TYPE = Ttype
        self.SEEN = False
    def setSeen(self):
        self.SEEN = True
    def setType(self, arg):
        self.TYPE = arg
    def getSeen(self):
        return self.SEEN
    def getType(self):
        return self.TYPE