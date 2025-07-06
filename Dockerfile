FROM python:3.9-slim-bullseye
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV FLASK_APP=app.py
ENV FLASk_ENV=development
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
