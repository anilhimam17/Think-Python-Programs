with open("words.txt", "r") as myfile:
    lines = myfile.readlines()

count_20 = 0

for i in lines:
    if len(i) > 20:
        count_20 += 1

print("The total no of words with length greater than 20 are: ", count_20)
