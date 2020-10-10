from googleapiclient.discovery import build
import requests
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
api_key = 'AIzaSyAuMGgTPCQKlwjedvzTm_Qu_d0ZyWE6kPw'
'''
youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
        part='statistics',
        forUsername='schafer5'
    )

response = request.execute()

'''

url = 'https://www.googleapis.com/youtube/v3/search'
params = {
    'part':'snippet',
    'q': 'official',
    'key': api_key,
    'publishedAfter': (datetime.utcnow() - timedelta(minutes=1)).isoformat("T") + "Z"
}
response = session.get(url,params=params)

#print(response.json())

for i in response.json()['items']:
    v={}
    v['title'] = i['snippet']['title']
    v['description'] = i['snippet']['description']
    v['urls'] = []
    for u in i['snippet']['thumbnails']:
        v['urls'].append(i['snippet']['thumbnails'][u]['url'])
    v['channelTitle'] = i['snippet']['channelTitle']
    v['published_at'] = datetime(*map(int, re.split('[^\d]', i['snippet']['publishTime'])[:-1]))
    print(v)