FROM python:3.11

RUN mkdir /victorina

WORKDIR /victorina

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /victorina/docker/app.sh

# RUN alembic upgrade head

CMD ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]
