import requests
import json

api_key = "YOUR_API_KEY"
api_url = "https://canar.io/_api/"


# Run a search against the canar.io database. Searches should be performed
# exactly as they are outlined at https://canar.io/help/
def search(query):
    payload = {"key": api_key, "action": "search", "query": query}
    r = requests.get(api_url, params=payload)
    return r.json()


# Returns the results for a reference ID
def view(item):
    payload = {"key": api_key, "action": "view", "item": item}
    r = requests.get(api_url, params=payload)
    return r.json()


# Enables you to determine whether or not your key is working
def test():
    payload = {"key": api_key, "action": "test"}
    r = requests.get(api_url, params=payload)
    return r.json()


# Users with the ability to upload data to the Canario database can use this
def store(title, text, source, source_url):
    if title is None:
        title = 'Untitled'
    payload = {"key": api_key, "action": "store", "title": title, "text": text, "source": source,
               "source_url": source_url}
    r = requests.get(api_url, params=payload)
    return r.json()
    
# Return a list of all urls associated with a search
def get_urls(search):
    referenceids = []
    urls = []

    for result in search["data"]["results"]["results"]:
        referenceids.append(result["referenceid"])

    for refid in referenceids:
        urls.append(view(refid)["data"]["sources"][0]["url"])
    return urls


# Write JSON data to a file
def write_to_file(filename, data):
    with open(filename, 'wb') as f:
        f.write(json.dumps(data, indent=4))
