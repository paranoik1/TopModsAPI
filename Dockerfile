FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

CMD [ "fastapi", "run", "src/main.py" ]
#CMD [ "gunicorn", "src.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000" ]