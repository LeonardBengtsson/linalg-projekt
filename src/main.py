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

    land = input("Välj land:")
    generations = int(input("Ange antalet generationer:"))

    dataset = get_data(Year.Y2020)
    
    land_index = dataset.countries.index(land)
    initial_vector = numpy.zeros(len(dataset.countries))
    initial_vector[land_index] = 1
    



    ims_matrix = dataset.ims_matrix
    emigration = numpy.sum(ims_matrix, axis = 0)

    immigration = numpy.sum(ims_matrix, axis = 1)
    natives = dataset.population - immigration 
    

    population_migration = math_utils.normalize(ims_matrix + numpy.diag(natives))

    result = numpy.linalg.matrix_power(population_migration, generations) @ initial_vector

    tuples = sorted(zip(dataset.countries, result), key=lambda k: k[1])
    
    for country, value in zip(dataset.countries, result):
        print (country, float(value))




if __name__ == '__main__':
    main()
