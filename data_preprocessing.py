import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

def preprocess_data(input_file, output_file):
    data = pd.read_csv(input_file)
    scaler = StandardScaler()
    data['Temperature'] = scaler.fit_transform(data[['Temperature']])
    data.to_csv(output_file, index=False)

preprocess_data('train/train_data.csv', 'train/preprocessed_train_data.csv')
preprocess_data('test/test_data.csv', 'test/preprocessed_test_data.csv')
