def create_table(table, headers=None):
    if headers:
        table = [headers] + table

    longest_cols = [
        (max([len(str(row[i])) for row in table]) + 3) for i in range(len(table[0]))
    ]
    row_format = "".join(
        ["{:>" + str(longest_col) + "}" for longest_col in longest_cols]
    )
    for row in table:
        print(row_format.format(*row))
