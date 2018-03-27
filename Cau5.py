#Sử dụng matplotlib.pyplot.plot vẽ các đồ thị hàm số f(x) = (e^(−x/10))*sin(πx) and g(x) = x*e^(−x/3)
# trong khoảng [0, 10] trên cùng một biểu đồ. Bao gồm trục x, trục y và các chú thích các đường biểu diễn của từng hàm số.
# Lưu đồ thì thành một file plot.jpg (“Jpeg”)
import math as m
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-20., 20., 0.2)
y=(m.e**(-x/10)) * np.sin(m.pi*x)
g= x*(m.e**(-x/3))

# vẽ đồ thị với đường màu xanh liền 'b-'
plt.plot(x,y,'b-', label='f(x) = (e^(−x/10))*sin(πx)')

# vẽ đồ thị với đường màu đỏ liền 'r-'
plt.plot(x,g,'r-', label='g(x) = x*e^(−x/3)')

# đánh dấu trục x, trục y
plt.xlabel('x')
plt.ylabel('y')

# hiển thị đồ thị trong đoạn [0, 10] ở trục x và [-5, 10] ở trục y
plt.axis([0, 10, -5, 10])
#lưu ảnh
plt.savefig('plot.jpg')

plt.legend()
plt.show()