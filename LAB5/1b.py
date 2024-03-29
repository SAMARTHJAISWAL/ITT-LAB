m = [[1,2,3],[4,5,6],[7,8,9]]
for i in range (3):
    print(i)
    for j in range (3):
        t=m[i][j]
        m[i][j]=m[j][i]
        print(m[i][j])
    
