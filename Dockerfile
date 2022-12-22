FROM python:3.10-slim
WORKDIR /app
# COPY requirements.txt ./
# RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
ENV   PYTHONUNBUFFERED 1
COPY . .

EXPOSE 80

CMD ["python", "openai_telegram_bot.py"]
