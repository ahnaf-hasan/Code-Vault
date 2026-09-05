A = [[10,27,33],
    [14 ,15,16],
    [17 ,18,29]]

B = [[25,18,11,12],
    [66,67,33,0],
    [24,55,99,1]]

result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]


for i in range(len(A)):
  
   for j in range(len(B[0])):
       
       for k in range(len(B)):
           result[i][j] += A[i][k] * B[k][j]

for r in result:
   print(r)
