class TitleKocka:
    def __init__(self, TposX, TposY, Ttype):
        self.POS = [TposX, TposY]
        self.TYPE = Ttype
        self.SEEN = False
    def setSeen(self):
        self.SEEN = True