#Sinh ngẫu nhiên một ma trận 100*100 giá trị các phần tử nằm trong khoảng (0, 100)
# rồi tìm định thức, ma trận chuyển vị, trị riêng và vector riêng của ma trận.
# Lưu kết quả vào một file output.txt
import numpy as np
from numpy import linalg as la
file = open("output1.txt", "w")
a=np.random.randint(0, 100, (100, 100))
print("ma trận a: \n",a)
np.savetxt(file, a,fmt='%.2f')

# ma trận chuyển vị
b = a.transpose()
print("ma trận chuyển vị: \n",b)
np.savetxt(file, b, fmt='%.2f')

#định thức
print ("Định thức của a = ",np.linalg.det(a))
file.write(str(np.linalg.det(a)))

w, v = la.eig(np.array(a))
# Danh sách trị riêng
print("Giá trị riêng: ",w)
np.savetxt(file, w, fmt='%.2f')
# Danh sách vector riêng
print("Vector riêng: ",v)
np.savetxt(file, v, fmt='%.2f')
file.close()