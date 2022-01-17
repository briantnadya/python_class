class Matrix:
    def __init__(self, param):
        self.param = param

    def __str__(self):
        str_1 = ''
        for list_el in self.param:
            for el in list_el:
                str_1 = str_1 + " " + str(el)
            str_1 = str_1 + "\n"
        return str_1

    def __add__(self, other):
        result_clmn = []
        result = []
        for i in range(len(self.param)):
            for j in range(len(self.param[0])):
                result_clmn.append(self.param[i][j] + other.param[i][j])
            result.append(result_clmn)
            result_clmn = []
        return result


obj_1 = Matrix([[1, 4, 3], [1, 1, 1]])
obj_2 = Matrix([[1, 1, 1], [1, 1, 1]])

result = Matrix(obj_1 + obj_2)
print(result)
