from matplotlib import pyplot as plt


def plot(raw_data: list):
    x = raw_data[0::2]
    y = raw_data[1::2]
    plt.scatter(x, y)
    plt.show()
    # return clean_data


def analyze(raw_data):
    print(type(raw_data))
    plot(raw_data)
