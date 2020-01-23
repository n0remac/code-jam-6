import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm


def plot(raw_data: list):
    x = np.array(raw_data[0::2])
    y = np.array(raw_data[1::2])

    x = x - x.min()
    y = y - y.min()

    c = cm.rainbow(np.linspace(0, 1, len(y)))

    plt.scatter(x, y, color=c)

    plt.axis('equal')
    plt.show()


def analyze(raw_data):
    plot(raw_data)
