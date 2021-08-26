def main():
    # list of all founds positions
    positions = []
    # gets string input
    str1 = input("Please enter the strand to search through:\n")
    str2 = input("Please enter the sequence to search for:\n")

    # finds sequence lenght
    seqLength = len(str2)

    # iterates through the DNA strand
    for i in range(len(str1)):
        # checks if current position has the sequence
        if str1[i:i+seqLength] == str2:
            # inserts as i+1 because rosalind wants the positions starting at 1
            positions.append(i+1)

    print(positions)

main()