if __name__ == '__main__':
    student=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name, score])
    grades=sorted(set(score for name, score in student))
    second_grade=grades[1]
    second_lowest_student=[name for name , score in student if score == second_grade]
    for name in sorted(second_lowest_student):
        print(name)
