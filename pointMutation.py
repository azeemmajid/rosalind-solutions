def countPointMutations():
    count = 0
    # gets string input
    str1 = input("Please enter the first strand:\n")
    str2 = input("Please enter the second strand:\n")

    # iterates through the string comparing values to check for point mutations
    for indx, value in enumerate(str1):
        if str1[indx] != str2[indx]:
            count += 1
    
    # prints out final difference count
    print(count)

countPointMutations()