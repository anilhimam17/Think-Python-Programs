import random


def main():
    inp = int(input("Enter the number of student present in the class: "))
    b_days = []

    for i in range(inp):
        day = random.randint(1, 365)
        b_days.append(day)
    
    prob = paradox_check(b_days)
    print("The probability that the b_days match for to students is: ", prob)


def paradox_check(b_days):

    count_double = 0

    for i in range(len(b_days)):
        for j in range(len(b_days)):
            if i != j and b_days[i] == b_days[j]:
                count_double += 1

    return round(count_double / len(b_days), 2)


if __name__ == "__main__":
    main()

                
    
