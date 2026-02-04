class TextRepo:
    def __init__(self, filepath: str):
        self._filepath = filepath
        self._data = [[0 for _ in range(8)]for _ in range(8)]
        self.read()

    def read(self):
        self._data = [[0 for _ in range(8)]for _ in range(8)]
        row = 0
        col = 0
        with open(self._filepath, "r") as file:
            for line in file:
                for char in line:
                    if char == "\n":
                        continue
                    self._data[row][col] = int(char)
                    col += 1
                row += 1
                col = 0


    def getData(self):
        return self._data[:]