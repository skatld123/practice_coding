import sys

input = sys.stdin.readline

while True:
    a, b, c= map(int, input().rstrip().split())
    if a == 0 and b == 0 and c == 0:
        break

    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("Equilateral")
        elif a == b or b == c or a == c:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")
