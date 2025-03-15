def count_xmas(array):
    nrow = len(array)
    ncol = len(array[0])
    counter = 0
    search = "MAS"
    nsearch = len(search)

    def search_right_down(i, j):
        for x in range(nsearch):
            if array[i + x][j + x] != search[x]:
                break
        else:
            return True

        for x in range(nsearch):
            if array[i + x][j + x] != search[nsearch - 1 - x]:
                break
        else:
            return True

        return False

    def search_left_down(i, j):
        for x in range(nsearch):
            if array[i + x][j - x] != search[x]:
                break
        else:
            return True

        for x in range(nsearch):
            if array[i + x][j - x] != search[nsearch - 1 - x]:
                break
        else:
            return True

        return False

    for i in range(nrow - nsearch + 1):
        for j in range(ncol - nsearch + 1):
            if search_right_down(i, j):
                if search_left_down(i, j + nsearch - 1):
                    counter += 1

    return counter


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        array = [[c for c in line.strip()] for line in f]

    print(count_xmas(array))
