# Використовуємо офіційний легкий образ Python
FROM python:3.10-slim

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо файл з залежностями
COPY requirements.txt .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо решту файлів проєкту
COPY . .

# Відкриваємо порт
EXPOSE 5000

# Запускаємо gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
