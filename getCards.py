import json, requests
    
def getallcardsdata(): #downloads the current all-cards.json file from scryfall. Just reads to memory, doesn't save it to a file.

    request_url = requests.get('https://api.scryfall.com/bulk-data')
    request_data = requests.get(request_url.json()['data'][3]['download_uri'])
    return request_data.json()
 
for card in getallcardsdata():
    if card['set'] == 'afr' and card['lang'] == 'en':
        r = requests.get(card['image_uris']['png'])
        card_name=card["collector_number"] + "_" + card['name'] + '.jpg'
        open(card_name, 'wb').write(r.content)
