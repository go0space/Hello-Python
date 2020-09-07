# Matplotlib
# 파이썬에서 데이터를 차트나 플롯으로 그려주는 라이브러리 패키지 -- 가장 많이 사용되는 데이터 시각화(Data Visualization) 패키지
# jupyter Notebbok을 사용하면 편리하다.

# 1
from Matplotlib import pyplot as plt

plt.plot([1,2,3], [110,130,120])
plt.show()

# 2
from matplotlib import pyplot as plt

plt.plot(["Seoul", "Paris", "Seattle"], [30,25,55])
plt.xlabel('city')
plt.ylabel('Response')
plt.title('Experiment Result')
plt.show()

# 3
from matplotlib import pyplot as plt
 
plt.plot([1,2,3], [1,4,9])
plt.plot([2,3,4],[5,6,7])
plt.xlabel('Sequence')
plt.ylabel('Time(secs)')
plt.title('Experiment Result')
plt.legend(['Mouse', 'Cat'])
plt.show()

# 4
from matplotlib import pyplot as plt
 
y = [5, 3, 7, 10, 9, 5, 3.5, 8]
x = range(len(y))
plt.bar(x, y, width=0.7, color="blue")
plt.show()