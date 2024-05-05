"""
    count the number of time a letter appaer in a string

"""

def lett_succ(strings):
    lis_tuples = []
    already = []

    for i in strings:

        if i not in already:
            already.append(i)
            lis = []
            lis.append(i)
            val=0
            for j in strings:
                if j == i:
                    val += 1
            lis.append(val) 
            # print(lis)
 
            lis_tuples.append(tuple(lis))

    print(lis_tuples)
    return lis_tuples

lett_succ("aaaccdaad")