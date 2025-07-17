if __name__ == '__main__':
    n = int(input())
    if n>1 and n<11:
        student_marks = {}
        for i in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores
        query_name = input()
        if query_name in student_marks:
            avrage=sum(student_marks[query_name])/ len(student_marks[query_name])
            print(f'{avrage:.2f}')
        else:
            print("Student not found")
    else:
        print("Wrong")
