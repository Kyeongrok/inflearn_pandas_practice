from matplotlib import pyplot as plt

x = ['Kyeongrok', 'Areum', 'Bright']
y_math = [60, 70, 80]
y_english = [88, 80, 70]
y_pe = [90,90,50]

plt.plot(x, y_math)
plt.plot(x, y_english)
plt.plot(x, y_pe)

plt.show()