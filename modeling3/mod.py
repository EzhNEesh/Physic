from random import random
import matplotlib.pyplot as plt

def get_I(wave, n, a, u, um):
    I = []
    t = []
    N = 5 * 10 ** 7
    h = 6.63 * 10 ** (-34)
    e = 1.6 * 10 ** (-19)
    nu = (3 * 10 ** 8) / (wave * 10 ** (-9))
    Uz = h * nu / e - a[n - 1]
    print("Uz = ", Uz)
    if u - Uz < (um[n - 1] - Uz):
        N = N * (u - Uz) / (um[n - 1] - Uz)
    for i in range (100):
        if u < Uz or wave * 10 ** (-9) > (h * 3 * 10 ** 8) / a[n - 1] / e:
            I.append(10 * e * (1 - 0.3 * random() / 100))
        else:
            I.append(N * e * (1 - 0.3 * random() / 100))
        t.append(i)
    return I, t




lamda = int(input("Enter wavelegth(nm): "))
print("Choose metal:\n"
      "1. Fe\n"
      "2. Na\n"
      "3. Cu\n"
      "4. Ni\n"
      "5. Si\n"
      "6. W\n")
number = int(input("Enter number: "))
A = [4.4, 2.28, 4.36, 4.91, 3.59, 4.54]
U_metals = [15, 7.5, 14.8, 15.5, 13.4, 15.4]
U = float(input("Voltage(V): "))
time = 0
Y, time = get_I(lamda, number, A, U, U_metals)
plt.plot(time, Y, 'b')
plt.xlabel('Время, с')
plt.ylabel('Фототок, А')
plt.show()