'''This is an example of processing file and using the csv module to extract data from it.'''


# 1. the first line of the datafile is neither data entry, nor header. It is a line describing the data source.
# extract the name of the station from it.

# 2. the data is returned as a list of lists (not dictionaries).

import csv
import os

DATAFILE = "745090.csv"


def parse_file(datafile):
    name = ""
    data = []
    with open(datafile, 'rb') as f:

        '''method #1
        source = f.readline().split(",")
        name = source[1].replace('"','')
        #skip the header line
        f.readline()
        energy_data = csv.reader(f)
        for d in energy_data:
            data.append(d) #type(d):list
        '''
        # use next()
        # type(f.next()) : string
        # type(f.next().split(",") : list
        name = f.next().split(",")[1].replace('"', '')
        f.next()
        '''
        for line in f:
            data.append(line) #line is string
        '''
        energy_data = csv.reader(f)
        for d in energy_data:
            data.append(d)

    return (name, data)


