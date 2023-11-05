**Requirements:**
- Python 3+
- Python imports: requests, BeautifulSoup 4

**Installation:**
- pip install beautifulsoup4
- pip install requests

**Search example:**
```python
print(json.dumps(
    snusbase().search({
        'type': 'username', # <- This is the type of search, this can be username, password, email, lastip, hash, name.
        'query': 'test' # <- This is the query, what will be searched in snusbase's databases.
    }),
    indent = 2
))
```

**Hash cracking example:**
```python
print(snusbase().hash('693afde92014e104a40c59dabc0fba58')) # <- Returns the cracked hash, for example this outputs "Undertaker123"
```
