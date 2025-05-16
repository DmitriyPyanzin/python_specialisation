class Matrix:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for i in range(rows)] for j in range(cols)]

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('Размеры матриц не совпадают')
        res = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                res.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return res


