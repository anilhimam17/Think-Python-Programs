with open("words.txt", "r") as myfile:
    lines = myfile.readlines()
    

def has_no_e():
    print("The words that have no e are as follows:")
    
    no_e = 0
    for i in lines:
        if "e" not in i:
            print(i)
            no_e += 1
            
    print("\nThe no of words that have no e are: ", no_e)
    percent = (no_e / len(lines)) * 100
    print("The percent of lines that have no e are: ", percent)
    

has_no_e()
