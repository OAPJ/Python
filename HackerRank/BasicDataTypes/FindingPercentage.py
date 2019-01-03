if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    suma_calificaciones = student_marks[query_name][0] + student_marks[query_name][1]+ student_marks[query_name][2]
    print("{0:.2f}".format(suma_calificaciones/3))
