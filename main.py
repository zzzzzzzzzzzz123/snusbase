import requests, bs4, json

class snusbase():
    key = 'sbu1u5krbvuh2e88fcx73ec6bn9v98' # example key, expires on January 12, 2023.

    def hash(self, a):
        response = requests.get('https://api-experimental.snusbase.com/legacy/hash-lookup/{}'.format(a))

        try:
            if response.json()['found'] == True:
                return response.json()['password']
            else:
                # no hash found
                print('Not found')
                return False
        except:
            # error
            return False

    def search(self, a):
        if type(a) != dict:
            print('[!] Incorrect args \nExample:\n{\n\t"type": "username",\n\t"query": "test"\n}')
            return False
        
        if not 'type' in a:
            print('[!] Missing arg "type"')
            return False

        if not 'query' in a:
            print('[!] Missing arg "query"')
            return False
        
        response = requests.post(
            'https://beta.snusbase.com/',
            json = {
                'activation_code': self.key,
                'term': a['query'],
                'type': a['type'],
                'wildcard': 'on'
            }
        )

        try:
            results = {}
            soup = bs4.BeautifulSoup(response.text, 'html.parser')
            for i in soup.find_all('div', class_ = 'results'):
                database = []

                for b in i.find_all('div', class_ = 'r-i'):
                    thisdata = {}
                    keyval = True
                    lastkey = ''
                    for c in b.find_all('span'):
                        if keyval == True:
                            lastkey = c.string
                            keyval = False
                        else:
                            keyval = True
                            thisdata[lastkey] = c.string

                    database.append(thisdata)
            
                results[i.label.span.string] = database
        except:
            return False

        return results

# Example search usage

print(json.dumps(
    snusbase().search({
        'type': 'username',
        'query': 'test'
    }),
    indent = 2
))

# Example hash usage

print(snusbase().hash('e7afc95f9d366b64ccdf0d7aaf6ccfba'))
