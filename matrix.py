class Matrix:
    def __init__(self, matrix):
        constant = len(matrix[0])
        for row in matrix:
            if len(row) != constant:
                raise TypeError("Invalid Input")
        self.matrix = matrix

    def __repr__(self):
        repr_str = ""
        for row in self.matrix:
            row_str = "|"
            for col in row:
                row_str += repr(col) + ", "
            repr_str += row_str[:-2] + "|\n"
        return repr_str[:-1]

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Matrix([[col*other for col in row] for row in self.matrix])
        elif type(other) == Matrix:
            if self.cols == other.rows:
                my_rows = range(self.rows)
                ur_cols = range(other.cols)
                result = [[0 for _n in ur_cols] for _m in my_rows]
                for i in my_rows:
                    for k in ur_cols:
                        elem = 0
                        for j in range(self.cols):
                            elem += self.matrix[i][j] * other.matrix[j][k]
                        result[i][k] = elem
                return Matrix(result)
            else:
                raise TypeError("Wrong Size, Cannot Multiply")
        else:
            raise TypeError("Invalid Type, Cannot Multiply")

    def __add__(self, other):
        if type(other) == Matrix:
            if self.rows == other.rows and self.cols == other.cols:
                r, c = range(self.rows), range(self.cols)
                s, o = self.matrix, other.matrix
                return Matrix([[s[r][c] + o[r][c] for _c in c] for _r in r])
            else:
                raise TypeError("Wrong Size, Cannot Add")
        else:
            raise TypeError("Invalid Type, Cannot Add")

    @property
    def rows(self):
        return len(self.matrix)
    @property
    def cols(self):
        return len(self.matrix[0])

    @property
    def has_deter(self):
        return self.rows == self.cols

    @property
    def has_inverse(self):
        return self.determinant != 0

    @property
    def inverse(self):
        def remove(lst, index):
            return lst[:index] + lst[index+1:]
        deter = self.determinant
        if deter == 0:
            raise TypeError("No Inverse")
        new_m = [[col for col in row] for row in self.matrix]
        size = self.rows
        for i in range(size):
            for j in range(size):
                factor = Matrix([remove(r, i) for r in remove(self.matrix, j)]).determinant
                new_m[i][j] = ((-1) ** (i + j)) * factor / deter
        return Matrix(new_m)

    @property
    def determinant(self):
        def remove(lst, index):
            return lst[:index] + lst[index+1:]
        if self.has_deter:
            if self.rows == 1:
                return self.matrix[0][0]
            if self.rows == 2:
                m = self.matrix
                return m[0][0] * m[1][1] - m[0][1] * m[1][0]
            else:
                first_row = self.matrix[0]
                result, num_col = 0, 0
                for i in range(len(first_row)):
                    first_part = ((-1) ** (num_col)) * first_row[i]
                    sub_matrix = [remove(r, i) for r in remove(self.matrix, 0)]
                    rest_part = Matrix(sub_matrix).determinant
                    result += first_part * rest_part
                    num_col += 1
                return result
        else:
            raise TypeError("No Determinant")

def solve(A, R):
    """Solve the equation of AX = R
    Where A is the coefficient matrix
          X is the variable matrix
          R is the result matrix
    >>> solve(Matrix([[1,1],[1,-1]]), Matrix([[8],[2]]))
    |5.0|
    |3.0|
    """
    return A.inverse * R

print(solve(Matrix([[1,1],[1,-1]]), Matrix([[8],[2]])))
