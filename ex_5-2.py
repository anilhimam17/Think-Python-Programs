'''Checking fermat's theorem a^n + b^n != c^n where n is greater than 2'''

def main():
    print("Please enter below the respective values for the equation:\n\
a^n + b^n = c^n\n")
    a = int(input("Enter the value for 'a' from the respective equation: "))
    b = int(input("Enter the value for 'b' from the respective equation: "))
    c = int(input("Enter the value for 'c' from the respective equation: "))
    n = int(input("Enter the value for 'n' from the respective equation: "))

    result = check_fermat(a, b, c, n)

    if result == 1:
        print("Holy smokes, Fermat was wrong")

    elif result:
        print("No that dosent work")

    else:
        print("The value of n should be greater than 2 please try again")
    

def check_fermat(a, b, c, n):

    if n > 2:
        val_left = a ** n + b ** n
        val_right = c ** n

        if val_left == val_right:
            return 1

        else:
            return 2

    else:
        return False

if __name__ == "__main__":
    main()
