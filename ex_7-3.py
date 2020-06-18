from math import pi


def main():
    result = Ramanujan_Function()
    print("The closest estimate to pi by the Ramanujan Function is: ",
          result)


def Ramanujan_Function():
    op_1 = (2 * (2 ** 0.5)) / 9801
    sum_val = 0
    k = 0
    run = True

    while run:
        numerator = factorial(4 * k) * (1103 + 26390 * k)
        denominator = (factorial(k) ** 4) * (396 ** (4 * k))
        val = op_1 * (numerator / denominator)
        sum_val += val

        if abs(val) < 1e-15:
            run = False

        else:
            k += 1

    return 1 / sum_val
        

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    main()
