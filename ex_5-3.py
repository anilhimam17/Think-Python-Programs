

def main():
    a = int(input("Enter the value for side 1 of the traingle: "))
    b = int(input("Enter the value for side 2 of the traingle: "))
    c = int(input("Enter the value for side 3 of the traingle: "))

    is_triangle(a, b, c)
    
    
def is_triangle(a, b, c):
    if a > (b + c) or b > (c + a) or c > (a + b):
        print("No")

    else:
        print("The triangle can be formed")


if __name__ == "__main__":
    main()
