# Dockerfile

FROM python:3.6-alpine3.6

RUN pip3 install --no-cache-dir "Flask>=0.12"

EXPOSE 5000

WORKDIR /app
ENV FLASK_APP=/app/hello.py

COPY hello.py /app/hello.py

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

