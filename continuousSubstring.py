
def losers(winners, winners_update):
    """ returns list of indicies of elements in winners for elements that are not in winners_update
        winners: list of indicies in arr
        winners_update: list of ints, a subset of winners"""
    loosers = []
    c = 0
    for a in range(len(winners)):
        b = a - c
        if b == len(winners_update) or winners_update[b] != winners[a]:
            loosers.append(a)
            c += 1
    return loosers

def contiguous_substring(arr):
    """ input: list of distinct integers
        output: list of contiguous substring begginging at each index"""
    out = [1] * len(arr)    # innitializing every output to 1 because every element in input has a len one solution
    winners = []    # a list of indicies for winning numbers, arr[i]
    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            if len(winners) == 0 or winners[-1] != i-1:
                winners.append(i-1)
        else: winners.append(i)

    while len(winners) > 1:
        winners_update = []
        for j in range(1,len(winners)): # update winners by walking through it once
            if arr[winners[j]] < arr[winners[j-1]]: 
                if len(winners_update) == 0 or winners_update[-1] != winners[j-1]:
                    winners_update.append(winners[j-1])
            else:winners_update.append(winners[j])

        loosers = losers(winners, winners_update)   # this wallks through winners once to generate loosers
        for l in loosers:   # generate output for each loser
            if l-1 >= 0: out[winners[l]] += (winners[l] - winners[l-1] -1)
            else: out[winners[l]] += winners[l]
            if l+1 < len(winners): out[winners[l]] += (winners[l+1] - winners[l] - 1)
            else: out[winners[l]] += len(arr) -1 - winners[l]
        winners = winners_update
    out[winners[0]] = len(arr) # this big guy is our global maximum, who's output number is always the length of the input list
    return out

def test():
    arr = [3,4,1,6,2]
    assert(contiguous_substring(arr) == [1, 3, 1, 5, 1])

    arr = [8,9,4,2,3,5]
    assert(contiguous_substring(arr) == [1, 6, 3, 1, 2, 4])

    arr = [38, 6, 18, 40, 43, 10, 29]
    assert(contiguous_substring(arr) == [3, 1, 2, 4, 7, 1, 2])

    arr = [23,10,21,13,3,4,14,18,11,5]
    assert(contiguous_substring(arr) == [10, 1, 9, 3, 1, 2, 4, 7, 2, 1])

    arr = [5,4,3,2,1]
    assert(contiguous_substring(arr) == [5, 4, 3, 2, 1])

    arr = [1,2,3,4,5]
    assert(contiguous_substring(arr) == [1, 2, 3, 4, 5])
    print("All tests passed!")

test()