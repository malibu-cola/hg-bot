from line_bot.line.send_message import send_line
from line_bot.nasa_api.fetch_apod import fetch_apod
from line_bot.nasa_api.new_ws import fetch_new_ws
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    send_line(fetch_apod())
    send_line(fetch_new_ws())