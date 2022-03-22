FROM tiangolo/uvicorn-gunicorn-fastapi:latest
COPY . .
RUN apt-get update -qq
RUN apt-get upgrade -qq
RUN python3 -m pip install --upgrade pip setuptools wheel
RUN python3 -m pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]