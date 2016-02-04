from linalg import gaussian_elimination
from numpy import linalg

index = 0
def test(m, v):
    global index
    index += 1
    mine = gaussian_elimination(m, v)
    numpys = linalg.solve(m, v)
    if (mine == numpys).all():
        print("Pass", index)
    else:
        print("Fail", index, m, v)
        print(" Mine:", mine)
        print(" numpys:", numpys)

# Test first column.

#1
matrix = [
    [1,0,0],
    [0,1,0],
    [0,0,1]
]
vector = [1,1,1]
test(matrix, vector)

#2
matrix = [
    [1,0,0],
    [0,1,1],
    [0,0,1]
]
vector = [1,1,1]
test(matrix, vector)

#3
matrix = [
    [1,0,1],
    [0,1,1],
    [0,0,1]
]
vector = [1,1,1]
test(matrix, vector)

# And the second...
#4
matrix = [
    [1,1,0],
    [0,1,0],
    [0,0,1]
]
vector = [1,1,1]
test(matrix, vector)
#5
matrix = [
    [1,1,0],
    [0,1,0],
    [0,1,1]
]
vector = [1,1,1]
test(matrix, vector)

# Third
#6
matrix = [
    [1,0,0],
    [1,1,0],
    [0,0,1]
]
vector = [1,1,1]
test(matrix, vector)
#7
matrix = [
    [1,0,0],
    [1,1,0],
    [1,0,1]
]
vector = [1,1,1]
test(matrix, vector)

# Complex

matrix = [
    [2,2,3],
    [4,5,5],
    [1,2,1]
]
vector = [1,4,2]
test(matrix, vector)
