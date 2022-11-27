from z3 import *

s = Solver()

'''
我们这里需要创建一个[5][5]的矩阵，表明该位置上是否有皇后，当为1时，证明有皇后；为0时，证明没有皇后。
'''

n = 5
Isempress = [[] for i in range(n)]
for i in range(n):
    for j in range(n):
        Isempress[i].append(Bool(str(i) + "-" + str(j)))
print(type(Isempress[0][0]))
row = []

'''保证同一行只有一个皇后,保证同一列只有一个皇后'''
for i in range(n):
    s.add(Or(Isempress[i][j])for j in range(n))
    s.add(And(Not(And(Isempress[i][j], Isempress[i][k]))) for j in range(n) for k in range(j+1, n))
    s.add(Or(Isempress[j][i])for j in range(n))
    s.add(And(Not(And(Isempress[j][i], Isempress[k][i]))) for j in range(n) for k in range(j + 1, n))

'''保证同对角线只有一个皇后'''
for i in range(n-1):
    s.add(And(Not(And(Isempress[i+j][j], Isempress[i+k][k]))) for j in range(n-i) for k in range(j+1, n-i))
    s.add(And(Not(And(Isempress[j][i+j], Isempress[k][i+k]))) for j in range(n-i) for k in range(j+1, n-i))
    s.add(And(Not(And(Isempress[i+j][n-j], Isempress[i+k][n-k]))) for j in range(n-i) for k in range(j+1, n-i))
    s.add(And(Not(And(Isempress[j][n-i-j], Isempress[k][n-i-k]))) for j in range(n-i) for k in range(j+1, n-i))

check = s.check()
print(check)