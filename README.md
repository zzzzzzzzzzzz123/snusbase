main.py - The API for parsing snusbase search results
cli.py - Command line tool for making searches easier, formats the results as well

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

# Output:
# {
#     "AXESS_FR_2792_BUSINESS_112022": [
#       {
#         "username": "TEST",
#         "hash": "$2y$10$t9GFBvvvG5Q5dvTNq9.mgO2pLAiwXQCgQ9ZRU2t60/zci2vS.ROfW",
#         "name": "TEST TEST",
#         "id": "2606",
#         "created": "0"
#       }
#     ],
#     "SELFDEFENSEMALL_COM_935_DEFENSE_092023": [
#       {
#         "username": "test",
#         "email": "dgordon@aweomemotive.com",
#         "hash": "$P$BjJTbhGYVjn0nXX.PcXODdA7Wf4/CR1",
#         "name": "test",
#         "id": "697"
#       }
#     ],
#     ...
# }
```

**Hash cracking example:**
```python
print(snusbase().hash('693afde92014e104a40c59dabc0fba58')) # <- Returns the cracked hash, for example this outputs "Undertaker123"
```
