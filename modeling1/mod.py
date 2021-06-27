from random import random
import matplotlib.pyplot as plt
import numpy as np

sigma = 5.67 * 10 ** (-8)

print("Select surface:\n"
      "1. Black;\n"
      "2. White;\n"
      "3. Matte;\n"
      "4. Silver;\n"
      "5. All;\n")
N = int(input("Input number: "))
A = 1
if (N == 1):
    A = 0.95
elif(N == 2):
    A = 1
elif(N == 3):
    A = 0.16
elif (N == 4):
    A = 0.04
elif (N == 5):
    A = [0.95, 1, 0.16, 0.04]

#y = [0.02, 0.12, 0.229, 0.392, 0.509, 0.630, 0.809]
T = [298.15]
X = [0]
y = [0]
y0 = [0]
y1 = [0]
y2 = [0]
y3 = [0]
teor = [0]
teor0 = [0]
teor1 = [0]
teor2 = [0]
teor3 = [0]

if (N != 5):
    for i in range(1, 76):
        T.append(i + 298.15)
        X.append((T[i] ** 4 - 298.15 ** 4) / 10 ** 8)
        p = (1 - 5 * random() / 100)
        y.append(A * sigma * X[i] * p * 10 ** 6)
        teor.append(A * sigma * X[i] * 10 ** 6)
else:
    for i in range(1, 76):
        T.append(i + 298.15)
        X.append((T[i] ** 4 - 298.15 ** 4) / 10 ** 8)
        y0.append(A[0] * sigma * X[i] * (1 - 5 * random() / 100) * 10 ** 6)
        y1.append(A[1] * sigma * X[i] * (1 - 5 * random() / 100) * 10 ** 6)
        y2.append(A[2] * sigma * X[i] * (1 - 5 * random() / 100) * 10 ** 6)
        y3.append(A[3] * sigma * X[i] * (1 - 5 * random() / 100) * 10 ** 6)
        teor0.append(A[0] * sigma * X[i] * 10 ** 6)
        teor1.append(A[1] * sigma * X[i] * 10 ** 6)
        teor2.append(A[2] * sigma * X[i] * 10 ** 6)
        teor3.append(A[3] * sigma * X[i] * 10 ** 6)
#x = [12.097, 12.346, 12.5, 12.987, 13.273, 13.575, 14.019]


# Plot the best fit line over the actual values

if (N != 5):
    b, a = np.polyfit(X, y, 1)
    abline_values = [b * i + a for i in X]
    plt.plot(X, y, 'b')
    plt.plot(X, teor, '--')
    plt.plot(X, abline_values, '--')
    #plt.title('График зависимости излучающей способности от X^4')
    plt.xlabel('X^4, 10^-8 К^4')
    plt.ylabel('Интенсивность излучения, мВ')
    a_ = round(a, 3)
    #slo = round(b, 18)
    plt.show()
    print("b =", b, "a =", a)
else:
    plt.plot(X, y0, 'b')
    plt.plot(X, y1, 'b')
    plt.plot(X, y2, 'b')
    plt.plot(X, y3, 'b')
    plt.plot(X, teor0, '--')
    plt.plot(X, teor1, '--')
    plt.plot(X, teor2, '--')
    plt.plot(X, teor3, '--')
    # plt.title('График зависимости излучающей способности от X^4')
    plt.xlabel('X^4, 10^-8 К^4')
    plt.ylabel('Интенсивность излучения, мВ')
    # slo = round(b, 18)
    plt.show()