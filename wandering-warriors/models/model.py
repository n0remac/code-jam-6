from keras.datasets import mnist
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D

# Import training data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Clean training data
img_rows, img_cols = 28, 28

x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
x_train = x_train / 255
x_test = x_test / 255
print(x_train.shape)
print(x_test.shape)

num_classes = 10
y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)
print(y_train.shape)
print(y_test.shape)

# Create Model
# empty model object "Linear stack of layers"
model = Sequential()

# add convolution layer
model.add(
    Conv2D(
        filters=32,
        kernel_size=(3, 3),
        activation="relu",
        input_shape=(img_rows, img_cols, 1),
    )
)

# Rectified Linear Units (max of a value or zero)
model.add(Conv2D(64, (3, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

# pooling layer
model.add(Conv2D(64, (3, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

# drop 25% of units to prevent overfitting
model.add(Dropout(0.25))

# convert the previous hidden layer into a 1D array
model.add(Flatten())

# dense hidden layer
model.add(Dense(units=128, activation="relu"))
model.add(Dropout(0.5))

# softmax classifies data into a number of pre-decided classes
model.add(Dense(units=num_classes, activation="softmax"))

# Compile model
model.compile(
    loss="categorical_crossentropy",
    optimizer="adam",
    metrics=["accuracy"]
)

model.summary()

# Train model
batch_size = 128
epochs = 5

model.fit(
    x=x_train,
    y=y_train,
    batch_size=batch_size,
    epochs=epochs,
    verbose=1,
    validation_data=(x_test, y_test),
)

score = model.evaluate(x_test, y_test, verbose=0)

print("Test loss:", score[0])
print("Test accuracy:", score[1])

model.save("test_model.h5")
