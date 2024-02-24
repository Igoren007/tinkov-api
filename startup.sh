#!/bin/bash
echo $MODE
if [ $MODE = "BOT" ]
then
	echo "режим бота"
    python3 tg_bot.py
elif [ $MODE = "HTTP" ]
then
	echo "режим http"
    python3 http_get_total_money.py
fi
