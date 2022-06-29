FROM python:3.10.5-slim-buster
WORKDIR /app
COPY . .
RUN pip install pip --upgrade
RUN pip install -U -r requirements.txt
# RUN python3 bootstrap.py
EXPOSE 5000
CMD [ "python", "app.py" ]

