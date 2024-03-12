# 람다를 활용하는 문제
n = int(input())

students = []
for i in range(n):
    name, kor, eng, math = input().split()
    students.append((int(kor), int(eng), int(math), name))
    
students.sort(key=lambda x:((-x[0]), x[1], (-x[2]), x[3]))

for stu in students:
    print(stu[3])