def calculateGCContent(fragment):
    # checks if strand is string or list
    if isinstance(fragment, list):
        fragment = ''.join(fragment)

    count = 0
    # loops through the string and counts all the G and Cs
    for i in fragment:
        if i == "G" or i == "C":
            count += 1
    
    return count/len(fragment)

# iterates through all the items to find the one with highest gc content
def compare(fragments):
    highestGCid = ""
    highestGCCount = 0
    for key in fragments:
        if fragments[key]["gcContent"] > highestGCCount:
            highestGCid = key
            highestGCCount = fragments[key]["gcContent"]

    print(highestGCid)
    print(highestGCCount)

def getInput():
    # initialized dictionary for fragment storage
    fragments = {}
    # reads file because taking FASTA format in terminal causes errors
    fragString = input("Please enter filename with DNA in FASTA format:\n")
    f = open(fragString, "r")
    fragmentsStr = f.read()
    # split first with \n> to get id and string pair + clean up id
    split = fragmentsStr.split("\n>")
    
    for p in split:
        # breaks it into id and string
        # collects all of strings in case they are split between multiple lines
        strandID, *strand = p.split("\n")
        # finds the gc content of each string
        gcContent = calculateGCContent(strand)
        fragments[strandID] = {
            "fragment": strand,
            "gcContent": gcContent
        }
    
    compare(fragments)
    
getInput()