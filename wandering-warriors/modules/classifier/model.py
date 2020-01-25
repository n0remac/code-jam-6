from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv1D, MaxPooling1D

from train import TrainingData

# Import training data
training_data = TrainingData("cuneiform.npz")
(x_all, y_all) = training_data.load()

# Separate into test and training sets
test_size = 40
train_size = len(y_all) - test_size

x_train = x_all[0:train_size]
y_train = y_all[0:train_size]
x_test = x_all[-test_size:]
y_test = y_all[-test_size:]

print(x_train)
print(x_train.shape)


model = Sequential()

model.add(
    Conv1D(
        filters=32,
        kernel_size=3,
        activation="relu",
        input_shape=(64, 2),
    )
)

model.add(Dropout(0.3))
model.add(Dense(16, activation='relu'))
model.add(MaxPooling1D(pool_size=2))
model.add(Dropout(0.3))
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.summary()

# Train model
batch_size = 2
epochs = 10

model.fit(
    x=x_train,
    y=y_train,
    batch_size=batch_size,
    epochs=epochs,
    verbose=1,
    validation_data=(x_test, y_test),
    shuffle=True
)

score = model.evaluate(x_test, y_test, verbose=0)

print("Test loss:", score[0])
print("Test accuracy:", score[1])

model.save("cuneiform_model.h5")
