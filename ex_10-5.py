def main():
    ls = []

    ls_len = int(input("Enter the number of elements to be entered into \
the list: "))

    for i in range(ls_len):
        inp = int(input("Enter the element to be appended into the list: "))
        ls.append(inp)

    if is_sorted(ls):
        print("The given list is sorted in ascending order")
    else:
        print("Nah the given list is not sorted, what waste of time")


def is_sorted(ls):

    for i in range(len(ls)):
        if i + 1 < len(ls) - 1 and ls[i] > ls[i + 1]:
            break
    else:
        return True

    return False


if __name__ == "__main__":
    main()
