docker run -d --rm -p 127.0.0.1:32768:6379 redis
gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker