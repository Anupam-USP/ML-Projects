import numpy as np
import pandas as pd
import pred_algo

# Give path to your test data
X_test = pd.read_csv("/home/anupam/Downloads/Test/Test.csv")
X_test = np.array(X_test)
ones = np.ones((X_test.shape[0], 1))
X_test = np.hstack((ones, X_test))

y_test = []
m = X_test.shape[0]
for i in range(m):
    pred = pred_algo.hypothesis(X_test[i], pred_algo.theta)
    y_test.append([int(i), pred])
y_test = np.array(y_test)
# print(type(y_test))

df = pd.DataFrame(data=y_test, columns=['Id', 'target'])
df = df.astype({'Id': 'uint8', 'target': 'float64'})
# df.head()

# This converts your file to csv type
df.to_csv("Y_test.csv", index=False)
