def pal(inp):

    if len(inp) < 1:
        return True

    else:
        if inp[0] == inp[-1]:
            return pal(inp[1:-1])

        else:
            return False

inp = input("Enter the string to check whether palindome or not: ")

if pal(inp):
    print("The given string is a palindrome")

else:
    print("The given string is not a palindrome")
    
