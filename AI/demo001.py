import numpy
import matplotlib
import sklearn

#ボストン住宅価格
from sklearn.datasets import load_boston

boston = load_boston()
print(boston.data.shape)

data, target = load_boston(return_X_y=True)
print(data.shape)
print(target.shape)

print("===============================")

#アイリスの品種分類
from sklearn.datasets import load_iris

iris = load_iris()
print(iris.data.shape)
print(iris.target.shape)
print(list(iris.target_names))

print("===============================")

#手書き文字
from sklearn.datasets import load_digits

digits = load_digits()
print(digits.data.shape)
print(digits.target.shape)
print(digits.images.shape)
import matplotlib.pyplot as plt
plt.matshow(digits.images[0])
plt.show()
