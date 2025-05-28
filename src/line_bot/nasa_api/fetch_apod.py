import requests
import os
from textwrap import dedent
from line_bot.util.translate import translate_text


def fetch_apod() -> str|None:
    try:
        nasa_key = os.getenv("NASA_API_KEY")
        url = f"https://api.nasa.gov/planetary/apod?api_key={nasa_key}"
        data = requests.get(url).json()

        title = data["title"]
        explanation_en = data["explanation"][:1000]
        explanation_ja = translate_text(explanation_en)
        image_url = data["url"]

        return dedent(f"""
        今日のNASAの画像をお届け!
        【タイトル】{title}\n\n
        【日本語訳】
        {explanation_ja}\n\n
        【画像はこちら】
        {image_url}
        """)
    except Exception as e:
        print(f"APODの取得中にエラーが発生しました: {e}")
        return None