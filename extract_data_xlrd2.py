'''This is an exmaple of using xlrd parsing excel file'''

"""
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples
"""

import xlrd
from zipfile import ZipFile
import pprint

datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

    cv = sheet.col_values(1, start_rowx=1, end_rowx=None) # a list
    max_val = max(cv)
    min_val = min(cv)

    max_i = cv.index(max_val) + 1 #cv starts from row1 in original data not row0
    min_i = cv.index(min_val) + 1

    max_time = sheet.cell_value(max_i, 0)
    max_stamp = xlrd.xldate_as_tuple(max_time,0)
    min_time = sheet.cell_value(min_i, 0)
    min_stamp = xlrd.xldate_as_tuple(min_time, 0)


    data = {
        'maxtime': max_stamp,
        'maxvalue': max_val,
        'mintime': min_stamp,
        'minvalue': min_val,
        'avgcoast': sum(cv)/float(len(cv))
    }
    return data

data = parse_file(datafile)
pprint.pprint(data)


test()
