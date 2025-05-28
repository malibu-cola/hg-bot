from line_bot.line.send_message import send_line
from line_bot.nasa_api.fetch_apod import fetch_apod
from line_bot.nasa_api.new_ws import fetch_new_ws
from dotenv import load_dotenv
from line_bot.kaggle_notification.fetch_information import fetch_competitions
from line_bot.youtube_podcast.save_and_send import save_and_send
load_dotenv()

if __name__ == "__main__":
    send_line(fetch_apod())
    if new_ws := fetch_new_ws():
        send_line(new_ws)
    if podcast:=save_and_send():
        send_line(podcast)
    if kaggle_info := fetch_competitions():
        send_line(kaggle_info)