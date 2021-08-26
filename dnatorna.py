def transcribe():
    rnaSequence = ""

    dnaSequence = input("Please enter a DNA sequence to be transcribed here:\n")

    for nucleotide in dnaSequence:
        if nucleotide == "T":
            rnaSequence += "U"
        else:
            rnaSequence += nucleotide
    
    print(rnaSequence)

if __name__ == '__main__':
    transcribe()