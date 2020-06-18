import math


def main():
    inp = int(input("Please enter the upper limits for the sqrt to be found: "))
    print("a", "\t", "mysqrt(a)", "\t", "math.sqrt(a)", "\t", "diff")
        
    for i in range(1, inp + 1):
        result = round(mysqrt(i), 5)
        m_sqrt = round(math.sqrt(i), 5)
        diff = round(result - m_sqrt, 5)

        print(i, "\t", result, "\t", m_sqrt, "\t", diff)


def mysqrt(a):
    x = 3
    sqrt = (x + a / x) / 2
    return sqrt


if __name__ == "__main__":
    main()

    
