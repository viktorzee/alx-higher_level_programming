def new_in_list(matrix = [[]]):
    for row in matrix:
        for val in row:
            print("{:d}".format(val), end=" " if val != row[-1] else "")
    print()
