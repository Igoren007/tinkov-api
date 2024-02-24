Create venv:
python -m venv /path/to/new/virtual/environment

Activate venv:
source env/bin/activate

Deactivate:
deactivate


Собирается один образ, но в зависимости от переменной MODE запускаются разные скрипты.
Режим http сервера:
docker run -it --rm --name tink-app -e MODE=HTTP --net=host tinkof


Режим телегам бота:
docker run -it --rm --name tink-bot -e MODE=BOT --net=host tinkof