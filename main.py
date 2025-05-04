from line_bot.line.send_message import send_line
from line_bot.nasa_api.fetch_apod import fetch_apod
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    send_line(fetch_apod())