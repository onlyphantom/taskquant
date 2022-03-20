def create_table(table, headers=None):

    if headers:
        headerstring = "\t{}\t" * len(headers)
        print(headerstring.format(*headers))

    rowstring = "\t{}\t" * len(table[0])

    for row in table:
        print(rowstring.format(*row))
