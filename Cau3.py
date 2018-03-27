import numpy as np

def matrix_square(matrix):#kiểm tra có phải là matrix square hay ko
	iSize = len(matrix[0])
	sum_list = []
	
	#cộng theo chiều dọc:
	for col in range(iSize):
		sum_list.append(sum(row[col] for row in matrix))
	
	#cộng theo hàng ngang
	sum_list.extend([sum (lines) for lines in matrix])
	
	#cộng theo đường chéo
	dlResult = 0
	for i in range(0,iSize):
		dlResult +=matrix[i][i]
	sum_list.append(dlResult)  
 	
	if len(set(sum_list))>1:
		return False
	return True

a=[[4, 9, 2], [3, 5, 7], [8, 1, 6]]

print(matrix_square(a))