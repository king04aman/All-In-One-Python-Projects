def gauss_partial(matrix: list, index_column: int):
    index_max_val = index_column

    for i in range(index_column, len(matrix)):
        if matrix[index_column][index_column] < abs(matrix[i][index_column]):
            index_max_val = i

    if index_column != index_max_val:
        matrix[index_column], matrix[index_max_val] = matrix[index_max_val], matrix[index_column]
            

def verify_triangular(matrix: list) -> bool:

    for i in range(len(matrix)):
        for j in range(i, len(matrix)):

            if (j == i and matrix[j][i] == 0) or (j != i and matrix[j][i] != 0):
                return False
        
    return True


def gauss(matrix: list, index: int) -> list:
    
    for j in range(index+1, len(matrix)):
        coefficient = round(matrix[j][index] / matrix[index][index], 2)
        matrix[j][index] = 0

        for k in range(index+1, len(matrix)+1):
            matrix[j][k] = round(matrix[j][k] - coefficient * matrix[index][k], 5)

    return matrix


def resolve_linear_system(matrix: list) -> list:
    sum = 0
    n = len(matrix)
    results = [1] * n

    for i in range(n-1, -1, -1):

        for j in range(n-1, i, -1):
            sum = sum + matrix[i][j]*results[j]

        results[i] = round((matrix[i][n] - sum)/matrix[i][i], 2)
        sum = 0

    return results


def resolve_matrix(matrix: list):

    for i in range(len(matrix)):
        gauss_partial(matrix, i)
        matrix = gauss(matrix, i)

    print('\nThe matrix after Gauss:')

    for line in matrix:
        print("[", end='')
        print(*(f'{val}' for val in line), end='')
        print("]")
        
    if verify_triangular(matrix):

        print("\nThe result of Gauss Elimination with Partial Pivoting:")
        for i, x in enumerate(resolve_linear_system(matrix)):
            print(f'x_{i} = {x}')

    else:
        print("It's impossible to resolve, because it's not a triangular matrix")
        return 0
        

def take_matrix() -> list:

    line = 0
    matrix = []
    max_length = 0

    number_lines = int(input("Please, insert the length of the your matrix: "))
    print("Please, insert only the numbers of the your augmented matrix (separete with espace):")

    for i in range(number_lines):
        
        try:
            line = list(input().split())
            line = list(int(val) for val in line)
    
            if max_length < len(line):
                max_length = len(line)

            matrix.append(line)
        
        except:
            print("This matrix don't exist!!!")
            return 1
        
    if len(matrix) == max_length - 1:
        return matrix
    
    return 0


if __name__ == '__main__':

    matrix = take_matrix()

    if matrix == 0:
        print("It's impossible to resolve")

    else:
        print('The matrix:')

        for line in matrix:
            print("[", end='')
            print(*(f'{val}' for val in line), end='')
            print("]")

        resolve_matrix(matrix)