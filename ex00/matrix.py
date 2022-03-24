class Matrix:
    @staticmethod
    def type_is_consistent(iterable):
        types = list(set(map(type, iterable)))
        if len(types) == 1 and types[0] == list:
            return list
        elif len(types) > 1 and list in types:
            return None
        elif len(types) > ((int in types) + (float in types)):
            return None
        else:
            return types[0]

    @staticmethod
    def is_valid(arg):
        n_dimensions = 0
        queue = arg.copy()
        while queue:
            n_dimensions += 1
            consistent = Matrix.type_is_consistent(queue)
            if consistent is None:
                print("A list can only contain elements of the same type.")
                return False
            n = len(queue)
            if consistent is list:
                if len(set(map(len, queue))) > 1:
                    print("Shape is inconsistent.")
                    return False
                for _ in range(n):
                    elem = queue.pop(0)
                    queue.extend(elem)
            else:
                break
        return n_dimensions

    def __init__(self, init):
        self.data = None
        self.shape = None
        error_msg = "Matrix/Vector can only be initialized with\
 a list of lists or a tuple."
        if isinstance(init, list):
            d = Matrix.is_valid(init)
            if not d:
                return
            if d != 2:
                print(error_msg)
                return
            self.data = init
            self.shape = (len(init), len(init[0]))
        elif isinstance(init, tuple):
            shape_error_msg = "The shape tuple has to have 2 strictly\
 positive integers: (n_rows, n_columns)."
            if len(init) != 2:
                print(shape_error_msg)
                return
            if not isinstance(init[0], int) or not isinstance(init[1], int):
                print(shape_error_msg)
                return
            (n, m) = init
            if n <= 0 or m <= 0:
                print(shape_error_msg)
                return
            self.data = [[0 for j in range(m)] for i in range(n)]
            self.shape = init
        else:
            print(error_msg)

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        if self.data:
            return f'{type(self).__name__}({self.data})'
        return 'None'

    def __add__(self, op):
        if not self.data:
            return None
        error_msg = "Only matrices/vectors of the same shape\
 can be added together."
        if isinstance(op, type(self)):
            if not op.data:
                return None
            if self.shape != op.shape:
                print(error_msg)
                return None
            (n, m) = self.shape
            data = [[0 for j in range(m)] for i in range(n)]
            for j in range(m):
                for i in range(n):
                    data[i][j] += op.data[i][j] + self.data[i][j]
            return type(self)(data)
        else:
            print(error_msg)

    def __radd__(self, op):
        if not self.data:
            return None
        error_msg = "Only matrices/vectors of the same shape\
 can be added together."
        if not isinstance(op, type(self)):
            print(error_msg)
            return None
        if not op.data:
            return None
        return self.__add__(op)

    def __sub__(self, op):
        if not self.data:
            return None
        error_msg = "Only matrices/vectors of the same shape can be\
 substracted from each other."
        if isinstance(op, type(self)):
            if not op.data:
                return None
            if self.shape != op.shape:
                print(error_msg)
                return None
            (n, m) = self.shape
            data = [[0 for j in range(m)] for i in range(n)]
            for j in range(m):
                for i in range(n):
                    data[i][j] += self.data[i][j] - op.data[i][j]
            return type(self)(data)
        else:
            print(error_msg)

    def __rsub__(self, op):
        if not self.data:
            return None
        error_msg = "Only matrices/vectors of the same shape can be\
 substracted from each other."
        if not isinstance(op, type(self)):
            print(error_msg)
            return None
        if not op.data:
            return None
        return op.__sub__(self)

    def __truediv__(self, scalar):
        if not self.data:
            return None
        error_msg = "Matrices/vectors can only be divided by scalars."
        div_by_zero_error_msg = "Division by zero."
        if not isinstance(scalar, (int, float)):
            print(error_msg)
            return None
        if not scalar:
            print(div_by_zero_error_msg)
            return None
        (n, m) = self.shape
        data = [[self.data[i][j] / scalar for j in range(m)] for i in range(n)]
        return type(self)(data)

    def __rtruediv__(self, scalar):
        if not self.data:
            return None
        error_msg = "Matrices/vectors can only be divided by scalars."
        div_by_zero_error_msg = "Division by zero."
        if not isinstance(scalar, (int, float)):
            print(error_msg)
            return None
        (n, m) = self.shape
        data = [[0 for j in range(m)] for i in range(n)]
        for j in range(m):
            for i in range(n):
                if not self.data[i][j]:
                    print(div_by_zero_error_msg)
                    return None
                data[i][j] = scalar / self.data[i][j]
        return type(self)(data)

    def __mul__(self, op):
        if not self.data:
            return None
        error_msg = "Matrices can only be multiplied\
 by another matrix, a vector, or a scalar."
        if isinstance(op, (int, float)):
            (n, m) = self.shape
            data = [[self.data[i][j] * op for j in range(m)] for i in range(n)]
            return type(self)(data)
        elif type(self) is Matrix and type(op) is Vector:
            if not op.data:
                return None
            (n, m) = self.shape
            d = op.shape[0]
            if m != d:
                print(f"The number of columns of the matrix ({m})\
 doesn't match the number of rows of the vector ({d}).")
                return None
            data = [[sum([self.data[i][j] * op.data[j][0] for j in range(m)])]
                    for i in range(n)]
            return Vector(data)
        elif isinstance(op, Matrix):
            if not op.data:
                return None
            (n, m) = self.shape
            (p, q) = op.shape
            if m != p:
                print(f"The number of columns of the left operand ({m})\
 doesn't match the number of rows of the right one ({p}).")
                return None
            data = [[sum([self.data[i][k] * op.data[k][j]
                    for k in range(m)]) for j in range(q)] for i in range(n)]
            return Matrix(data)
        else:
            print(error_msg)
            return None

    def __rmul__(self, op):
        if not self.data:
            return None
        error_msg = "Matrices can only be multiplied\
 by another matrix, a vector, or a scalar."
        if isinstance(op, (int, float)):
            return self.__mul__(op)
        elif isinstance(op, Matrix):
            if not op.data:
                return None
            return op.__mul__(self)
        else:
            print(error_msg)
            return None

    def T(self):
        if not self.data:
            return None
        (n, m) = self.shape
        data = [[self.data[i][j] for i in range(n)] for j in range(m)]
        return type(self)(data)


class Vector(Matrix):
    def __init__(self, init):
        super().__init__(init)
        if self.shape:
            (n, m) = self.shape
            if n != 1 and m != 1:
                print("Vector can only be initialized with a list of\
 shape (1, n) (row vector) or (n, 1) (column vector).")
                return

    def dot(self, v):
        if not self.data:
            return None
        if type(v) is Vector:
            if not v.data:
                return None
            if self.shape != v.shape:
                print("Vectors must have the same shape.")
            elif self.shape[0] == 1:
                return sum([x * y for (x, y) in zip(self.data[0], v.data[0])])
            else:
                return sum([x[0] * y[0] for (x, y) in zip(self.data, v.data)])
        else:
            print("v is not a vector.")
        return None
