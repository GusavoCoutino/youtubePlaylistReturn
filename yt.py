import re
from datetime import timedelta
from googleapiclient.discovery import build

def playlist_time(link):
    api_key = 'AIzaSyCTg7rbdALMaIm_3NKCd4NT7iyy3JqfBf0'

    youtube = build("youtube", "v3", developerKey=api_key)

    hours_pattern = re.compile(r'(\d+)H')
    minutes_pattern = re.compile(r'(\d+)M')
    second_pattern = re.compile(r'(\d+)S')

    total_seconds = 0

    playlist_id = link

    nextPageToken = None
    while True:
        pl_request = youtube.playlistItems().list(
            part='contentDetails',
            playlistId = playlist_id,
            maxResults = 50,
            pageToken = nextPageToken
        )
        pl_response = pl_request.execute()
        vid_ids = []
        for item in pl_response['items']:
            vid_ids.append(item['contentDetails']['videoId'])
        vid_request = youtube.videos().list(
            part='contentDetails',
            id=','.join(vid_ids)
        )

        vid_response = vid_request.execute()


        for item in vid_response['items']:
            duration = item['contentDetails']['duration']
            hours = hours_pattern.search(duration)
            minutes = minutes_pattern.search(duration)
            seconds = second_pattern.search(duration)

            if hours:
                hours = int(hours.group(1))
            else:
                hours = 0
            if minutes:
                minutes = int(minutes.group(1))
            else:
                minutes = 0
            if seconds:
                seconds = int(seconds.group(1))
            else:
                seconds = 0

            video_seconds = timedelta(
                hours=hours,
                minutes=minutes,
                seconds=seconds
            ).total_seconds()
            total_seconds += video_seconds
        nextPageToken = pl_response.get('nextPageToken')
        if not nextPageToken:
            break
    total_seconds = int(total_seconds)
    minutes, seconds = divmod(total_seconds, 60 )
    hours, minutes = divmod(minutes, 60)
    return (f'{hours}:{minutes}:{seconds}')
