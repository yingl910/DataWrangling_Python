'''This is a simple example of using csv module reading csv file, specifically the dictionary reader'''

# assume first row is header;
# create a dictionary for each row;
# deal with quotes and other small problems

import os
import pprint
import csv

DATADIR = ""
DATAFILE = "beatles-diskography.csv"

def parse_csv(datafile):
    data = []
    with open(datafile, "r") as sd:

        r = csv.DictReader(sd)
        for line in r:
            data.append(line)

    return data


if __name__ == '__main__':
    datafile = os.path.join(DATADIR,DATAFILE)
    parse_csv(datafile)
    d = parse_csv(datafile)
    pprint.pprint(d)
