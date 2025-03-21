import pandas as pd
from sklearn.metrics import mean_squared_error
import pickle


def test_model(test_file, model_file):
    data = pd.read_csv(test_file)
    X_test = data[['Day']]
    y_test = data['Temperature']

    with open(model_file, 'rb') as f:
        model = pickle.load(f)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')


test_model('test/preprocessed_test_data.csv', 'model.pkl')
