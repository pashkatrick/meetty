FROM python:3.8.7-slim-buster
WORKDIR /app
COPY . .
RUN pip install pip --upgrade
RUN pip install -U -r requirements.txt
RUN python3 bootstrap.py
EXPOSE 5000
CMD [ "python", "fastapp.py" ]

