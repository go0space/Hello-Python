# pandas
# 데이터 분석(Data Analysis)을 위해 널리 사용되는 라이브러리
# 아나콘다를 사용

# Series
# 가장 간단한 1차원 자료구조
# 배열/리스트와 같은 일련의 시퀀스 데이터를 받아들이는데,
# 별도의 인덱스 레이블을 지정하지 않으면 자동적으로 0부터 시작되는 디폴트 정수 인덱스를 사용
import pandas as pd

data = [1,3,5,7,9]
s = pd.Series(data)

# DataFrame
# 2차원 자료구조
# 행과 열이 있는 테이블 데이터(Tabular Data)를 받아들임
import pandas as pd

data = {
    'year':[2016, 2017, 2018],
    'GDP rate':[2.8, 3.1, 3.0],
    'GDP':['1.637M', '1.73M', '1.83M']
}

df = pd.DataFrame(data)

# Panel
# 3차원 자료구조
# Axis 0(items), Axis 1(major_axis), Axis 2(minor_axis) 등 2개의 축을 가지고 있음
# Axis 0은 그 한 요소가 2차원의 DataFrame에 해당
# Axis 1은 행(row)에 해당
# Axis 2는 열(colimn)에 해당
import pandas as pd
import numpy as np

data = np.random.rand(2,3,4)
p = pd.Panel(data)
print(p)

p[0]

# 데이터 엑세스
# pandas에서 Series, DataFrame, Panel 등의 자료구조를 만든 후, 다양한 방법을 통해 데이터를 엑세스 할 수 있다.

# 외부 데이터 엑세스 
# pandas는 CSV파일, 텍스트 파일, 엑셀 파일, SQL 데이터베이스, HDF5 포맷 등 다양한 외부 리소스에 데이터를 읽고 쓸 수 있는 기능을 제공
