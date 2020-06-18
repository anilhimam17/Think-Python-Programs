def main():
    ls = []

    ls_len = int(input("Enter the number of elements to be entered into the\
 list: "))

    for i in range(ls_len):
        inp = int(input("Enter the elements to be entered into the list: "))
        ls.append(inp)

    ser_ele = int(input("Enter the element to be searched in the list: "))

    ls.sort()
    result = bin_search(ls, ser_ele, ls_len, 0)
    if result:
        print("The search element was found in the index: ", result)
    else:
        print("The search element was not found in the list")


def bin_search(ls, ser_ele, high, low):
    if high >= low:
        mid = int((high + low) / 2)

        if ls[mid] == ser_ele:
            return mid

        elif ls[mid] > ser_ele:
            return bin_search(ls, ser_ele, mid - 1, low)

        else:
            return bin_search(ls, ser_ele, high, mid + 1)

    else:
        return False


if __name__ == "__main__":
    main()
        
