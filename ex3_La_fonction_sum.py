def somme(lists):
    som = 0
    for list in lists:
        som += list
    return som

a=[2,3,4,5,5,5,6]

print(f"the sum of numbers in the list a is {somme(a)}")