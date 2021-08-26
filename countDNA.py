def processSequence():
    # creates dictionary for nucleotide count
    nucleotides = {
        "A": 0,
        "C": 0,
        "G": 0,
        "T": 0
    }
    # gets sequence
    sequence = input("Please enter the DNA sequence here:\n")
    
    # iterates throught the sequence and increments for each nucleotide
    for nucleotide in sequence:
        nucleotides[nucleotide] += 1

    # prints results
    print(f'{nucleotides["A"]} {nucleotides["C"]} {nucleotides["G"]} {nucleotides["T"]}') 

if __name__ == '__main__':
    processSequence()