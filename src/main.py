import numpy

from data.data import DataSet, Year, get_data
import data.data


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
    print('Sweden population:', dataset.get_population('Sweden'))

    ims_matrix = dataset.ims_matrix
    sweden_index = dataset.countries.index('Sweden')
    norway_index = dataset.countries.index('Norway')

    sweden_to_norway = ims_matrix[norway_index, sweden_index]
    print('International migrant stock (Swedes living in Norway):', sweden_to_norway)

    norway_to_sweden = ims_matrix[sweden_index, norway_index]
    print('International migrant stock (Norwegians living in Sweden):', norway_to_sweden)


if __name__ == '__main__':
    main()
