FROM python:3.9-slim

WORKDIR /app

COPY http_get_total_money.py .

COPY tg_bot.py .

COPY requirements.txt .
COPY startup.sh .

RUN pip install -r ./requirements.txt

#EXPOSE 8888
#CMD ["python", "http_get_total_money.py"]
ENTRYPOINT [ "./startup.sh" ]