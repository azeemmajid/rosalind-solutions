# multipliers for the likelihood that an offspring will display dominant phenotype
# order correlates to order inputs should be given
multipliers = [1, 1, 1, 0.75, 0.5, 0]

def main():
    offspringCnt = 0
    # takes couple input in order of AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa
    coupleCnt = input("Please enter the couple counts separated by spaces:\n")
    # converts input into an array
    coupleCnt = coupleCnt.split(" ")

    # for each entry assumes that each couple has 2 children and
    # multiplies it by the likelihood the children will be dominant phenotype
    for indx, val in enumerate(coupleCnt):
        offspringCnt += int(val)*2*multipliers[indx]

    print(offspringCnt)

main()