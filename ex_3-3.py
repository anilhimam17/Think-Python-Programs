''' Write a function that draws a grid like the following:
+ - - - - + - - - - +
| | | | | | | | | | |
+ - - - - + - - - - +
| | | | | | | | | | |
+ - - - - + - - - - +
'''

#We are splitting the pattern into two functions
#Function 1: | | | |
def stand_lines(n):
    stand_str = " | "
    print(stand_str * n)


#Function 2: - - - -
def sleep_lines(n):
    sleep_str = " - "
    print(sleep_str * n, end = "")


def plus(n):
    plus_str = " + "
    print(plus_str * n, end = "")


row = int(input("Enter the no of rows: "))

for i in range(1, row+1):
    for j in range(3):
        if j == 2:
            plus(1)
            print()
        else:
            plus(1)
            sleep_lines(4)

    if i == row:
        stand_lines(11)
        for j in range(3):
            if j == 2:
                plus(1)
                print()
            else:
                plus(1)
                sleep_lines(4)

    else:
        stand_lines(11)
    
            
