import warnings
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

warnings.filterwarnings('ignore')
plt.style.use("seaborn")

# Give path to your dataset
# Training data
x = pd.read_csv(
    "/home/anupam/Documents/ML_courses/CB/assignments/Training Data/Training Data/Logistic_X_Train.csv").values
y = pd.read_csv(
    "/home/anupam/Documents/ML_courses/CB/assignments/Training Data/Training Data/Logistic_Y_Train.csv").values
# Test data
x_ = pd.read_csv(
    "/home/anupam/Documents/ML_courses/CB/assignments/Training Data/Training Data/Test Cases/Logistic_X_Test.csv").values

x = (x - np.mean(x, axis=0)) / (np.std(x, axis=0))
x_ = (x_ - np.mean(x_, axis=0)) / (np.std(x_, axis=0))
indices = np.ones((3000, 1))
x = np.hstack((indices, x))
ones = np.ones((1000, 1))
x_ = np.hstack((ones, x_))


# Visualising the dataset, uncomment if you want
# plt.style.use("seaborn")
# plt.scatter(x[:, 1], x[:, 2], x[:, 3], c=y[:, 0], cmap=plt.cm.coolwarm_r)
# plt.show()


def getypred(theta, x):
    return 1 / (1.0 + np.exp(-(np.dot(x, theta))))


def predict(theta, x):
    y_pred = getypred(theta, x)
    result = np.zeros((y_pred.shape))
    result[y_pred > 0.5] = 1
    return result


def error(x, y, theta):
    y_ = getypred(theta, x)

    e = -(np.sum(y * np.log(y_) + (1 - y) * np.log(1 - y_)))
    m = x.shape[0]
    return e / m


def getGrad(x, y, theta):
    y_ = getypred(theta, x)
    grad = np.dot(x.T, (y_ - y))
    return grad


def gradDescent(x, y, lr, maxItr):
    theta = np.zeros((x.shape[1], 1))
    error_list = []

    for i in range(maxItr):
        grad = getGrad(x, y, theta)
        e = error(x, y, theta)
        theta = theta - lr * grad
        error_list.append(e)

    return theta, error_list


theta, error_list = gradDescent(x, y, 0.01, 200)

# Plot to show our model is working correctly
# plt.plot(error_list)
# plt.show()

# Plot to show our prediction
# plt.scatter(x[:, 1], x[:, 2], x[:, 3], c=y[:, 0], cmap=plt.cm.coolwarm_r)
# x1 = np.linspace(-3, +3, 5)
# x2 = -(theta[0] + theta[1] * x1) / theta[2]
# plt.plot(x1, x2)
# plt.show()

result = predict(theta, x_)
df = pd.DataFrame(data=result, columns=['label'])

# Conversion to csv typ file
df.to_csv("submission.csv", index=False)
