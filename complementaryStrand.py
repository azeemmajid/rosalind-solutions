def getStrand():
    secondStrand = ""

    dnaSequence = input("Please enter a DNA sequence to find the complementary strand:\n")

    for nucleotide in dnaSequence:
        if nucleotide == "A":
            secondStrand = "T" + secondStrand
        elif nucleotide == "C":
            secondStrand = "G" + secondStrand
        elif nucleotide == "G":
            secondStrand = "C" + secondStrand
        elif nucleotide == "T":
            secondStrand = "A" + secondStrand
    
    print(secondStrand)

if __name__ == '__main__':
    getStrand()