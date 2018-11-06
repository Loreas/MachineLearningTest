class state:
    def __init__(self, mouse, grid):
        self.grid = grid
        self.mouse = mouse




class mouse:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.end = False
        if x == 1:
            directions = ()