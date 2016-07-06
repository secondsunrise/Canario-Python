import requests

api_key = "YOUR_API_KEY"
api_url = "https://canar.io/_api/"


# Run a search against the canar.io database. Searches should be performed
# exactly as they are outlined at https://canar.io/help/
def search(query):
    payload = {"key": api_key, "action": "search", "query": query}
    r = requests.get(api_url, params=payload)
    return r.text


# Returns the results for a reference ID
def view(item):
    payload = {"key": api_key, "action": "view", "item": item}
    r = requests.get(api_url, params=payload)
    return r.text


# Enables you to determine whether or not your key is working
def test():
    payload = {"key": api_key, "action": "test"}
    r = requests.get(api_url, params=payload)
    return r.text


# Users with the ability to upload data to the Canario database can use this
def store(title, text, source, source_url):
    if title is None:
        title = 'Untitled'
    payload = {"key": api_key, "action": "store", "title": title, "text": text, "source": source,
               "source_url": source_url}
    r = requests.get(api_url, params=payload)
    return r.text
