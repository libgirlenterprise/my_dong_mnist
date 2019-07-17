def train(self, data, config=None):

    self.compile(optimizer='adam',
                 loss='sparse_categorical_crossentropy',
                 metrics=['accuracy'])
    self.fit(data.get_train_data().x, data.get_train_data().y, epochs=3)

    return self.evaluate(data.get_eval_data().x, data.get_eval_data().y)[1]
