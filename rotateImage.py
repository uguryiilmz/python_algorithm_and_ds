

def rotateImage(matrix):
    row=len(matrix)
    col=len(matrix[0])
    matrix=matrix[::-1]
    for i in range(0,row):
        for j in range(i+1,col):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    return matrix


print(rotateImage([
    [1,2,3],
    [4,5,6],
    [7,8,9]
  ],))


print(5//2)