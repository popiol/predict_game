import os

import numpy as np

os.environ["CUDA_VISIBLE_DEVICES"] = ""
from tensorflow import keras

from src.pattern_guesser import PatternGuesser


class BasicModel(PatternGuesser):

    def __init__(self, dims: list[int]):
        super().__init__(dims)
        self.memory_length = 2
        self.model = self.create_model()
        self.memory = np.zeros((self.memory_length, *self.dims))
        
    def guess_next(self, last_pattern: np.array) -> np.array:
        self.model.fit(self.transform_input(self.memory), self.transform_input(last_pattern), epochs=1, verbose=0)
        for index in range(self.memory_length - 1):
            self.memory[index, :] = self.memory[index, :] * 0.1 + self.memory[index + 1, :] * 0.9
        self.memory = np.concatenate((self.memory[:-1, :], np.expand_dims(last_pattern, 0)))
        new_pattern = self.model.predict(self.transform_input(self.memory))
        return self.transform_output(new_pattern)

    def transform_input(self, x):
        return np.expand_dims(x, 0)

    def transform_output(self, x):
        return np.clip(np.round(x[0]).astype(int), 0, 1)

    def create_model(self) -> keras.Model:
        inputs = keras.layers.Input(shape=(self.memory_length, *self.dims))
        l = inputs
        l = keras.layers.UnitNormalization()(l)
        l = keras.layers.Flatten()(l)
        l = keras.layers.Dense(100)(l)
        l = keras.layers.Dense(np.prod(self.dims))(l)
        l = keras.layers.Reshape(self.dims)(l)
        outputs = l
        model = keras.Model(inputs=inputs, outputs=outputs)
        model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.002), loss=keras.losses.MeanSquaredError())
        model.summary()
        return model
