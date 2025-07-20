class Blockblast:
    def __init__(self, height, width):
        self.height = height
        self.width = width

        self.board = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(False)
            self.board.append(row)


