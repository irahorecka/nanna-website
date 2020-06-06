import datetime
import json
import os
import bs4
import requests

def get_youtube_channel_json(limit=100):
    yt_api_key = os.environ.get("YOUTUBE_API")
    yt_channel = os.environ.get("YOUTUBE_CHANNEL")
    yt_content = requests.get(f"https://www.googleapis.com/youtube/v3/search?key={yt_api_key}&channelId={yt_channel}&part=snippet,id&order=date&maxResults={limit}")
    return yt_content.json()

def trim_youtube_channel_json(youtube_channel_json):
    videos = youtube_channel_json['items']
    return [
        {
            'date': video['snippet']['publishedAt'][:10],
            'title': convert_encoded_char(video['snippet']['title']),
            'embed_url': f"https://www.youtube.com/embed/{video['id']['videoId']}",
        }
        for video in videos if video['id'].get('videoId')
    ]

def convert_encoded_char(video_title):
    encoded_dict = {
        '&amp;': '&'
    }
    for key, value in encoded_dict.items():
        if key in video_title:
            video_title = video_title.replace(key, value)
    return video_title

def main():
    full_channel_json = get_youtube_channel_json()
    trimmed_videos_json = trim_youtube_channel_json(full_channel_json)
    current_pyfile_dir = os.path.abspath(os.path.dirname(__file__))
    parent_pyfile_dir = os.path.abspath(os.path.join(current_pyfile_dir, os.pardir))
    with open(parent_pyfile_dir + '/nannaElise/static/videos.json', 'w') as outfile:
        json.dump({'videos': trimmed_videos_json}, outfile)

if __name__ == '__main__':
    main()
