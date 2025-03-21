import numpy as np
import pandas as pd
import os


# Функция для генерации данных
def generate_data(size=100, noise=False, anomaly=False):
    # Пример: данные об изменении дневной температуры
    x = np.arange(size)
    y = 10 * np.sin(0.1 * x) + 20

    if noise:
        y += np.random.normal(0, 1, size)  # Добавляем шум

    if anomaly:
        y[::10] += np.random.normal(50, 20, size // 10)  # Добавляем аномалии

    return pd.DataFrame({'Day': x, 'Temperature': y})


# Создаем папки, если их нет
os.makedirs('train', exist_ok=True)
os.makedirs('test', exist_ok=True)

# Генерация данных
train_data = generate_data(1000, noise=True, anomaly=False)
test_data = generate_data(300, noise=True, anomaly=True)

# Сохранение данных
train_data.to_csv('train/train_data.csv', index=False)
test_data.to_csv('test/test_data.csv', index=False)
