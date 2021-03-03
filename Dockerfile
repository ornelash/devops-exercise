FROM python:rc-alpine

WORKDIR /usr/src/app

COPY requirement.txt app.py ./
RUN pip install --no-cache-dir -r requirement.txt

EXPOSE 5000

CMD [ "python", "./app.py" ]
