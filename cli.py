import requests, bs4, json, os

class snusbase():
    key = 'sbu1u5krbvuh2e88fcx73ec6bn9v98'

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

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def valid_type(str_type):
    types = [
        'username', 
        'lastip',
        'email',
        'hash',
        'password',
        'name'
    ]

    for i in types:
        if i == str_type:
            return True

    return False

sb = snusbase()

while True:
    clear_console()

    search_type = input('[-] Search type..\n > ')
    if not valid_type(search_type):
        clear_console()
        print('[!] Invalid search type..\n')
        print('username -> username in the database')
        print('lastip -> last ip address used')
        print('email -> email in the database')
        print('hash -> hashed password in the database')
        print('password -> plain text password found')
        print('name -> full name in the database')
        input('\n[-] Enter to continue..')
        continue
    search_query = input('[-] Search query..\n > ')

    clear_console()

    print('Loading results..')

    results = sb.search({
		'type': search_type,
		'query': search_query
	})

    clear_console()

    print('Showing {} results for query "{}" (Type: "{}")\n'.format(len(results), search_query, search_type))
    for i in results:
        print('{}:'.format(i.lower()))
        recur1 = results[i]
        for ii in recur1:
            recur2 = ii
            for iii in recur2:
                print(' - {}: {}'.format(iii, recur2[iii]))
            print('')

    input('[-] Enter to continue..')
