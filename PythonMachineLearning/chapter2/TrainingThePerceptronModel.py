import matplotlib.pyplot as plt
from perceptron import Perceptron
from ch02 import x,y

ppn=Perceptron(eta=.1,n_iter=10)
ppn.fit(x,y)
plt.plot(range(1,len(ppn.errors_)+1),ppn.errors_,marker='o')
plt.xlabel('Epochs')
plt.ylabel('Number of misclassifications')
plt.show()