import json
from pathlib import Path
from textwrap import dedent

from line_bot.youtube_podcast.fetch_playlist import get_playlist_videos

def load_sent_log(filepath: str) -> set[str]:
    path = Path(filepath)
    if not path.exists() or path.stat().st_size == 0:
        return set()
    with open(filepath, "r", encoding="utf-8") as f:
        return set(json.load(f))


def save_sent_log(sent_set: set[str], filepath: str):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(list(sent_set), f, indent=2, ensure_ascii=False)

def get_next_unsent_video(all_videos: list[tuple[str, str]], sent_urls: set[str]) -> tuple[str, str] | None:
    for title, url in all_videos:
        if url not in sent_urls:
            return (title, url)
    return None

def save_and_send() -> str | None:
    all_videos = get_playlist_videos()
    sent_urls = load_sent_log("./sent_videos.json")

    next_video = get_next_unsent_video(all_videos, sent_urls)
    if next_video:
        try:
            title, url = next_video
            print(f"送信対象: {title} - {url}")
            sent_urls.add(url)
            save_sent_log(sent_urls, "sent_videos.json")
            return dedent(f"""
                    【🌌本日の宇宙物理Podcast】
                    タイトル: {title}
                    URL: {url}
                    """).strip()
        except Exception as e:
            print(f"送信中にエラーが発生しました: {e}")
            return None
    else:
        print("すべての動画はすでに送信済みです。")
        return None
