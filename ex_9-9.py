def main():
    parent_age = input("Enter the age of the parent: ")
    child_age = input("Enter the age of the child: ")

    max_parent = 100
    pal_count = 0

    while int(parent_age) < 100:
        p_list = list(parent_age)
        c_list = list(child_age)
        parent_age.reverse()
        if child_age == parent_age.reverse():
            pal_count += 1
            parent_age = int(parent_age) + 1
            child_age = int(child_age) + 1
            parent_age.reverse()

    else:
        print("The total no of time this event is possible is: ", pal_count)


main()
        
        
