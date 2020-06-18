'''Then modify the program to count the total number of words in the book, and the number of times each word is used.
   Print the number of different words used in the book.'''
import string

def main():
    with open("Rumpty-Dudget's Tower.txt", "r") as myfile:
        lines = myfile.readlines()

    for i in range(len(lines)):
        if "IN 1877" in lines[i]:
            lines = lines[i:]
            break

    freq_calc(lines)


def freq_calc(lines):

    words = {}
    no_of_words = 0
    
    for i in lines:
        for j in i.split():
            if j[-1] in string.punctuation:
                j[:-1].strip()
                if j[:-1] in words:
                    words[j[:-1]] += 1

                else:
                    words[j[:-1]] = 0
                    no_of_words += 1

            elif j.isalpha():
                if j in words:
                    words[j] += 1

                else:
                    words[j] = 0
                    no_of_words += 1
                

    print(f"The total no of words found was: {no_of_words}")
    print("The top twenty repeated words are: ")

    top_words = list(words.items())
    top_words.sort(reverse = True)

    for i in range(20):
        print(top_words[i])
        

    
if __name__ == "__main__":
    main()
    
