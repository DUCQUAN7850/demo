import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame, Series
# đọc file
df = pd.read_csv('pokemon.csv', sep=',')
#lưu các giá trị trong cột attack và speed vào 2 danh sách
a=df['Attack']
b=df['Speed']
#in ra các row có attack >52 và speed >80
for i in range(0,len(df)):
	if (a[i]>52) and (b[i]>80):
		print(df.iloc[[i]])
#vẽ các điểm có tọa độ (attack, speed) trên mặt phẳng tọa độ
plt.plot([a],[b], 'ro')
plt.axis([0,200,0,200])
plt.ylabel('Speed')
plt.xlabel('Attack')
plt.show()