import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Path to your training data
data = pd.read_csv("/home/anupam/Downloads/Train/Train.csv")

X_train = data.iloc[:, :-1].values
Y_train = data.iloc[:, -1].values

# Normalizing the data
u = np.mean(X_train, axis=0)
std = np.std(X_train, axis=0)
X_train = (X_train - u) / std

# To show your data uncomment following
# plt.scatter(X_train[:, 4], Y_train)
# plt.title("Raw data")
# plt.show()

ones = np.ones((X_train.shape[0], 1))
X_train = np.hstack((ones, X_train))


def hypothesis(X, theta):
    return np.dot(X, theta)


def error(X, Y, theta):
    e = 0.0
    y_ = hypothesis(X, theta)
    e = np.sum((Y - y_) ** 2)
    m = X.shape[0]
    return e / m


def gradient(X, Y, theta):
    m = X.shape[0]
    y_ = hypothesis(X, theta)
    grad = np.dot(X.T, (y_ - Y))
    return grad / m


def gradient_descent(X, Y, learning_rate=0.1, max_iter=250):
    n = X.shape[1]
    theta = np.zeros((n,))
    error_list = []
    for i in range(max_iter):
        e = error(X, Y, theta)
        error_list.append(e)

        grad = gradient(X, Y, theta)
        theta = theta - learning_rate * grad
    return theta, error_list


# Give your files here as X_train, Y_train
theta, error_list = gradient_descent(X_train, Y_train)

# To confirm that your model is working correctly uncomment following
# plt.plot(error_list)
# plt.title("This shows that our algorithm works correctly")
# plt.show()

y_ = []
m = X_train.shape[0]
for i in range(m):
    pred = hypothesis(X_train[i], theta)
    y_.append(pred)
y_ = np.array(y_)


# r2_score to calculate accuracy
def r2_score(Y, Y_):
    num = np.sum((Y - Y_) ** 2)
    denom = np.sum((Y - np.mean(Y)) ** 2)
    score = (1 - num / denom)
    print(f"Your accuracy is {score * 100}%")


(r2_score(Y_train, y_))
