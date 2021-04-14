class Matrix:
    def __init__(self, my_list):
        self.new_list = '\n'.join(['\t'.join([str(j) for j in i]) for i in my_list])
        List = []
        for i in my_list:
            List.append([j for j in i])
        self.my_list = List

    def __str__(self):
        for i in range(len(self.my_list)):
            return f'{self.my_list[0]} \n{self.my_list[1]} \n{self.my_list[2]}'

    def __add__(self, other):
        result = []
        number = []
        for i in range(len(self.my_list)):
            for j in range(len(self.my_list[0])):
                summ = other.my_list[i][j] + self.my_list[i][j]
                number.append(summ)
                if len(number) == len(self.my_list):
                    result.append(number)
                    number = []
        return Matrix(result)


matrix_1 = Matrix([[1, 2, 1], [1, 1, 5], [0, 1, 1]])
matrix_2 = Matrix([[2, 3, 2], [7, 2, 2], [2, 7, 2]])
matrix_3 = matrix_1 + matrix_2
print(matrix_3)
