import numpy

from data.data import DataSet, Year, get_data
import data.data
import math_utils


def main():
    dataset = get_data(Year.Y2020)

    ims_matrix = dataset.ims_matrix
    immigration = numpy.sum(ims_matrix, axis=0)
    natives = dataset.population - immigration
    natives[natives < 0] = 0
    population_matrix = ims_matrix + numpy.diag(natives)

    normalized_population_matrix = math_utils.normalize(population_matrix.astype(float))
    assert math_utils.is_normalized(normalized_population_matrix)
    assert math_utils.is_positive(population_matrix)

    country = input('Choose country: ').strip()
    assert country in dataset.countries
    generations = int(input('Choose how many generations: '))
    assert generations > 0

    index = dataset.countries.index(country)
    initial_vector = numpy.zeros(len(dataset.countries))
    initial_vector[index] = 1

    power = math_utils.normalize(numpy.linalg.matrix_power(normalized_population_matrix, generations))
    if not math_utils.is_normalized(power) or not math_utils.is_positive(power):
        print('Precision error, too many generations')
        return
    result = power @ initial_vector

    result_tuples = sorted(zip(dataset.countries, result), key=lambda k: k[1], reverse=True)

    included_countries: list[tuple[str, int]] = []
    max_name_length: int = len('Others')
    included_percentage: int = 0
    index: int = 0
    for country, value in result_tuples:
        if value > 0.01 or index < 10:
            included_countries.append((country, value))
            max_name_length = max(max_name_length, len(country))
            included_percentage += value
        index += 1
    print(f'+{"":-<{max_name_length + 2}}+---------+')
    for country, value in included_countries:
        print(f'| {country:{max_name_length}} | {round(float(value) * 100, 2):6}% |')
    print(f'+{"":-<{max_name_length + 2}}+---------+')
    print(f'| {"Others":{max_name_length}} | {round(float(1 - included_percentage) * 100, 2):6}% |')
    print(f'+{"":-<{max_name_length + 2}}+---------+')


if __name__ == '__main__':
    main()
