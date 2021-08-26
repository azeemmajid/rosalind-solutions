def calculate():
    dominantStr = input("Please enter the amount of individuals who are homozygous dominant for the factor:\n")
    heterozygousStr = input("Please enter the amount of individuals who are heterozygous for the factor:\n")
    recessiveStr = input("Please enter the amount of individuals who are homozygous recessive for the factor:\n")

    # converts into integer and then finds population size
    dominant = int(dominantStr)
    heterozygous = int(heterozygousStr)
    recessive = int(recessiveStr)
    population = dominant + heterozygous + recessive

    # all cases that contain a dominant allele
    domCases = [
        (dominant*(dominant-1))/population/(population-1), # AA x AA
        (dominant*heterozygous)/population/(population-1), # AA x Aa
        (dominant*recessive)/population/(population-1), # AA x aa
        (heterozygous*dominant)/population/(population-1), # Aa x AA
        (heterozygous*(heterozygous-1)*0.75)/population/(population-1), # Aa x Aa x 0.75, 25% chance of aa
        (heterozygous*recessive*0.5)/population/(population-1), # Aa x aa x 0.5, 50% of aa
        (recessive*dominant)/population/(population-1), # aa x AA
        (recessive*heterozygous*0.5)/population/(population-1) # aa x Aa x 0.5, 50% of aa
    ]

    print(round(sum(domCases), 5))

calculate()