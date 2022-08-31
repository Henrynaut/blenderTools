import numpy as np
import matplotlib.pyplot as plt

x = [95, 102.5]
y = [5, 17]

x_new = []
y_new = []
i = x[0]

delta = 0.5
while(i < (x[1] - delta)):
    i = i + delta
    x_new.append(i)
    print(i)
# x_new = 100

for element in x_new:
    y_new.append(np.interp(element, x, y))

# print(y_new)
# # 13.0


plt.plot(x, y, "og-", x_new, y_new, "or")
plt.show()