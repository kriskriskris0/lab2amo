import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

def train_model(train_file, model_file):
    data = pd.read_csv(train_file)
    X = data[['Day']]
    y = data['Temperature']

    model = LinearRegression()
    model.fit(X, y)

    with open(model_file, 'wb') as f:
        pickle.dump(model, f)

train_model('train/preprocessed_train_data.csv', 'model.pkl')
