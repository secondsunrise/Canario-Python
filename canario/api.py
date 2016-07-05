import requests


class Canario():
    def __init__(self, api_key):
        self.api_key = api_key
        
    # Enables you to determine whether or not your key is working
    def test(self):
        payload = {"key": self.api_key, "action": "test"}
        r = requests.get("https://canar.io/_api/", params=payload)
        return r.text

    # Simple function for searches
    def search(self, query):
        payload = {"key": self.api_key, "action": "search", "query":query}
        r = requests.get("https://canar.io/_api/", params=payload)
        return r.text
    
    # Simple function for pulling specific views
    def view(self, item):
        payload = {"key": self.api_key, "action": "view", "item": item}
        r = requests.get("https://canar.io/_api/", params=payload)
        return r.text

    # Users with the ability to upload data to the Canario database can use this
    def store(self, title, text, source, source_url):
        if title is None:
            title = 'Untitled'
        payload = {"key": self.api_key, "action": "store", "title": title, "text": text, "source": source, "source_url": source_url}
        r = requests.get("https://canar.io/_api/", params=payload)
        return r.text
