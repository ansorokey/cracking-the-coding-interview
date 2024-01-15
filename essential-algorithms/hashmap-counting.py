def hashmapCount(it):
    counts = {}

    for x in it:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    
    for key in counts:
        print(counts[key])
