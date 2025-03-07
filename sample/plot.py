import matplotlib.pyplot as plt

plt.style.use("ebi_mpl.lab")

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, label='1')
plt.plot(x, [2 * yi for yi in y], label='2')
plt.plot(x, [3 * yi for yi in y], label='3')
plt.plot(x, [4 * yi for yi in y], label='4')
plt.plot(x, [5 * yi for yi in y], label='5')

plt.xlabel("X values")
plt.ylabel("Y values")
plt.legend()
plt.tight_layout()

plt.show()
