import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm


def clean(data_in) -> np.array:
    x = np.array(data_in[0::2])
    y = np.array(data_in[1::2])

    # Normalised [0,255] as integer
    max_point = max(np.ptp(x), np.ptp(y))
    x = (255 * (x - np.min(x)) / max_point).astype(int)
    y = (255 * (y - np.min(y)) / max_point).astype(int)

    # Visualize coordinates for development
    plot(x, y)

    return np.dstack((x, y))


def plot(x, y):
    c = cm.rainbow(np.linspace(0, 1, len(x)))
    plt.scatter(x=x, y=y, color=c)

    plt.axis('equal')
    plt.show()


def analyze(raw_data):
    clean_data = clean(raw_data)
    print(clean_data.shape)
