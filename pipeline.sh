#!/bin/bash

# Установка зависимостей
echo "Installing dependencies from requirements.txt..."
pip3 install -r requirements.txt --break-system-packages
echo "Dependencies installed."

# Генерация данных
echo "Starting data generation..."
python3 data_generation.py
echo "Data generation completed."

# Предобработка данных
echo "Starting data preprocessing..."
python3 data_preprocessing.py
echo "Data preprocessing completed."

# Обучение модели
echo "Starting model training..."
python3 model_training.py
echo "Model training completed."

# Тестирование модели
echo "Starting model testing..."
python3 model_testing.py
echo "Model testing completed."

