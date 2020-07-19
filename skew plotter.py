def skewplot (genome):
    skew = 0
    skewlist = [0]
    for i in range (len(genome)):
        if genome[i]=='C':
            skew = skew - 1
            skewlist.append(skew)
        elif genome[i]=='G':
            skew = skew + 1
            skewlist.append(skew)
        else:
            skew = skew
            skewlist.append(skew)
    import matplotlib.pyplot as plt
    plt.plot(skewlist)
    plt.show()
    return;

skewplot(genome = 'CATGGGCATCGGCCATACGCC')
