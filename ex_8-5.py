def main():
    
    string = input("Enter the message to be encrypted by Caesar Rotation: ")
    rot = int(input("Enter the now of rotations to be made: "))
    print("The program is processing the output........")
    
    result = Caesar(string, rot)
    print("The encrypted string is: ", end = "")

    for i in result:
        print(i, end = "")

    print()


def Caesar(string, rot):

    new_vals = []
    for i in range(len(string)):
        
        if string[i].isspace():
            new_vals.append(string[i])

        elif string[i].isalpha():
            
            if string[i].islower():
                val = ord(string[i]) + rot % 26
                if val < 122:
                    new_vals.append(chr(val))
                else:
                    wrap = (val - 122) + 96
                    new_vals.append(chr(wrap))
                
            else:
                val = ord(string[i]) + rot % 26
                if val < 90:
                    new_vals.append(chr(val))
                else:
                    wrap = (val - 90) + 64
                    new_vals.append(chr(wrap))

        else:
            new_vals.append(string[i])

    return new_vals


if __name__ == "__main__":
    main()
