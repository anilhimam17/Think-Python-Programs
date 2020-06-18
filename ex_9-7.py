with open("words.txt", "r") as myfile:
    lines = myfile.readlines()


def main():
    for i in lines:
        if recurr(i):
            print(i)


def recurr(word):
    w_len = len(word)
    i = 0
    count = 0

    while i < w_len:
        if i + 1 < w_len - 1 and word[i] == word[i + 1]:
            count += 1
            if count == 3:
                return True
            i += 2
        else:
            i = i + 1 - 2 * count
            count = 0


main()

            
