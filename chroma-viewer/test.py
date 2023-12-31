import requests
import json

# url = "https://llamaindexdemo.atlassian.net/wiki/rest/api/content"
url = "https://llamaindexdemo.atlassian.net/wiki/rest/api/space"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

if response.status_code == 200:
    # Convert JSON response to dictionary
    data_dict = json.loads(response.text)
    print(data_dict)
else:
    print("Request was not successful. Status code:", response.status_code)
    
import chromadb
client = chromadb.Client()
collection = client.create_collection(name="test")
documents =[]
metadata = []
ids = []
for i in range(0, len(data_dict['results'])):
  documents.append(data_dict['results'][i]['name'])
  meta = {
        "source": data_dict['results'][i]['key']
    }
  metadata.append(meta)
  ids.append(str(data_dict['results'][i]['id']))
  
  collection.add(
    documents = documents,
    metadatas = metadata,
    ids = ids
)