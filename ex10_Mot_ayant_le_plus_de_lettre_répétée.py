from collections import Counter
def mot_lettre_repetee(lists):
    greatest =""
    p=0
    for i in lists:
        counter = Counter(i)
        most_common = counter.most_common(1)
        letter, count = most_common[0]

        if count > p:
            p = count
            greatest = i

    print(greatest)
    return greatest, letter


mot_lettre_repetee(["On", "a", "effectuee", "plusieurs", "tests", "elementaire", "ce", "matin"])