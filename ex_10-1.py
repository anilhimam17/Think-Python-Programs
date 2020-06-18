def main():
    ls = []

    rows = int(input("Enter the no of rows: "))
    cols = int(input("Enter the no of cols: "))

    for i in range(rows):
        row = []
        for j in range(cols):
            inp = int(input("Enter an integer to be evaluated: "))
            row.append(inp)

        ls.append(row)

    result = calc_sum(ls)
    print("The sum of all the elements of the given nested list is: ", result)


def calc_sum(ls):
    sum_val = 0

    for i in ls:
        for j in i:
            sum_val += j

    return sum_val


if __name__ == "__main__":
    main()
    
