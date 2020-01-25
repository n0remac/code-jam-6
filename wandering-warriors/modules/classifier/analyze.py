import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
# from keras.models import load_model

from .train import TrainingData


def clean(data_in) -> np.array:
    x = np.array(data_in[0::2])
    y = np.array(data_in[1::2])

    # enforce a uniform length for training/analysis
    current_length = x.size
    target_length = 64
    if current_length > target_length:
        reduction_factor = int(current_length / target_length) + 1
        x = x[0::reduction_factor]
        y = y[0::reduction_factor]

    # normalized [0,255] as integer
    max_point = max(np.ptp(x), np.ptp(y))
    x = (255 * (x - np.min(x)) / max_point).astype(int)
    y = (255 * (y - np.min(y)) / max_point).astype(int)

    # pad with 0 up to target length
    if x.size < target_length:
        pad = target_length - x.size
        x = np.pad(x, pad_width=(0, pad))
        y = np.pad(y, pad_width=(0, pad))

    # visualize coordinates for development
    plot(x, y)

    return np.dstack((x, y))


def plot(x, y):
    c = cm.rainbow(np.linspace(0, 1, len(x)))
    plt.scatter(x=x, y=y, color=c)

    plt.axis('equal')
    plt.show()


def analyze(raw_data, training: bool = False):
    # don't attempt to classify tiny shapes
    if len(raw_data) < 20:
        return None

    clean_data = clean(raw_data)

    if training:
        print(clean_data.shape)
        training_data = TrainingData('./modules/classifier/cuneiform.npz')
        training_data.append(clean_data, 1)

    # model = load_model("model.h5")
    # prediction = model.predict(clean_data)
    # print(prediction.argmax())
