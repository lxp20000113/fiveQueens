from z3 import *

s = Solver()

'''
我们这里需要创建一个[5][5]的矩阵，表明该位置上是否有皇后，当为1时，证明有皇后；为0时，证明没有皇后。
'''

n = 4
Isempress = [[Int("x_%s_%s" % (i, j)) for j in range(n)] for i in range(n)]
print(type(Isempress[0][0]))
'''保证每个位置只有0和1的取值, 1为有皇后 2为无皇后'''
cells_c = [Or(Isempress[i][j] == 0, Isempress[i][j] == 1) for i in range(n) for j in range(n)]
'''保证同一行只有一个皇后,保证同一列只有一个皇后'''
rows = [Sum(Isempress[i]) == 1 for i in range(n)]
cols = [Sum([Isempress[i][j] for i in range(n)]) == 1 for j in range(n)]
'''保证同对角线只有一个皇后'''
diagonals1 = [And(Sum([Isempress[i+k][k] for k in range(n-i)]) <= 1,
                  Sum([Isempress[k][i+k] for k in range(n-i)]) <= 1) for i in range(n)]
diagonals2 = [And(Sum([Isempress[k][n-1-i-k] for k in range(n-i)]) <= 1,
                  Sum([Isempress[i+k][n-1-k] for k in range(n-i)]) <= 1) for i in range(n)]

s.add(cells_c + rows + cols + diagonals1 + diagonals2)
check = s.check()
print(check)
if check == sat:
    m = s.model()
    print(m)
else:
    print("Failed solve")