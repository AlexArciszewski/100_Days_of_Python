def data_container() -> None:
    student_scores = {
        'Harry': 88,
        'Ron': 78,
        'Hermione': 95,
        'Draco': 75,
        'Neville': 60
    }
    names_list = []
    for name in student_scores.keys():
        names_list.append(name)
    print(names_list)

    scores_list = []
    for score in student_scores.values():
        scores_list.append(score)
    print(scores_list)

    grades = []
    for score in scores_list:
        if score > 91:
            grade = "Outstanding"
            grades.append(grade)
        elif score > 80 and score < 91:
             grade = "Exceeds Expectations"
             grades.append(grade)
        elif score > 71 and score < 80:
             grade = "Acceptable"
             grades.append(grade)
        elif score < 70:
             grade = "Fail"
             grades.append(grade)
        else:
             print("error")
    print(grades)
    students_grades = dict(zip(names_list, grades))
    print(students_grades)
    # students_grades = {}
    # grade = None
    # for key, value in students_grades.items():
    #     if value > 91:
    #         grade == "Outstanding"
    #     elif value > 80 and value < 91:
    #         grade == "Exceeds Expectations"
    #     elif value > 71 and value < 80:
    #         grade == "Acceptable"
    #     elif value < 70:
    #         grade == "Fail"
    #     else:
    #         print("error")
    #
    # print(key, grade)




def main() -> None:
    data_container()



if __name__ == "__main__":
    main()

