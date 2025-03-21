#!/bin/bash

# Создание и активация виртуального окружения
echo "Creating virtual environment..."
python -m venv venv
echo "Virtual environment created."

echo "Activating virtual environment..."
source venv/bin/activate
echo "Virtual environment activated."

# Установка зависимостей
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt
echo "Dependencies installed."

# Генерация данных
echo "Starting data generation..."
python data_generation.py
echo "Data generation completed."

# Предобработка данных
echo "Starting data preprocessing..."
python data_preprocessing.py
echo "Data preprocessing completed."

# Обучение модели
echo "Starting model training..."
python model_training.py
echo "Model training completed."

# Тестирование модели
echo "Starting model testing..."
python model_testing.py
echo "Model testing completed."

# Деактивация виртуального окружения
echo "Deactivating virtual environment..."
deactivate
echo "Virtual environment deactivated."