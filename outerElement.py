def outerElement(mat):
    length_i=len(mat)
    length_j=len(mat[0])
    arr1=mat[0]
    arr3=mat[length_i - 1][::-1]
    arr2=[]
    arr4=[]
    for i in range(1, length_i-1):
        for j in [0,length_j-1]:
            if j == 0:
                arr4.append(mat[i][j])
            else:
                arr2.append(mat[i][j])
    outpt = arr1+arr2+arr3+arr4[::-1]
    print(outpt)

mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
outerElement(mat)
