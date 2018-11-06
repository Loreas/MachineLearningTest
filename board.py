class Board:
    def __init__(self):
        self.bord = {}
        for i in range(1,11):
            for j in range(1, 11):
                self.bord[(i, j)] = 0

    def __str__(self):
        string = ""
        for i in range(1, 11):
            string += "\n"
            for j in range(1,11):

                string += str(self.bord[(i, j)]) + "\t"
        return string