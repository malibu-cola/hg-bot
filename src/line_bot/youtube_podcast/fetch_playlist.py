import os
import requests

def get_playlist_videos():
    playlist_id = os.getenv("PLAYLIST_ID")
    api_key = os.getenv("YOUTUBE_API_KEY")
    
    url = "https://www.googleapis.com/youtube/v3/playlistItems"
    videos = []
    next_page_token = ""

    while True:
        params = {
            "part": "snippet",
            "playlistId": playlist_id,
            "maxResults": 50,
            "key": api_key,
            "pageToken": next_page_token
        }

        res = requests.get(url, params=params)
        res.raise_for_status()
        data = res.json()

        for item in data["items"]:
            snippet = item["snippet"]
            video_id = snippet["resourceId"]["videoId"]
            title = snippet["title"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            videos.append((title, video_url))

        next_page_token = data.get("nextPageToken")
        if not next_page_token:
            break

    return videos