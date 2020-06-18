def main():
    ls = []

    ls_len = int(input("Enter the number of elements to be entered into \
the list: "))

    for i in range(ls_len):
        inp = int(input("Enter the element to be appended into the list: "))
        ls.append(inp)

    result = middle(ls)
    print("The resulting list is: ", result)


def middle(ls):
    n_ls = []

    for i in range(len(ls)):
        if i == 0 or i == len(ls) - 1:
            continue
        else:
            n_ls.append(ls[i])

    return n_ls


if __name__ == "__main__":
    main()
