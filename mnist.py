import pickle
from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop

hidden_n = [32, 128, 512]
lr_n = [0.1, 0.01, 0.001]
epoch_n = [10, 30, 50]
batchs_n = [32, 128, 512]

all_settings = []
best_accuracy = 0
config = ()

for h in hidden_n:
    for l in lr_n:
        for e in epoch_n:
            for b in batchs_n:


                batch_size = b
                num_classes = 10
                epochs = e

                # the data, split between train and test sets
                (x_train, y_train), (x_test, y_test) = mnist.load_data()

                x_train = x_train.reshape(60000, 784)
                x_test = x_test.reshape(10000, 784)
                x_train = x_train.astype('float32')
                x_test = x_test.astype('float32')
                x_train /= 255
                x_test /= 255
                print(x_train.shape[0], 'train samples')
                print(x_test.shape[0], 'test samples')

                # convert class vectors to binary class matrices
                y_train = keras.utils.to_categorical(y_train, num_classes)
                y_test = keras.utils.to_categorical(y_test, num_classes)

                model = Sequential()
                model.add(Dense(h, activation='relu', input_shape=(784,)))
                model.add(Dropout(0.2))
                model.add(Dense(num_classes, activation='softmax'))

                model.summary()

                model.compile(loss='categorical_crossentropy',
                            optimizer=RMSprop(lr=l),
                            metrics=['accuracy'])

                history = model.fit(x_train, y_train,
                                    batch_size=batch_size,
                                    epochs=epochs,
                                    verbose=1,
                                    validation_data=(x_test, y_test))
                score = model.evaluate(x_test, y_test, verbose=0)
                print('Test loss:', score[0])
                print('Test accuracy:', score[1])

                all_settings.append((score[0], score[1]))


                if(score[1] > best_accuracy):
                    best_accuracy = score[1]
                    config = h, l, e, b


print('\n\n\n\n')
print('best accuracy: {}'.format(best_accuracy))
print(all_settings)
print('BEST_CONFIG:\nnumber hidden: {}\nlearning rate: {}\nnumber of epochs: {} \
\nnumber of batchs: {}\n'.format(config[0], config[1], config[2], config[3]))



data = [best_accuracy, all_settings, config]
with open('config', 'wb') as f:
    pickle.dump(data, f)

# recovery = pickle.load(open('config', 'rb'))