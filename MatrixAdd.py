# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]

def matrix(m,n): # 3 * 3
    o = []
    for i in range(m): #3
        row = []
        for j in range(n): #3
            inp = int(input(f" Enter o[{i}][{j}]")) # i = 0 1 2 j = 0 1 2 3
            row.append(inp)
        o.append(row)
    return o

def sum(A,B):
    output = []
    for i in range(len(A)): #Number of rows
        row = []
        for j in range(len(A[0])): #Num of columns
            row.append(A[i][j] + B[i][j]) # Adding the two Matrix
        output.append(row)
    return output



m = int(input("Enter the value of ROW\n"))
n = int(input("Enter the value of COLUMN\n"))

print("Enter the Matrix A")
A = matrix(m,n)
print(A)

print("Enter the Matrix B")
B = matrix(m,n)
print(B)


s = sum(A, B)
print(f" Sum is,{s}")