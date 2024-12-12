import numpy 


def normalize(matrix: numpy.ndarray):
    column_sum = numpy.sum(matrix, axis=0)
    normalized_matrix = numpy.multiply(matrix, numpy.reciprocal(column_sum))
    return normalized_matrix


def is_normalized(matrix: numpy.ndarray) -> bool:
    column_sum = numpy.sum(matrix, axis=0)
    return numpy.all(abs(column_sum - 1) < 0.0000001)


def is_positive(matrix: numpy.ndarray) -> bool:
    return numpy.all(matrix >= 0)