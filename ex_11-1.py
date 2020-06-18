from sys import argv


def main():
    word_dict = {}

    for i in lines:

        if i not in word_dict:
            word_dict[i] = 0

        else:
            word_dict[i] += 1

    print("The count for each of the words read is: \n", word_dict.items())
    

if open(argv[1]) != None:
    with open(argv[1], "r") as myfile:
        lines = myfile.readlines()

    if __name__ == "__main__":
        main()

else:
    sys.exit(1)
    
