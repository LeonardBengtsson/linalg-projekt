import numpy

from data.data import DataSet, Year, get_data
import data.data
import math_utils


def main():
    dataset = DataSet(
        Year.Y2020,
        [ 'A', 'B', 'C' ],
        numpy.array([ 1000, 2000, 3000 ]),
        numpy.array([
            [ 0, 2, 2660 ],
            [ 10, 0, 30 ],
            [ 100, 200, 0 ]
        ])
    )

    dataset = get_data(Year.Y2020)
    ims_matrix = dataset.ims_matrix
    emigration = numpy.sum(ims_matrix, axis=0)

    immigration = numpy.sum(ims_matrix, axis=1)
    natives = dataset.population - immigration
    population_migration = math_utils.normalize(ims_matrix + numpy.diag(natives))

    land = input('Choose country: ').strip()
    assert land in dataset.countries
    generations = int(input('Choose how many generations: '))
    assert generations > 0

    land_index = dataset.countries.index(land)
    initial_vector = numpy.zeros(len(dataset.countries))
    initial_vector[land_index] = 1

    result = numpy.linalg.matrix_power(population_migration, generations) @ initial_vector

    tuples = sorted(zip(dataset.countries, result), key=lambda k: k[1], reverse=True)

    included_countries: list[tuple[str, int]] = []
    max_name_length: int = len('Others')
    included_percentage: int = 0
    for country, value in tuples:
        if value > 0.01:
            included_countries.append((country, value))
            max_name_length = max(max_name_length, len(country))
            included_percentage += value
    print(f'+{'':-<{max_name_length + 2}}+---------+')
    for country, value in included_countries:
        print(f'| {country:{max_name_length}} | {round(float(value) * 100, 2):6}% |')
    print(f'+{'':-<{max_name_length + 2}}+---------+')
    print(f'| {'Others':{max_name_length}} | {round(float(1 - included_percentage) * 100, 2):6}% |')
    print(f'+{'':-<{max_name_length + 2}}+---------+')


if __name__ == '__main__':
    main()
