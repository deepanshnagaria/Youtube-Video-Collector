from .models import Video
import requests
from .serializers import VideoSerializer
from datetime import date,datetime,timedelta
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from background_task import background
from googleapiclient.discovery import build
import re
session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)
import os


@background(schedule=0)
def collect():
    
    api_key = os.environ.get('API_KEY')
    url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'part':'snippet',
        'q': 'cricket',
        'key': api_key,
        'publishedAfter': (datetime.utcnow() - timedelta(minutes=1)).isoformat("T") + "Z"
    }
    response = session.get(url,params=params)

    if response.status_code == 403:
        return 
        
    for i in response.json()['items']:
        v={}
        v['title'] = i['snippet']['title']
        v['description'] = i['snippet']['description']
        v['urls'] = []
        for u in i['snippet']['thumbnails']:
            v['urls'].append(i['snippet']['thumbnails'][u]['url'])
        v['channelTitle'] = i['snippet']['channelTitle']
        v['published_at'] = datetime(*map(int, re.split('[^\d]', i['snippet']['publishTime'])[:-1]))
        serializer=VideoSerializer(data=v)

        if serializer.is_valid():
            serializer.save()

    return
