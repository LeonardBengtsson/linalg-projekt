import numpy 

def normalize(matrix: numpy.ndarray):
    column_sum = numpy.sum(matrix, axis= 0)
    normalized_matrix = matrix/column_sum
    return normalized_matrix