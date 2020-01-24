import numpy as np
import os


class TrainingData:
    def __init__(self, filepath):
        self.filepath = filepath

    def load(self):
        if not os.path.exists(self.filepath):
            print(f'File not found: {self.filepath}')
            return None, None
        else:
            with np.load(self.filepath, allow_pickle=True) as data:
                return data['x'], data['y']

    def append(self, points, label):
        x, y = self.load()

        if x is None or y is None:
            x = np.array(points)
            y = np.array(label)
        else:
            x = np.vstack((x, points))
            y = np.append(y, label)

        np.savez(self.filepath, x=x, y=y, allow_pickle=True)

        print(self.load())
