def count_xmas(array):
    nrow = len(array)
    ncol = len(array[0])
    counter = 0
    search = "XMAS"
    nsearch = len(search)

    def search_right(i, j):
        nonlocal counter

        if j > (ncol - nsearch):
            return

        for x in range(nsearch):
            if array[i][j + x] != search[x]:
                break
        else:
            counter += 1

        for x in range(nsearch):
            if array[i][j + x] != search[nsearch - 1 - x]:
                break
        else:
            counter += 1

    def search_down(i, j):
        nonlocal counter

        if i > (nrow - nsearch):
            return

        for x in range(nsearch):
            if array[i + x][j] != search[x]:
                break
        else:
            counter += 1

        for x in range(nsearch):
            if array[i + x][j] != search[nsearch - 1 - x]:
                break
        else:
            counter += 1

    def search_right_down(i, j):
        nonlocal counter

        if i > (nrow - nsearch) or j > (ncol - nsearch):
            return

        for x in range(nsearch):
            if array[i + x][j + x] != search[x]:
                break
        else:
            counter += 1

        for x in range(nsearch):
            if array[i + x][j + x] != search[nsearch - 1 - x]:
                break
        else:
            counter += 1

    def search_left_down(i, j):
        nonlocal counter

        if i > (nrow - nsearch) or j < (nsearch - 1):
            return

        for x in range(nsearch):
            if array[i + x][j - x] != search[x]:
                break
        else:
            counter += 1

        for x in range(nsearch):
            if array[i + x][j - x] != search[nsearch - 1 - x]:
                break
        else:
            counter += 1

    for i in range(nrow):
        for j in range(ncol):
            search_right(i, j)
            search_down(i, j)
            search_right_down(i, j)
            search_left_down(i, j)

    return counter


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        array = [[c for c in line.strip()] for line in f]

    print(count_xmas(array))
