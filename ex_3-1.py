'''A program to write a function write_justify to print enough leading spaces
for column 70'''

inp = input("Enter the inpute to be printed: ")

def right_justify(inp):
    print(" " * 69, end = "")
    print(inp)
    
right_justify(inp)
