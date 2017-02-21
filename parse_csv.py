'''This is an example of parsing CSV file, without using csv module'''

# 1. read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# 2. split each line on "," and then for each line, create a dictionary where the key is the header title of the field,
# and the value is the value of that field in the row.
# 3. the function parse_file should return a list of dictionaries, each data line in the file being a single list entry.
# 4. field names and values should not contain extra whitespace, like spaces or newline characters.
# 5. parse only the first 10 data lines in this exercise,

DATAFILE = "beatles-diskography.csv"

def parse_file(datafile):
    data = []
    with open(datafile, "r") as f:
        header = f.readline().split(",")
        counter = 0

        #as I already read header, this supposes to start from line 2 (first line that is not header)
        for line in f:
            if counter == 10:
                break

            fields = line.split(",")
            entry = {}

            for i, value in enumerate(fields):
                entry[header[i].strip()] = value.strip()

            data.append(entry)
            counter += 1

    return data

d = parse_file(DATAFILE)
print(d)

