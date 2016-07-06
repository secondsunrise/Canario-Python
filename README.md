# Canario-Python
**Canario-Python** is a small library, written in Python, that is used to interact with the Canario API.

## Requirements
- [Python 2.7+][0]
- [Requests][1]
- [API Key from Canario][2]

## Usage
Getting started with **Canario-Python** is straightforward and simple. Import the library and then set your API key. 

```python
from canario import api
c = api.Canario(api_key="YOUR_API_KEY_HERE")
```

## Test
Test your API key to make sure you can successfully interact with the Canario API.
> **NOTE**: The "test" action isn't documented as it is only provided by [Canario](https://canar.io/help/api/#help_action_overview) for testing purposes.

```python
c.test()
```

## Search
Searches via **Canario-Python** can be performed as shown below. The syntax used for searches is the exact same syntax documented on the [Canario website][3]. Search results will be displayed in the same manner as discussed in the [API documentation][4].

```python
c.search("!host gmail.com")
```

## View
**Canario-Python** can be used to view the details of a specific result. It retrieves this information by using a *reference ID* as shown below. More information about viewing results can be found [here][5].

```python
c.view("9898fa737bdbbf056cbb4cb9fdb20b4c")
```

## Store
Users who are community members can upload data to the Canario database using the store function. 
> **NOTE**: This feature is not documented as it is not a feature typical to the average user.

The following information is required in order to upload into the database:

* Document title
* Document data (body)
* Source of the document (predefined by the community)
* Source URL of the document

It can then be pushed to the database using the following command:

```python
c.store(title="My title", text="My text", source="mysource", source_url="https://mysource/1.txt")
```

It will return an output that lets you know if it is successful or not.

[0]: https://www.python.org/downloads/
[1]: http://docs.python-requests.org/en/master/user/quickstart/
[2]: https://canar.io/register/
[3]: https://canar.io/help/#help_using
[4]: https://canar.io/help/api/#help_action_search
[5]: https://canar.io/help/api/#help_action_view
