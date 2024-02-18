import numpy as np

class Perceptron:
    def __init__(self, num_features, learning_rate=0.01, num_epochs=100):
        self.num_features = num_features
        self.learning_rate = learning_rate
        self.num_epochs = num_epochs
        self.weights = np.zeros(num_features + 1)  # Add one for bias

    def train(self, X, y):
        X = np.column_stack((np.ones(len(X)), X))  # Add bias term
        for _ in range(self.num_epochs):
            for i in range(len(X)):
                prediction = self.predict(X[i])
                error = y[i] - prediction
                self.weights += self.learning_rate * error * X[i]

    def predict(self, x):
        x_with_bias = np.insert(x, 0, 1)  # Add bias term
        activation = np.dot(self.weights, x_with_bias)
        return 1 if activation >= 0 else 0

# Example usage:
X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_train = np.array([0, 0, 0, 1])

perceptron = Perceptron(num_features=2)
perceptron.train(X_train, y_train)

X_test = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
for x in X_test:
    prediction = perceptron.predict(x)
    print(f"Input: {x}, Predicted class: {prediction}")
