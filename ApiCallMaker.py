import requests

import Keys

#google custom api
url = "https://www.googleapis.com/customsearch/v1"
params = {
    "q": "bentley",
    "key": Keys.GeminiApiKey,
    "cx": Keys.SearchEngineId,
    "searchType": "image"
}
response = requests.get(url,params=params)
result = response.json()["items"]
for item in result:
    print(item['link'])
    break