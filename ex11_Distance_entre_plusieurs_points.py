# Noukoundido
def dis_point(lists):
    new_lists = []
    for i in range(len(lists) - 1):
        new_lists.append(abs(lists[i] - lists[i+1])) 

    print(new_lists)
    return new_lists

pi = [40, 54, 59,60, 45]
dis_point(pi)