import matplotlib.pyplot as plt
from sklearn import linear_model
reg = linear_model.LinearRegression()
x = [[174], [152], [138], [128], [186]]
y = [71, 55, 46, 38, 88]
reg.fit(x, y)

reg.predict([[178]])
plt.scatter(x, y, color='blue')
plt.plot(x, reg.predict(x), color='blue', linewidth=3)
plt.show()
