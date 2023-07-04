from functools import lru_cache

class Matrix:
    def __init__(self, matrix: list[list[int, float]]):
        self._rows = len(matrix)
        self._cols = len(matrix[0])
        self._matrix = matrix

    def __add__(self, other):
        new_matrix = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        for j in range(self._rows):
            for i in range(self._cols):
                new_matrix[j][i] = self._matrix[j][i] + other._matrix[j][i]
        return Matrix(new_matrix)

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return self.__rmul__(other)
        elif isinstance(other, int) or isinstance(other, int):
            new_matrix = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
            for j in range(self._rows):
                for i in range(self._cols):
                    new_matrix[j][i] = self._matrix[j][i] * other
            return Matrix(new_matrix)

    def __rmul__(self, other):
        new_matrix = [[0 for _ in range(other._rows)] for _ in range(self._rows)]
        for j in range(self._rows):
            for i in range(other._rows):
                new_matrix[j][i] = self._matrix[j][i] * other._matrix[i][j]
        return Matrix(new_matrix)

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if self._rows != other._rows or self._cols != other._cols:
            return False
        for j in range(self._rows):
            for i in range(self._cols):
                if self._matrix[j][i] != other._matrix[j][i]:
                    return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self._matrix]) + '\n'

    def __repr__(self):
        return f'Matrix({self._matrix})'




