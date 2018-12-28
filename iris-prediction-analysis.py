from sklearn.datasets import load_iris
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

iris = load_iris()
#print(list(iris['data']))

X_train, X_test,y_train, y_test = train_test_split(iris['data'],iris['target'],random_state=0)

fig, ax = plt.subplots(3, 3, figsize=(15, 15))
plt.suptitle("iris_pairplot")
for i in range(3):
    for j in range(3):
        ax[i, j].scatter(X_train[:, j], X_train[:, i + 1], c=y_train, s=60)
        ax[i, j].set_xticks(())
        ax[i, j].set_yticks(())
        if i == 2:
            ax[i, j].set_xlabel(iris['feature_names'][j])
        if j == 0:
            ax[i, j].set_ylabel(iris['feature_names'][i + 1])
        if j > i:
            ax[i, j].set_visible(False)
#plt.show()

#pridction for new species
knn= KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,y_train)
X_new = np.array([[5, 2.9, 1, 0.2]])
print(X_new)
prediction = knn.predict(X_new)
print(iris['target_names'][prediction])