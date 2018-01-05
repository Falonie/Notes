from ch02 import AdalineGD
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/rasbt/python-machine-learning-book/master/code/datasets/iris/iris.data',
    header=None)
df.tail()
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)
x = df.iloc[0:100, [0, 2]].values

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
ada1 = AdalineGD(n_iter=10, eta=.01).fit(x, y)
ax[0].plot(range(1, len(ada1.cost_) + 1), np.log10(ada1.cost_) + 1)
ax[0].set_xlabel('Epochs')
ax[0].set_ylabel('log(Sum-squared-error)')
ax[0].set_title('Adaline-Learning rate 0.01')
ada2 = AdalineGD(n_iter=10, eta=.0001).fit(x, y)
ax[1].plot(range(1, len(ada2.cost_) + 1), np.log10(ada2.cost_) + 1)
ax[1].set_xlabel('Epochs')
ax[1].set_ylabel('Sum-squared-error')
ax[1].set_title('Adaline-Learning rate 0.0001')
plt.show()
