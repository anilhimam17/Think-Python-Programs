def main():
    ls = []

    ls_len = int(input("Enter the number of elements to be entered into \
the list: "))

    for i in range(ls_len):
        inp = int(input("Enter the element to be appended into the list: "))
        ls.append(inp)

    result = cumsum(ls)
    print("The resultign list after all the calculation is: ", result)


def cumsum(ls):
    sum_val = 0

    for i in ls:
        sum_val += i

    ls[-1] = sum_val
    return ls


if __name__ == "__main__":
    main()
