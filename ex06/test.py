#!/usr/bin/env python3
import numpy as np
from prediction import predict_
from loss import loss_, loss_elem_
x1 = np.array([[0.], [1.], [2.], [3.], [4.]])
theta1 = np.array([[2.], [4.]])
y_hat1 = predict_(x1, theta1)
y1 = np.array([[2.], [7.], [12.], [17.], [22.]])
# Example 1:
print(repr(loss_elem_(y1, y_hat1)))
# Output:
# array([[0.], [1], [4], [9], [16]])
# Example 2:
print(loss_(y1, y_hat1))
# Output:
# 3.0
x2 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
theta2 = np.array([[0.05], [1.], [1.], [1.]])
y_hat2 = predict_(x2, theta2)
y2 = np.array([[19.], [42.], [67.], [93.]])
# Example 3:
print(loss_elem_(y2, y_hat2))
# Output:
# array([[10.5625], [6.0025], [0.1225], [17.2225]])
# Example 4:
print(loss_(y2, y_hat2))
# Output:
# 4.238750000000004
x3 = np.array([[0], [15], [-9], [7], [12], [3], [-21]])
theta3 = np.array([[0.], [1.]])
y_hat3 = predict_(x3, theta3)
y3 = np.array([[2], [14], [-13], [5], [12], [4], [-19]])
# Example 5:
print(loss_(y3, y_hat3))
# Output:
# 2.142857142857143
# Example 6:
print(loss_(y3, y3))
# Output:
# 0.0
