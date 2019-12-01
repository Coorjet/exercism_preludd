def distance(strand_a, strand_b):
    distanceValue = 0
    if ( len(strand_a) != len(strand_b)):
        raise ValueError("Distance between two strands of different sizes is nonsense")
    for i in range(len(strand_a)):
        if (strand_a[i] != strand_b[i]):
            distanceValue+=1
    return distanceValue   
