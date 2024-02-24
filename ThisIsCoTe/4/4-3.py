# 실전문제: 왕실의 나이트 
import sys

dx = [-1, 1, -1, 1, -2, -2, 2, 2]
dy = [-2, -2, 2, 2, 1, -1, -1, 1 ]
type = ['UL', 'UR', 'DL', 'DR', 'LL', 'LR', 'RL', 'RR']

x_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# a1 -> [a, 1] -> [1, 1]
start = list(input())
start_x = x_list.index(start[0])
start[0] = start_x

available_cnt = 0
for mx, my, type in zip(dx, dy, type) :
    sx, sy = map(int, start)
    fx = sx + mx 
    fy = sy + my 
    if (fx > 0 and fy > 0) and (fx <= 9 and fy <= 9):
        available_cnt += 1

print(available_cnt)