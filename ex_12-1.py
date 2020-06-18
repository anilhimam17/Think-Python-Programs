import time
import matplotlib.pyplot as plt

def main():
    alpha = {}
    for i in range(97, 123):
        alpha[chr(i)] = 0
    print("The initial dictionary for the frequency of all the alphabets is: \n", alpha)

    string = input("Enter the string to find the frequency of all the alphabets being used: ")
    freq_calc(string, alpha)

    keys = []
    counts = []
    for i, j in alpha.items():
        keys.append(i)
        counts.append(j)

    plt.figure(figsize = (10, 8))
    plt.bar(keys, counts)
    plt.tight_layout()
    plt.show()


def freq_calc(string, alpha):
    for i in string:
        for j in i:
            j.lower()
            if j in alpha:
                alpha[j] += 1

            else:
                continue
    

if __name__ == "__main__":
    main()

