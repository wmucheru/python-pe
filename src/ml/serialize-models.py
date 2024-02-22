import pickle

from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression


from utils import time_elapsed


model_filename = "linear_regression.pkl"


def pickel_model(model):
    with open(model_filename, "wb") as f:
        pickle.dump(model, f)


@time_elapsed
def unpickel_model():
    with open(model_filename, "rb") as f:
        unpickled_linear_model = pickle.load(f)


@time_elapsed
def train_model():
    # Generate regression dataset
    X, y = make_regression(n_samples=100, n_features=2, noise=0.1, random_state=1)

    # Train regression model
    linear_model = LinearRegression()
    linear_model.fit(X, y)

    # Print summary model parameters
    print("Model intercept: ", linear_model.intercept_)
    print("Model coefficients: ", linear_model.coef_)
    print("Model score: ", linear_model.score(X, y))

    # pickel_model(linear_model)


train_model()

# unpickel_model()
