class Dance:
    moves = {right:step, left:step, right:jig, left:jig}
    def __init__(self, dancing):
        self.dancing = dancing
    def move_genwrator(self, dancing):
        try:
            if dancing:
                dance_move = moves[rand.int]