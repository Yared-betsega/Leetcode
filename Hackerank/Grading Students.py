def gradingStudents(grades):
    length = len(grades)
    for i in range(length):
        if grades[i] < 38:
            continue
        if (grades[i] + 1) % 5 == 0:
            grades[i] = grades[i] + 1
            continue
        if (grades[i] + 2) % 5 == 0:
            grades[i] = grades[i] + 2
    return grades
