import requests 
r = requests.get(
  url="http://api.miningindonesia.com/v1/dataset/survey", 
  headers={
    "api-key": "6rcWUxdVEAX5c8r17z9Il3OH1LsAknqQ",
  },
  params={
    "dataset_version_hash": "r2wRadly06mu8URe5KWAMVSRe91gFvct",
  },
)

json_response = r.json()
# print(json_response)
print(len(json_response['data']))