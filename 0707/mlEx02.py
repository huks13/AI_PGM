from sklearn.datasets import load_iris
import pandas as pd
import plotly.express as px
from sklearn import svm

# 1. 데이터 로드
iris = load_iris()

# 2. SVM 모델 학습 및 예측
s = svm.SVC(gamma=0.1, C=10)
s.fit(iris.data, iris.target)

new_d = [[6.4, 3.2, 6.0, 2.5], [7.1, 3.1, 4.7, 1.35]]
res = s.predict(new_d)
print("새로운 2개 샘플의 부류는", res)

# 3. 데이터프레임 생성 및 'species' 컬럼 추가 ✨
df = pd.DataFrame(iris.data, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
df['species'] = iris.target  # 정답 레이블(0, 1, 2)을 species 컬럼으로 추가
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'}) # 숫자를 꽃 이름으로 가독성 좋게 변환

# 4. 3차원 시각화 (petal_length 제외)
fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width', color='species')
fig.show(renderer="browser")