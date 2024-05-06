def decision(python,numpy,pandas,matplotlib ,abscence ,niveau):
    note_final = ((python * 3) + (pandas * 7) + (matplotlib *5) + (numpy * 4)) /19
    if abscence == 0:
        note_final = note_final + (note_final*0.1)

    else:
        for _ in range(abscence):
            note_final = note_final - (note_final*0.05)

    pass_grade = "Non"
    if niveau == 1 and note_final >= 12:
        pass_grade = "Oui"

    elif niveau == 2 and note_final >= 13.5:
        pass_grade = "Oui"

    elif niveau == 3 and note_final >= 14:
        pass_grade = "Oui"

    elif niveau == 4 and note_final >= 15:
        pass_grade = "Oui"

    elif niveau == 5 and note_final >= 17:
        pass_grade = "Oui"

    return pass_grade

