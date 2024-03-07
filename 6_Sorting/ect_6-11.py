n = int(input())

students = []
for i in range(n):
    name, score = input().split()
    students.append((name, int(score)))

students.sort(key=lambda x : x[1])
for student in students:
    print(student[0], end=' ')